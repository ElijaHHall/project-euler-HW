# 1. # num = [3,5]
# max = 1000

# result = 0
# for num in num:
# 	for i in range(1,1000):
# 		if num*i < max:
# 			result += num*i
# print(result)

# result = 0
# for i in range(0,1000):
# 	if i%3 == 0 or i%5 == 0:
# 		result += i

# print(result)


def SubFib(startNumber, endNumber):
	for cur in SubFib():
		if cur > endNumber: return
		if cur >= startNumber:
			yield cur

for i in SubFib(10, 200):
	print(i)