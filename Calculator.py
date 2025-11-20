def oper_calc(num1, num2, operation):                                                                                   # Calculator operations function
    if operation == "+":
        print(num1 + num2)
    elif operation == "-":
        print(num1 - num2)
    elif operation == "*":                                                                                  
        print(num1 * num2)
    elif operation == "/":
            try:
                 print(num1 / num2)
            except ZeroDivisionError:
                print("На ноль делить нельзя")
    else:
        print("Неверная операция")

while True:                                                                                                               # Entering and checking numbers and operations
    while True:
        try:
            num1 = float(input("Введите первое число: "))
            break
        except ValueError:
            print ("Это не число, попробуйте еще раз")

    while True:                                                                                                                             
        try:
            num2 = float(input("Введите второе число: ")) 
            break
        except ValueError:
            print ("Это не число, попробуйте еще раз")

    operation = str(input("Выберите операцию: + (сложение), - (вычетание), * (умножение), / (деление): "))

    oper_calc(num1, num2, operation)                                                                                     # Function call                                                  

    while True:                                                                                                          # Loop. Checking if the user wants to continue working
        answ = input("Хотите продолжить? Y - да, N - нет: ").upper()
        if answ == 'Y' or answ == 'N':
            break
        else:
            print("Введите Y или N")

    if answ == 'Y':
         pass
    elif answ == 'N':
        break

        