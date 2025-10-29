def toNBase(num, base):
	ans = ""
	while num:
		ans += "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[num % base]
		num //= base
	return ans[::-1]

def toDecBase(num, base):
	num = str(num)
	ans, lenNum = 0, len(num)
	for i in range(lenNum):
		ans += "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(num[i]) * base ** (lenNum - 1 - i)
	return ans
