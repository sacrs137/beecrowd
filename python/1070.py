x = int(input())
count = 0
while count < 6 :
    if x % 2 != 0:
        count = count + 1
        print(x)
    x = x + 1
