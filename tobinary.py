def to_Binary(n):
	list = []

	while n>0:
		list.append(str(n%2))
		n = int(n/2)
	print(reversed(list))	    	
	print("".join(list))
#to_Binary(5)    
list1=[]
list2=[]
T = int(input('enter'))
print(T)
'''while T>0:
    N = int(input())
    while N>0:
        c = int(input())
        list1.append(c)
        N=N-1
    for i in range(0,N):
        list2.append(list1[list1[i]]) 
    print(list2)
        '''
    
    
