from random import randint
spisok = []
sum1 = 0
sum2 = 0
print("Вывод 15-и рандомных чисел")
for i in range(15):
    a = randint(-1000, 1000)
    print(a)
    spisok.append(a)
for i in range(15):
    if spisok[i] == 0:
        while spisok[i] == 0:
            a = randint(-1000, 1000)
    elif spisok[i] > 0:
        sum1 = sum1 + spisok[i]
    else:
        sum2 = sum2 + spisok[i]
print("Результат сложения положительных чисел", sum1)
print("Результат сложения отрицательных чисел", sum2)
