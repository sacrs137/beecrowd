
x = input()
y = input()
z = input()
resultado = 'nada'
if ((x == 'vertebrado')) and ((y == 'ave')) and ((z == 'carnivoro')):
    resultado = 'aguia'
    print(resultado)
elif ((x == 'vertebrado')) and ((y == 'ave')) and ((z == 'onivoro')):
    resultado = 'pomba'
    print(resultado)
elif ((x == 'vertebrado')) and ((y == 'mamifero')) and ((z == 'onivoro')):
    resultado = 'homem'
    print(resultado)
elif ((x == 'vertebrado')) and ((y == 'mamifero')) and ((z == 'herbivoro')):
    resultado = 'vaca'
    print(resultado)
elif ((x == 'invertebrado')) and ((y == 'inseto')) and ((z == 'hematofago')):
    resultado = 'pulga'
    print(resultado)
elif ((x == 'invertebrado')) and ((y == 'inseto')) and ((z == 'herbivoro')):
    resultado = 'lagarta'
    print(resultado)
elif ((x == 'invertebrado')) and ((y == 'anelideo')) and ((z == 'hematofago')):
    resultado = 'sanguessuga'
    print(resultado)
elif ((x == 'invertebrado')) and ((y == 'anelideo')) and ((z == 'onivoro')):
    resultado = 'minhoca'
    print(resultado)
else:
    print('erro')
