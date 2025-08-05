import buchberger as berg

buch = berg.Buchberger_Algorithms()
buch.set_variaveis('x y z')

### Teste 3: Reduções sucessivas
# O teste 2, mas agora testando a função de redução até que seja irredutível
p1, p2 = buch.criar_polinomios('x**2 - y', 'y**2')
L = [p1, p2]
p3 = buch.criar_polinomio('x**4 * y')


print('Para responder se x**4 * y pertence ao ideal gerado por {x**2 - y, y**2}, é preciso fazer reduções sucessivas:')
p4 = buch.reduz(p3, L)
print('Resultado da redução p3 módulo L:', p4)
print()
print('Segundo Buchberger I,', end=' ')
if p4.is_zero:
    print('x**4 * y pertence ao ideal gerado por {x**2 - y, y**2}.')
else:
    print('x**4 * y >não< pertence ao ideal gerado por {x**2 - y, y**2}.')

