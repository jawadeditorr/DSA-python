#lambda
add=lambda a,b:a+b
print(add(45,89))

#filter - applies a function to all items in a list amd filters the value for true condition
arr = [10,59,24,64,26,73,75]
even = filter(lambda arr:arr%2==0, arr)
print(list(even))

#map - applies a function to all items in a list
print(list(map(lambda x:x**2,arr)))

num1 = [3,4,5]
num2 = [6,7,8]
add_list = list(map(lambda x,y:x+y,num1,num2))
print(add_list)

"""type casting using map"""
str_num=['1','3','5']
print(str_num[0]+str_num[2])
int_num=list(map(int,str_num))
print(int_num[0]+int_num[2])