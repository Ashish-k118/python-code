# replace (old_value_new_value)


s="we are here to lern c++, it is a high level lang"

s1=s.replace("c++", "python")
s2=s.replace('a', 'b', 2)
s3=s.replace(s,"new")
print (s1)
print (s2)
print (s3)




# 2. split function 
# split() function.  -->  return list


s="we are here to lern c++, it is a high level lang"
s1=s.split()
print (s1)

s2=s.split("a")   # singal word split
print (s2)




# join()   -->return string

lis= ["Apple", "mango", "banana", "orange"]
lis1= ["Ashish"]
lis2=("Kushwaha")
s = " ,".join(lis) + " ," +".".join(lis1)+ "  "+"".join(lis2)
print (s)



# slice , split , join

s= "its now or never"
# print(s[::-1])
s1=s.split()
print (s1)
a=s1[0][::-1]
b=s1[1][::-1]
c=s1[2][::-1]
d=s1[3][::-1]
s1=[a,b,c,d]
print(s1)



# s1="sti.now.or.never"