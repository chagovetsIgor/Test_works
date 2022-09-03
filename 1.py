#напишите программу которая считает сумму цифр числа
a = input(f"введите число для просчета ")
summa = sum(map(int, str(a).replace(".", "")))
print(summa)
