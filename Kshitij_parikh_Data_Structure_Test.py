#1
def func1(my_dict):
    try:
        for i in my_dict.values():
            assert float(i)
        keys=list(my_dict.keys())
        keys.sort()
        sorted_dict={i:my_dict[i] for i in keys}
        list1=[(values,keys) for keys,values in sorted_dict.items()]
        print(list1)
    except:
        print('Invalid Input') 
        
func1({'c': 3, 'a': 1, 'd': 4, 'b': 2})



#2

def func2(data,sum):
    try:
        assert len(data)>2
        for i in range(len(data)):
            assert int(data[i])
        for i in range(len(data)):
            for j in range(i+1,len(data)):
                if data[i]+data[j]==sum:
                    yield (data[i],data[j])
    except:
        print('Length should be more than 2')  
        print('Data should only contain Integers')              
x=func2([1, 2, 3, 4, 5, 6, 7, 8, 9],10)
list2=[i for i in x]
print(list2)
