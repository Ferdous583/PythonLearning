a=int(input('a = '))
b=int(input('b = '))
c=int(input('c = '))
if a==b and a==c:
    print('\na = b = c')
elif a>b and a>c:

    if b > c:
        print('\na > b > c')
    elif c > b:
        print('\na > c > b')
elif b>a and b>c:

    if a > c:
        print('\nb > a > c')
    elif c > a:
        print('\nb > c > a')
elif c>a and c>b:

    if b > a:
        print('\nc > b > a')
    elif a > b:
        print('\nc > a > b')