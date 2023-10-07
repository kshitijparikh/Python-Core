thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

# get()
print(thisdict.get('brand'))

# pop()
print(thisdict.pop('colors'), thisdict)

#copy()
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
thisdict2=thisdict.copy()

#values()
print(thisdict.values())

#keys
print(thisdict.keys())

#items
print(thisdict.items())

#update()
thisdict.update({'electric':True})
print(thisdict)

#fromkeys()
x=[1,2,3]
y='a'
print(thisdict.fromkeys(x,y))

#popitem
print(thisdict.popitem())

#setdefault()
print(thisdict.setdefault('brand'))
