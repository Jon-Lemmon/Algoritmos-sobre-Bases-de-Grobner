import buchberger as berg

buch = berg.Buchberger_Algorithms()
buch.set_variaveis('x y z')

### Teste 2: Redução a um passo
# advindos de partes feitas à mão do mesmo exercício do Teste 1
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
    print()
    if p5:
        p6 = buch.reduz_em_um_passo(p5, p2)
        print('Resultado da redução p5 módulo p2:', p6)
        print()
print('Resultado total das reduções:', p6)
