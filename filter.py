'''
filter(function, iterable)

'''
#1
list1 = [5, 12, 17, 18, 24, 32]
def func1(x):
  if x < 18:
    return False
  else:
    return True
f1 = filter(func1, list1)
print(list(f1))
  
#2
f2=filter(lambda x: x%2!=0, [1,2,3,4])
print(list(f2))

#3
def func3(x):
  return x%3==0
f3=filter(lambda x: func3(x),[1,2,3,4,5,6,7,8,9])
print(list(f3))

