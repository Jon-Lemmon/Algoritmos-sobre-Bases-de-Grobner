import buchbeasy as beasy

buch = beasy.Buchberger_Algorithms()
buch.set_variaveis('x y z')

### Teste 1: Exercícios básicos
# Testando os resultados de buchbeasy.py, observando se eles batem com os obtidos à mão
p1, p2 = buch.criar_polinomios('x**2 - y', 'y**2')
L = [p1, p2]

print('O conjunto {x**2 - y, y**2} é uma base de Gröbner?')
print('Resposta:', buch.is_grobner(L) )
print()
print('O conjunto {x**2 - y, y**2} é uma base de Gröbner reduzida?')
print('Resposta:', buch.is_grobner_reduzido(L) )
print()
L_reduzido = buch.grobner_reduzido(L)
print('Base de Gröbner reduzida de {x**2 - y, y**2}:', L_reduzido )
print('A base obtida é uma base de Gröbner reduzida?')
print('Resposta:', buch.is_grobner_reduzido(L_reduzido) )
print()
p3 = buch.criar_polinomio('x**4 * y')
print( p3 )
print('O polinômio x**4 * y pertence ao ideal gerado por {x**2 - y, y**2}?')
print('Resposta:', buch.pertence_ao_ideal(p3, L) )
print()
p4, p5 = buch.criar_polinomios('x - y', 'x + y')
p6, p7 = buch.criar_polinomios('x', 'y')
I = [p4, p5]
J = [p6, p7]
print('Os ideais < x - y, x + y > e < x, y > são iguais?')
print('Resposta:', buch.sao_iguais(I, J) )