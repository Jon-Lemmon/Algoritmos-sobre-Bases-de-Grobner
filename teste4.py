import buchbeasy
import buchberger

beasy  = buchbeasy.Buchberger_Algorithms()
berger = buchberger.Buchberger_Algorithms()

variaveis = 'x y z'
beasy.set_variaveis(variaveis)
berger.set_variaveis(variaveis)

### Teste 4: Exercícios básicos
# Testando os resultados de buchberger.py, observando se eles batem com os obtidos com buchbeasy.py
p1, p2 = beasy.criar_polinomios('x**2 - y', 'y**2')
L = [p1, p2]

print('O conjunto {x**2 - y, y**2} é uma base de Gröbner?')
print('Berger:', berger.is_grobner(L))
print('Beasy: ', beasy.is_grobner(L) )
print()
'''
print('O conjunto {x**2 - y, y**2} é uma base de Gröbner reduzida?')
print('Berger:', berger.is_grobner_reduzido(L))
print('Beasy: ', beasy.is_grobner_reduzido(L) )
print()
L_reduzido = beasy.grobner_reduzido(L)
print('Base de Gröbner reduzida de {x**2 - y, y**2}:', L_reduzido )
print('A base obtida é uma base de Gröbner reduzida?')
print('Resposta:', beasy.is_grobner_reduzido(L_reduzido) )
print()
p3 = beasy.criar_polinomio('x**4 * y')
print( p3 )
print('O polinômio x**4 * y pertence ao ideal gerado por {x**2 - y, y**2}?')
print('Resposta:', beasy.pertence_ao_ideal(p3, L) )
print()
p4, p5 = beasy.criar_polinomios('x - y', 'x + y')
p6, p7 = beasy.criar_polinomios('x', 'y')
I = [p4, p5]
J = [p6, p7]
print('Os ideais < x - y, x + y > e < x, y > são iguais?')
print('Resposta:', beasy.sao_iguais(I, J) )
'''