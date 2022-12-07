operant = int(input("1 - плюс, 2 - минус, 3 - умножить, 4 разделить \nВведите действие: "))
if operant >= 1 and operant <= 4:
	a = int(input("Введите 1 число: "))
	b = int(input("Введите 2 число: "))
	if operant == 1: print(a + b)
	elif operant == 2: print(a - b)
	elif operant == 3: print(a * b)
	else: print(a / b)
else: print('ошибка ввода операции')
