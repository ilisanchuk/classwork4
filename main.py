n = int(input('Введите число: '))

s1 = []

for i in range(1, n + 1):
    for k in range(i):
        s1.append(i)
result = ' '.join(map(str, s1[:n]))
print(result)