
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
    l1=0
    l2=0
    l3=0
    for i in s:
        if i.isalpha():
           l1=l1+1 
        elif i.isnumeric():
           l2=l2+1 
        elif i in ['%','^','&','*','(',')','?',':','[',']','@','_','!','#','$']  :
            l3=l3+1
    
    print("No of alphabetic character are ", l1)
    
    print("No of Numeric character are ", l2)
    
    print("No of special character are ", l3)
    
myfunc2('Naukri12345@@#')
