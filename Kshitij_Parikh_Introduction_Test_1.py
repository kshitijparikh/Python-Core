
def myfunc1(s):
    list1=[]
    list2=[]
    k=''
    for i in s:
        if i.isalpha():
            list1.append(i)
        elif i.isnumeric():
            list2.append(int(i))    

    for i in range(len(list1)):
         k=k+list1[i]*list2[i]
    print('Final String is: ',k)
myfunc1('a3b4c2')


def myfunc2(s):
    list1=[]
    list2=[]
    list3=[]
    for i in s:
        if i.isalpha():
           list1.append(i) 
        elif i.isnumeric():
           list2.append(i) 
        elif i in ['%','^','&','*','(',')','?',':','[',']','@','_','!','#','$']  :
            list3.append(i)
    
    print("No of alphabetic character are ", len(list1))
    
    print("No of Numeric character are ", len(list2))
    
    print("No of special character are ", len(list3))
    
myfunc2('Naukri12345@@#')
