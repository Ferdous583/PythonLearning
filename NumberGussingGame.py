# Small fun game.
# Number gassing.


print('\n"Gassing a number between 0 to 30. And you have only 5 chances."')
num=17

def f_name():
    if num==x:
        print('You have win.')
    elif x<0 or x>30:
        print('Wrong Input!')
    elif num<x:
        print("Wrong! try to guess lesser number." )
    elif num>x:
        print("Wrong! try to guess greater number.")


for i in range(1,6):
    x = int(input('\nEnter a number: '))
    print(i,':',' ',end='')
    f_name()
    if num==x:
        break
    print('You have',5-i,'time left.')
