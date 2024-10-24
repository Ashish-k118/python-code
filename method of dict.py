# method of dict

# Zip method --->  

key = ["Ashish", "Paawan", "Vikash", "Arun","Abhisekh"]
value = [23,24,21,22]
result= dict(zip(key,value))
print (result)


#  tuple zip method

key = ["Ashish", "Paawan", "Vikash", "Arun","Abhisekh"]
value = [23,24,21,22]
result= tuple(zip(key,value))
print (result)


# list zip method

key = ["Ashish", "Paawan", "Vikash", "Arun","Abhisekh"]
value = [23,24,21,22]
result= list(zip(key,value))
print (result)




#  Get function (key) ---> return value

data= {'Ashish': 23, 'Paawan': 24, 'Vikash': 21, 'Arun': 22}
a=data.get("Roshon")
# a=data['bhupendra']    Eror
print (a)



# set default ()
# 1) key available --> return existing value 
# 2) key not available --> key value pair add , return added value

data={'1': 2398, '2': 248, '3': 2109, '4': 2209}
data.setdefault('1',7899)   # return value
value=data.setdefault('12',7899)   # Update 
print (data,value)   # same ans
print (value)    # same ans 




# pop() , popitem()  , ---> return value
# Clear()  !

data={'1': 2398, '2': 248, '3': 2109, '4': 2209}
print (data)
value=data.pop('1') 
print (data)   # return deteal data
print (value)




# popitem

data={'1': 2398, '2': 248, '3': 2109, '4': 2209 , '5':{'11':3522, '12':3454, '44':4574}}
print (data)
value=data['5'] ['44']
print (data)
print (value)



# clear

data={'1': 2398, '2': 248, '3': 2109, '4': 2209}
print (data)
value=data.clear() 
print (data)
print (value)



#  Qustion And Ans  #
# kisi bhi data ko delet kar skte hai 

data={'1': 2398, '2': 248, '3': 2109, '4': 2209 , '5':{'11':3522, '12':3454, '44':4574}}
print (type(data['1']))
print(type(data))
print(type(data['5']))
data['5'].popitem()
print(data)
data.popitem()
