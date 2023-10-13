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

#4
list4 = ['Sammy', 'Ashley', 'Jo', 'Olly', 'Jackie', 'Charlie']
f4=filter(lambda x: x[0].lower() in 'aeiou',list4)
print(list(f4))

#5
list5 = [11, False, 18, 21, "", 12, 34, 0, [], {}]
f5 = filter(None, list5)
print(list(f5))

#6
list6 = [
  {"name": "sammy", "species": "shark", "tank number": "11", "type": "fish"},
  {"name": "ashley", "species": "crab", "tank number": "25", "type": "shellfish"},
  {"name": "jo", "species": "guppy", "tank number": "18", "type": "fish"},
  {"name": "jackie", "species": "lobster", "tank number": "21", "type": "shellfish"},
  {"name": "charlie", "species": "clownfish", "tank number": "12", "type": "fish"},
  {"name": "olly", "species": "green turtle", "tank number": "34", "type": "turtle"}
]

def func6(list6,search_string):
  def iterator_func(x):  
    for i in x.values():
      if search_string in i:
        return True
    return False
  return filter(iterator_func,list6)

print(list(func6(list6,'s')))
