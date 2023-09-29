#Global Scope
#1
x = 300
def myfunc():
  print(x)
myfunc()
print(x)

#2
def myfunc():
  global x
  x = 300
myfunc()
print(x)


#Local Scope
def myfunc():
  x = 300
  print(x)

myfunc()

