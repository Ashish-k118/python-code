
number= (12,99)+ (78,90)
number = number + (89, 90)
print (number) #(12,99,78,90,89,90)




lis = [["ajay", "Ashish"],(45,67)]
# lis[0][1]=90------------> Erore(tuple)
lis.pop()
print (lis)



t = (35,67,[3,4,5555])
print(t)
t[2][1]=909090
print (t)
t[2].append(6767)
print(t)




lis = [["ajay", "Ashish"],(45,[67,56])]
lis[1][1][0]=787878
print (lis)


# len(), max(), min(), sum(), index(), count()
# sorted () ---> return sorted list


t= (9,8,7,6,6,5,4)
# a=t.count(6)
# a=t.index(5)
a=sorted(t)
print (a)



t = (23)
print (type(t))  # int

t2 = (23,)
print (type(t2)) # tuple

t3 = ("abcd")
print (type(t2)) # string

t4 = ("abcd",)
print (type(t4))  # tuple 

t5 = 23,56,75   # function use
print (type(t5))  # tuple 



# Empty tuple.

t = ()

t1 = tuple()
print(t,t1)  # tuple


record = ("Ashish", 101, 21, 7651978810)
record = list(record)
record[3],record[0]=9569274030, "Ashish Kushwaha"  # multpul assinment
record[1]=99  # singal asssinment 
print(record)
record = tuple (record)
print (record)

