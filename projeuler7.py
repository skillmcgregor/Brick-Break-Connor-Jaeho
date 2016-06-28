num = 21

if (num > 1):
	for i in range(2,num):
		if (num%i) == 0:
			print(num, "nope")
			print(i, "times", num//i, "is", num)
			break
	else:
		print(num, "yep")
else:
	print(num, "nope")
