#    Higher order function  //   22/11/2024

#    map , filter, reduse, lambda, decarat, ganreter :



#   [  MAP  ]

'''
Syntex:-

collection citerater
def fun_name():
    return
map(fun_name, callection)

'''

#  MAP 

# mylist=[10,20,30,40,50]
# def dec(x):
#     return x-5
# x=map (dec, mylist)
# print(tuple(x))


# mylist=[10,20,30,40,50]
# def dec(x):
#     return x +5
# x=map (dec, mylist)
# print(sum(x))



#  Fillter :-

# mytupple=(70,75,80,60,50,40,30)
# def qrater_60(x):
#     if x>60:
#         return(x)
# x=list(filter(qrater_60,mytupple))
# print(x)


# Even number

# mytupple=(70,75,80,60,50,40,30)
# def qrater_60(x):
#     if x%2==20:
#         return(x)
# x=list(filter(qrater_60,mytupple))
# print(x)


#  ADD Number

# mytupple=(70,75,80,60,50,40,30)
# def qrater_60(x):
#     if x%2 !=20:
#         return(x)
# x=list(filter(qrater_60,mytupple))
# print(x)



# Object Addresh

# mytupple=(70,75,80,60,50,40,30)
# def qrater_60(x):
#     if x>60:
#         return(x)
# x=(filter(qrater_60,mytupple))
# print(x)




#   REDUCE :-

# from functools import  reduce
# import functools
# mytuple=(10,20,30,40,50)
# def maxdigit(x,y):
#     if x>y:
#         return(x)
#     else:
#         return(y)
# x=functools.reduce(maxdigit,mytuple)
# print(x)


from functools import  reduce
#import functools
mytuple=(10,20,30,40,50)
def maxdigit(x,y):
    if x>y:
        return(x)
    else:
        return(y)
x=reduce(maxdigit,mytuple)
print(x)