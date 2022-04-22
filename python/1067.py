y = 0
x = int(input())
while y != x:
    y = y + 1
    if y > x:
        break
    elif y % 2 != 0:
        print(y)
