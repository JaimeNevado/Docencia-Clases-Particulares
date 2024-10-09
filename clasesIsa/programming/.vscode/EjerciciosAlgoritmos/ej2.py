a = 4
b = 2

while (a > 0):
	if a%2 == 0:
		b = b + a
	elif a < b:
		b = b - 1
	else:
		a = a - 1

print(b)
