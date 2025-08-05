import buchberger as berg

buch = berg.Buchberger_Algorithms()
buch.set_variaveis('x y z')
'''
### Teste 1: Exercícios básicos
p1, p2 = buch.criar_polinomios('x**2 - y', 'y**2')
L = [p1, p2]

print('Qual o S-Polinômio de x**2 - y e y**2 ?')
print('Resposta:', buch.S(p1, p2) )
print()
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
'''

### Teste 2: Funções auxiliares
# advindos de partes feitas à mão do exercício do Teste 1
p1, p2 = buch.criar_polinomios('x**2 - y', 'y**2')
L = [p1, p2]
p3 = buch.criar_polinomio('x**4 * y')


print('Para responder se x**4 * y pertence ao ideal gerado por {x**2 - y, y**2}, é preciso fazer uma redução de dois passos:')
p4 = buch.reduz_em_um_passo(p3, p1)
print('Resultado da redução p3 módulo p1:', p4)
if p4:
    p5 = buch.reduz_em_um_passo(p4, p2)
    print('Resultado da redução p4 módulo p2:', p5)
print('Resultado total das reduções:', p5)
print()

print('Ué. Está diferente do que foi feito nos exercícios... Mas foi engano humano. Cada redução a um passo é exatamente 1 passo de divisão, e na verdade, no exercício, foram três passos.')
print('Foi descoberta uma maneira mais rápida de calcular se o exercício, abandonando a divisão mais cedo. Interessante, porém fora do algorítmo. O certo são três passos:')

p4 = buch.reduz_em_um_passo(p3, p1)
print('Resultado da redução p3 módulo p1:', p4)
if p4:
    p5 = buch.reduz_em_um_passo(p4, p1)
    print('Resultado da redução p4 módulo p1:', p5)
    if p5:
        p6 = buch.reduz_em_um_passo(p5, p2)
        print('Resultado da redução p5 módulo p2:', p6)
print('Resultado total das reduções:', p6)
