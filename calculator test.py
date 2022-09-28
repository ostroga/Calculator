while True:
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))
    operation = (input("Що робимо - ,+ ,* ,/:"))
    result = 0
    if operation == '+':
        result = a+b
    elif operation == "-":
        result = a-b
    elif operation == "*":
        result = a*b
    elif operation == "/":
        if b == 0:
            print ("Ділити на нуль не можна")
        else:
            result = a / b
    print(input(f"Дорівнює {result}:"))
