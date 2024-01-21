def  main():
    try:
        number = int(input('Enter a number: '))
    except ValueError: 
        print('It is not a number, dummy.\n\n\n\n')

    buzz(number)

def buzz(num):
    if num == 7 or (num % 7) == 0:
        print('BUZZZZZZ')
    else:
        print(num)

if __name__ == '__main__':
    while (True):
        main()