
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






# def add (x,y,z):
#     #z=x+y+z
#    return x,y,z
# p= int(input("Enter 1st number")) 
# q= int(input("Enter 2st number")) 
# r= int(input("Enter 3st number")) 

# a,b,c= add(y=r,x=p,z=q)
# print(a)
# print(b)
# print(c)




# Key-words

# def show (**kwargs):
#     print(kwargs)
#     for i,j in kwargs.items():
#         print(i,"=",j)

# show (name='Ashish',age=20,quali='ITI')






#   variable-congth argument


# x=10     # Global 
# def show():
#     global y
#     y=20   #  Local 
#     print(x)
#     print(y)    
# show()
# print(x)
# print(y)



x=10     # Global 
def show():
    global y 
    y=20
    x=50   #  Local 
    print(x)
    print(globals()['x'])    
show()
print(x)
print(y)