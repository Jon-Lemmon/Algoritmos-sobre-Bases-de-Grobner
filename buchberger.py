import copy
import sympy as sp

class Buchberger_Algorithms():

  ##### Variáveis da Classe
    def __init__(self):
        self.variaveis = '' # Variáveis do anel de polinômios atual



  ##### Funções da Classe
  # Funções cujo objetivo é apenas facilitar a execução prática dos algorítmos

    def set_variaveis(self, variaveis: str): # Formato da string: 'a b c1:4 x0:5'; Gera: a, b, c1, c2, c3, x0, x1, x2, x3, x4
        self.variaveis = sp.symbols(variaveis)
    
    def criar_polinomio(self, polinomio: str): # Formato da string: '2*x0**2 - 8*x1 + (5/3)*x3**4'
        return sp.Poly(polinomio, self.variaveis)
    
    def criar_polinomios(self, *polinomios: str):
        return [self.criar_polinomio(p) for p in polinomios]



  ##### Funções Auxiliares
  # Funções que organizam os cálculos feitos dentro de funções maiores

    # S-Polinômio de p e q
    def S(self, p: sp.Poly, q: sp.Poly):
        mmc = sp.lcm(sp.LM(p), sp.LM(q)) # MMC(LM(p), LM(q))
        return (mmc / sp.LT(p))*p - (mmc / sp.LT(q))*q # (mmc/LT(p))p - (mmc/LT(q))q
    
    # p -> h mod d
    def reduz_em_um_passo(self, p: sp.Poly, d: sp.Poly):
        LT_d = d.LT() # (monomio, coeficiente)
        
        print('    Reduzindo', p, 'módulo', d, ':')
        # confere se LT_d divide algum termo de p
        
        for monomio, coeficiente in p.terms():
            # monomio é uma tupla de expoentes
            # LT_d[0] é o monômio líder de d e se comporta como lista de expoentes
            if all(m >= l for m, l in zip(monomio, LT_d[0])): # Se LT_d divide monomio ...
                # Obtém o termo atual em expressão que o SymPy saiba calcular
                termo = 1
                for exp, var in zip(monomio, self.variaveis):
                    termo *= var**exp
                termo *= coeficiente

                # Transforma LT_d em Poly
                LT_d = LT_d[1] * LT_d[0].as_expr()

                print('    Encontrado:', termo, 'é divisível por', LT_d)

                # Retorna a redução
                h = p - (termo/LT_d)*d
                print('    Retornando redução:', h)

                print()
                return h
            # else, continua procurando nos termos de p
        print('   ', p, 'não é divisível por', d, '! Retornando False...')

        print()
        return False

    # p -> h mod F
    def reduz(self, p: sp.Poly, F: list[sp.Poly]):
        # Aplica reduções a um passo até h ser irredutível (0 ou não divisivel por nenhum LT(d))
        h = p
        print('  Reduzindo', p, 'sucessivamente módulo', F, ':')
        while True:
            for d in F:
                reducao = self.reduz_em_um_passo(h, d)
                if reducao: # passo feito, prossegue para o próximo passo
                    h = reducao
                    break
                elif reducao is not False and reducao.is_zero: # Redução terminou bem
                    return reducao
                #else reducao == False:
                #   passo não feito, tenta próximo d
            else:
                # Redução terminou em um h != 0
                return h



  ##### Funções de Alto Nível
  # Funções que encapsulam as funcionalidades visiveis ao usuário, que resolvam as perguntas e operações de seu interesse
    
    # Responde se F é uma base de Gröbner ou não (Buchberger I)
    def is_grobner(self, F: list[sp.Poly]):
        # Iterando apenas triangular superior da matriz GxG, evitando assim sua diagonal
        for i in range(len(F)):
            for j in range(i+1, len(F)):
                # Se pelo menos uma das reduções for diferente de zero, então não é Gröbner
                if not self.reduz(self.S(F[i], F[j]), F).is_zero:
                    return False
                if not self.reduz(self.S(F[j], F[i]), F).is_zero:
                    return False
        #else, é Gröbner
        return True
    
    # Calcula a base de Grobner reduzida de F (Buchberger II)
    def grobner_reduzido(self, F: list[sp.Poly]):
        G = copy.deepcopy(F)
        print('Reduzindo', G, ':')
        
        i = 0
        while i < len(G):
            # Reduz módulo G - G[i]
            h = self.reduz(G[i], G[:i]+G[i+1:])
            
            if h.is_zero: # G[i] é figurinha repetida
                print('Descartando', G.pop(i), '...')
                # quem tinha o índice i+1 agora vira i, então não precisamos acrescentar o valor de i
            else:
                # Deixa mônico
                G[i] = sp.Poly( h / h.LT()[1], self.variaveis )
                i += 1
        
        return G
    
    # Responde se F é uma base de Gröbner reduzida ou não
    def is_grobner_reduzido(self, G: list[sp.Poly]):
        for g in G:
            if g.LT()[1] != 1: # Não é mônico
                print(g, 'não é mônico; G não é reduzido!')
                print()
                return False
        #else:
        for i in range(len(G)):
            for d in G[:i]+G[i+1:]:
                h = self.reduz_em_um_passo(G[i], d)
                if h is not False:
                    print(G[i], '-->>', h, ';', 'G não é reduzido!')
                    print()
                    return False
        #else:
        print(G, 'é reduzido.')
        print()
        return True
    
    # Responde se o polonômio p pertence ao ideal I
    def pertence_ao_ideal(self, p: sp.Poly, I: list[sp.Poly]):
        I_grobner_reduzido = self.grobner_reduzido(I)
        print('Reduzindo', p, 'sucessivamente módulo', I_grobner_reduzido, ':')
        if self.reduz(p, I_grobner_reduzido).is_zero:
            print(p, 'pertence a', I)
            print()
            return True
        else:
            print(p, 'não pertence a', I)
            print()
            return False

    # Responde se os conjuntos de polinômios I e J geram o mesmo ideal ou não
    def sao_iguais(self, I: list[sp.Poly], J: list[sp.Poly]):
        I_grobner_reduzido = self.grobner_reduzido(I)
        J_grobner_reduzido = self.grobner_reduzido(J)
        print('Comparando', I_grobner_reduzido, 'e', J_grobner_reduzido, '...')
        return set(I_grobner_reduzido) == set(J_grobner_reduzido)
