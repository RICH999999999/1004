def find_pairs(n):
    result = ""
#Перебираем первое число в паре от 1 до n-1
    for i in range(1, n):
#Перебираем второе число в паре от i до n-1
        for j in range(i+1, n):
            if n % (i + j) == 0:
                result += str(i) + str(j)
    return result
n = int(input("Введите число от 3 до 20: "))
print(f"Пароль для числа {n}: {find_pairs(n)}")
