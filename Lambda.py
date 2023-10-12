'''
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.


'''



#1 
x=lambda a,b:a+b
print(x(3,4))

#2
def func2(x):
    print('First Function')
    return lambda a:x*a 
print(func2(3)(4))

#3
dict3={'b':1,'a':2,'c':0}
print(sorted(dict3, key=lambda x: x[0]))

#4
sorted_dict_items=sorted(list(dict3.items()),key=lambda x: x[1])
print(sorted_dict_items)

#5
name_list = ['Zen Jack', 'Luigi Austin', 'Ben Benson', 'John Ann']
name_list.sort(key=lambda x:x.split()[1])
print(name_list)


#6
x="some kind of a useless lambda"
(lambda x : print(x))(x)

#7 
list7=[(lambda x:x*x)(i) for i in [1,2,3,4] if i%2!=0]
print(list7)