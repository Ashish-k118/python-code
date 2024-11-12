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
'''


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