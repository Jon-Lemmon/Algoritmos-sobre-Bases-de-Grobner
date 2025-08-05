import sympy as sp

class Buchberger_Algorithms():

  ##### Variáveis da Classe
    def __init__(self):
        self.variaveis = '' # Variáveis do anel de polinômios atual

    
  ##### Funções da Classe 
  # Funções cujo objetivo é apenas facilitar a execução prática dos algorítmos

    def set_variaveis(self, variaveis: str): # Formado da string: 'a b c1:4 x0:5'; Gera: a, b, c1, c2, c3, x0, x1, x2, x3, x4
        self.variaveis = sp.symbols(variaveis)
    
    def criar_polinomio(self, polinomio: str): # Formato da string: '2*x0**2 - 8*x1 + (5/3)*x3**4'
        return sp.Poly(polinomio, self.variaveis)
    
    def criar_polinomios(self, *polinomios: str):
        return [self.criar_polinomio(p) for p in polinomios]
    

  ##### Funções Auxiliares
  # Funções que organizam os cálculos feitos dentro de funções maiores

    # S-Polinômio de p e q
    def S(self, p: sp.Poly, q: sp.Poly):
        mmc = sp.lcm(sp.LM(p), sp.LM(q)) # MMC(p_mon, q_mon)
        return (mmc / sp.LT(p))*p - (mmc / sp.LT(q))*q # (m/p_top)p - (m/q_top)q


  ##### Funções de Alto Nível
  # Funções que encapsulam as funcionalidades visiveis ao usuário, que respondam as perguntas e façam as operações de seu interesse
    
    # Responde se F é uma base de Gröbner ou não
    def is_grobner(self, F: list[sp.Poly]):
        # Iterando apenas triangular superior da matriz GxG, evitando assim sua diagonal
        for i in range(len(F)):
            for j in range(i+1, len(F)):
                Q, r = sp.reduced(self.S(F[i], F[j]), F)
                if not r.is_zero:
                    return False
                Q, r = sp.reduced(self.S(F[j], F[i]), F)
                if not r.is_zero:
                    return False
        return True
    
    # Calcula a base de Grobner reduzida de F
    def grobner_reduzido(self, F: list[sp.Poly]):
        return sp.groebner(F, method='buchberger') # O método pode ser Buchberger (lento), F5 (otimizado) ou F5B (meio-termo)
    
    # Responde se F é uma base de Gröbner reduzida ou não
    def is_grobner_reduzido(self, G: list[sp.Poly]):
        return G == self.grobner_reduzido(G)
    
    # Responde se o polonômio p pertence ao ideal I
    def pertence_ao_ideal(self, p: sp.Poly, I: list[sp.Poly]):
        I_grobner_reduzido = self.grobner_reduzido(I)
        return sp.reduced(p, I_grobner_reduzido)[1].is_zero # [1] é o resto da redução. Se é o polinômio nulo, p pertence a I.

    # Responde se os conjuntos de polinômios I e J geram o mesmo ideal ou não
    def sao_iguais(self, I: list[sp.Poly], J: list[sp.Poly]):
        return self.grobner_reduzido(I) == self.grobner_reduzido(J)
