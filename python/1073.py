n = int(input())
x = 0
while x < n:
    x = x + 1
    if x % 2 == 0:
        quadrado = x * x
        print ('{}^2 ='.format(x),quadrado)
