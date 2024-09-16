def find_pairs(n):
    pairs = []
    for i in range(1, 21):
        for j in range(i, 21):
            if (i + j) % n == 0:
                pairs.append((i, j))
    return pairs

def generate_password(n):
    pairs = find_pairs(n)
    password = ''.join([str(i) + str(j) for i, j in pairs])
    return password

#Тест для числа от 3 до 20
for n in range(3, 21):
    print(f"Пароль для числа {n}: {generate_password(n)}")