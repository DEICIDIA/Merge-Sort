import time
import random 

lst = random.sample(range(0,100000), 100000)
lst2 = lst.copy()

def split(lst):
	if len(lst) > 1:
		return merge_sub_lst(split(lst[len(lst)//2:]), split(lst[:len(lst)//2]))
	return lst

def merge_sub_lst(lst1, lst2):
	new_lst = []
	goal = len(lst1) + len(lst2)
	while(len(new_lst) != goal):
		if len(lst1) == 0:
			for nb in lst2:
				new_lst.append(nb)
			break
		if len(lst2) == 0:
			for nb in lst1:
				new_lst.append(nb)
			break
		if lst1[0] < lst2[0]:
			new_lst.append(lst1[0])
			lst1.pop(0)
		else:
			new_lst.append(lst2[0])
			lst2.pop(0)	
	return new_lst

a = time.time()
lst = split(lst)
b = time.time()

print("temps d'execution merge : ", b-a)

c = time.time()
lst2.sort()
d = time.time()

print("temps d'execution sorted : ", d-c)
