N = int(input('Введите число от 1 до 10 000:'))
N1 = []
if N < 1 or N > 10000:
    print("Не правильно!")
else:
    for i in range(N):
       a = int(input('Введите число по модулю не более 10е5:'))
       if a > 10e5:
           print("Не правильно!")
       else:
            N1.append(a)
    N1.reverse()
    print(N1)
