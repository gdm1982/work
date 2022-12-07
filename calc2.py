operant = int(input("1 - плюс, 2 - минус, 3 - умножить, 4 разделить \nВведите действие: "))
if operant >= 1 and operant <= 4:
	nums = int(input("Сколько будет чисел?: "))
	num1 = int(input(f"Введите 1 число: "))
	for cycle in range(2, nums+1):
		num = int(input(f"Введите {cycle} число: "))
		if operant == 1: num1 += num
		elif operant == 2: num1 -= num
		elif operant == 3: num1 *= num
		else: num1 /= num
	print(num1)
else: print('ошибка ввода операции')
