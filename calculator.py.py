A = int(input("Первое число"))
operation = input("Операция"))
B = int(input("Второе число"))
dalee = 'y':
while dalee == 'y':
    if operation == '+':
        print(A + B)
    elif operation == '-':
            print(A - B)
    elif operation == '*':
        print(A * B)
    elif operation == '/':
        print(A / B)
    else:
        print("Error")
    dalee = input("Введите 'y',чтобы продолжить, или любую клавишу, чтобы завершить")