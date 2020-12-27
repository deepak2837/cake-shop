num = int(input("enter the value of n"))
j=[]
for i in range(0,num):
    k = int(input("enter ur numbers"))
    j.append(k)

l = []

for i in j:
    for a in range(0,i):
    
        def decimalToBinary(a):  
            l.append(format(a, 'b'))
        decimalToBinary(a+1)
        h =[]
        for d in l:
            h.append(int(d))
        print(sum(h))
# print(h)








    # def DecimalToBinary(i): 
    #     if int(i) > 1: 
    #         DecimalToBinary(i // 2) 
    #     print((i % 2), end = '')
    # DecimalToBinary(i)
# print(l)