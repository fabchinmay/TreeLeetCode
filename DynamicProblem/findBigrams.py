test_list = ['Have free hours and love children? Drive kids to school, soccer practice and other activities']
for i in test_list:
	#print(i)
	for j, x in enumerate(i.split()):
		#print(j,x,len(i.split()))
		if j < len(i.split()) - 1:
			print([x, i.split()[j + 1]])

res = [[x, i.split()[j + 1]] for i in test_list
       for j, x in enumerate(i.split()) if j < len(i.split()) - 1]

print(res)