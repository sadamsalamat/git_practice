'''

Interview Questions
Sam Alsalamat @ sadamsalamat@gmail.com

'''

#Two Sum
#Takes a list of numbers and return a list with all the pairs that sums up to a given target

def tow_sum(nums, target):

	lst = []
	d_target = {i:None for i in nums}
	for num in nums:
		x = target - num
		if x in d:
			lst.append([num, x])
			del dct[num]
	return lst

nums = [5, 9, 2, 7, 8, 1, 10, 12, -1]
print(tow_sum(nums, 9))


