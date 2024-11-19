
#   POSITIONAL ARGUMENT 



# def add (x,y,z):
#     z=x+y+z
#   #  return z
# p= int(input("Enter 1st number")) 
# q= int(input("Enter 2st number")) 
# r= int(input("Enter 3st number")) 

# x= add(p,q,r)
# print(x)





# NONE

# def add (x,y,z):
#     z=x+y+z
#   #  return z
# p= int(input("Enter 1st number")) 
# q= int(input("Enter 2st number")) 
# r= int(input("Enter 3st number")) 

# x= add(p,q,r)
# print(x)



#  KEYWORD 

# def add (x,y,z):
#     z=x+y+z
#     return z
# p= int(input("Enter 1st number")) 
# q= int(input("Enter 2st number")) 
# r= int(input("Enter 3st number")) 

# x= add(y=r,x=p,z=q)
# print(x)






def add (x,y,z):
    #z=x+y+z
   return x,y,z
p= int(input("Enter 1st number")) 
q= int(input("Enter 2st number")) 
r= int(input("Enter 3st number")) 

a,b,c= add(y=r,x=p,z=q)
print(a)
print(b)
print(c)