'''

# continue,   break,   pass

n=int(input("Enter no:"))
i=1
while i<=n:
    if i==5 or i==7:
       i=i+1
       continue
    else:
        print(i)
    i=i+1  



# jab do ya do se adhik word pass ya continue krna ho to ham or ka use krte hai  

n=int(input("Enter no:"))
i=1
while i<=n:
    if i==5 or i==7:
       i=i+1
       continue
    else:
        print(i)
    i=i+1  



# continue / pass  dono ka same use  

n=int(input("Enter no:"))
i=1
while i<=n:
    if i==5:
       i=i+1
       continue
    else:
        print(i)
    i=i+1  



# break 

n=int(input("Enter no:"))
i=1
while i<=n:
    if i==5:
       break
    else:
        print(i)
    i=i+1  



#  pass kisi ek word ko hatana ho to hum pass ka use karte hai.
    
n=int(input("Enter no:"))
i=1
while i<=n:
    if i==5:
       pass
    else:
        print(i)
    i=i+1  
'''            




while True:
    print ("1. add\n 2.sub\n 3.div\n  4. multi\n 5. off\n")
    n=int(input("Enter no: "))

    x=[1,2,3,4,5]
    if n in x:
        x=int(input("first value"))
        y=int(input("2nd value"))
        if n==1:
            print("adition=", x+y)
        elif n==2:
            print("subscrition=", x-y)
        elif n==3:
            print("division=", x*y)
        elif n==4:
            print("mulltiolication=", x/y)
    elif n==5:
        break
    else:
            print("rong number")