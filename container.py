# set : 

#   set is a container in which we contain multiple data , but duplicatio is not allowed,
# and it is an unordered data type,
# where  our main concern is data ,  but not any order releted to it , then ewe use set.



s1={1,2,3,3,4,9,11,17}
s2={4,5,9,17,89}
s3={"a","b",1,2,3,88}
# r=s1.union(s2,s3)
r=s1|s2|s3
print (r)
# r=s1.intersection(s2,s3)
r= s1 & s2 & s3
print (r)
# r=s1.difference(s2)
r= s2-s1
# r= s1-s2
print (r)



# set difference

s1 = {'a','a','b','f','y','t'}
s2 = {'b','y', '1','6','7'}
r= s1-s2
print (r)
r= s2-s1
print (r)


#  union vs update

s1={1,2,3,3,4,9,11,17}
s2={33,55}

# r= s1=s2    # Erorr
s1.update(s2)
print (s1)



# ADD

s1={1,2,3,3,4,9,(4,5,6),11,17}
s1.add((2,4,5,6))    # koi sa bhi word tupple me add ho jayega
# s1.update((2, 89, 76)) # same word add  nhi hoga 
print (s1)



