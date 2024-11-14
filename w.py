'''
n=int(input("Enter no: "))
i=1
sum=0
while i<=n:
    if i%2==0:
      sum=sum+i
      if i<=(n-2):
         print(i,end='+')
      else:
         print(i,end='=')
    i=i+1 
print(sum)



# Even number

n=int(input("Enter no: "))
#n=0
i=1
while i<=n:
    if i<n:
        print(2*i,end=',')
    else:
        print(2*i)
    i=i+1




#   odd number

n=int(input("Enter no: "))
#n=0
i=1
while i<=n:
    if i<n:
        print(2*i-1,end=',')
    else:
        print(2*i-1)
    i=i+1



    
# Range to use odd number: 

n=int(input("Enter eny number: "))
#sum=0
for i in range(1,n+1,2):
   # sum=sum+i
    if i<=(n-2):
        print(i,end=',')
    else:
        print(i)
# print(sum)



# Reang to Even number

n=int(input("Enter no: "))
for i in range(1,n+1):
    if i<(n-1):
        print(2*i-1,end=',')
    else:
        print(2*i-1)
'''


#  for loop use t string number:  

n=input("Enter String number: ")
v=0
c=0
for i in n:
    x=['a','e','i','o','u','A','E','I','O','U']
    if i in x:
        v=v+1
    else:
        c=c+1
print(v)
print(c)