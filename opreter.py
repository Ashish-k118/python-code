
"""
print(23 % 4)
print (4-23)

#  1. .// floor division operator   ( // )
# ceiling value 

print (23/4)  # 5.75
print (23//4)  # 5
print(60//7)  # 8
print (60//6) # 10
print (4**5)  # base power
print (7**3)  # 343


#  2. comparision oparetor

print (23>=45)  # F
print (23>45)   # F
print (23!=45)  # T
print (23<=45)  # T
print (23==45)  # F


# 3. string comparision oparetor
# on the basis of ASCII  ( American Standrd Code The Information Interchange)

print ("apple" > "banana")  # F
print ("appleeeeee" > "banana")  # F
print ("apple" > "apple")  # F
print ("apple"=="apple")  # T
print ("OranGe" < "orange") # T
print ("oranGe" < "orange") # T
print ("ABCD" < "ABC")  # F
print ("cat" < "camel")  # F
"""

# logical operator
#====================
# And      Or      Not

"""
print (True and True)    # T
print (3>2 and 45<3)     # F
print (3>2 or 45<3)      # T
print (not (24>56))      # T
print (not(3>2) or 45<3) # F
print (not(3>2 and 45<3)) # T
"""

# member ship operator
# =====================

# in    ,   not in

"""
string1= "apple is good 455 health"
print ("is" in string1)   # T
print ("apple  is" in string1)   # F
print ('4' in string1) # T
print ("455" in string1)  # T
print ("health " not in string1)  # F
"""

# Identity operator
# is , is not

# is operator gives true when we test for same object
# otherwise false.



# variables and datatype
# ====================== 
# variable/ refrence:   variable is a refrence to a memory locetion where or object (resaits).

num = 90
num1 = 101
num = 90
print (id(num))
print (id(num1))
print (id(num))