# Strings :

"""
    - In python, strings are arrays of bytes representing 
      Unicode characters.
    - Whatever we write between two triple, double or single quotes
      while assigning a value to variable is considered as string.

      eg. x = "Hello world"

    - Multiline string :
        - by three quotes we can assign a multiline string to a variable.
        - it helps to maintain linebreaks positions of actual code.
"""

# Accessing characters in python :

"""
    - using indexing method we can access individual character of string.
    - indexing allows negative address references too.
       for eg. -1 refer to last character of string.
               -2 refer to second last character of string.
    - while accessing an index out of range will cause an IndexError.
    - Only integers are allowed to be passed as an index other types
      will cause TypeError.

        * indexing :

        x = "hello"
        print(x[0])
        o/p : h

        0  1  2  3  4 
        h  e  l  l  0
       -5 -4 -3 -2 -1

"""

# String length :

"""
    len() function will provide the length of the string 
    including number of spaces.

"""

# String slicing :
# Remember one thing : In string slicing the 
# end slicing indexed value will be excluded.

"""
    - to access a range of characters in the string,
      the method of slicing is used.
    - slicing in a string is done by using a slicing operator
      (colon ":")  
    - let's get the character from position 2 to 8
        eg.
            str1 = "lets do string slicing"
            print(str1[2:9])
            o/p : ts do st

            * in this from 2nd position to 8th position
              values will be printed.


    => slice from the start :
        - empty start index will start from 0 index
            print(str1[:5])
            >> lets 

    => slice to the end :
        - empty end index will consider range till the end
            print(str1[2::])  
            >> ts do string slicing
            print(str1[2:]) 
            >> ts do string slicing
    => negative indexing :
        - use negative indexes to start the slice from the end
            print(str1[-3:-1])
            >> ing

    => reverse string :
        - there is no method for reversing a string in python but 
          we can reverse by...

          print(str1[::-1])

    => jump characters :
        - print(str1[0:10:3]) 
          >>lsot
"""

# string concatenation :

"""
         + operator :

         var1 = "hello"
         var2 = " world"
         var3 = var1 + var2
         print(var3)
         >> hello world

   
        .join() method :

           - The join() method is string method and returns 
            a string in which the elements of sequence have been
            joined by str seperator.


            var1 = "hello"
            var2 = "world"
            print("".join([var1, var2]))
            >> hello world

        % operator :
            - We can use % operator for string formatting, 
              it can also be used for string concatenation.
            - It's useful when we want to concatenate string 
              and perform simple formatting.

            var1 = "hello"
            var2 = "world"
            print("%s %s" % (var1,var2))   
            >> hello world

        format ()function :
            - str.fromat() 

              var1 = "hello"
              var2 = "world"  
              print("{} {}".format(var1,var2))
              >>hello world

        , (comma) :
            var1 = "hello"
            var2 = "world"     
            print(var1,var2)
            >> hello world         


"""

# string formatting :
 
"""
    print("you are most {}!".format("welcome"))
    >> you are most welcome!

    print("{2} {1} {0}".format("directions.","Read","the"))
    >> Read the directions

    print("a : {a}, b : {b}, c : {c}").format(a=1,b="two",c=12.5)
    >> a : 1, b : two, c : 12.5

    print("{x} move ahead, {x} work hard, {x} succeed!".format(x="you"))
    >> you move ahead, you work hard, you succeed!


"""

# escape characters :
     
"""
    - \ escape characters are used to print illegal characters

    eg. str1 = "\"Hello\"" 
    anything just after \ will be ignored

    - \\ for backslash
    - \n for new line
    - \t for tab
    - \b for backspace

"""

# methods of string


"""
    => capitalize() : converts the first character to uppercase.

            str1 = "Methods of string will be applied on this string"
            print(str1.capitalize())
            >> Methods of string will be applied on this string

    => casefold() : converts all strings to lower case   

            str1 = "METHODS OF STRING WILL BE APPLIED ON THIS STRING"
            print(str1.casefold()) 
            >> methods of string will be applied on this string 

    => center() : returns centered string :

               str1 = "METHODS"
               print(str1.center(10))
               >>          Methods

    => count() : returns number of times a specified value 
                 occured in a string   

               str1 = "you can learn, you can teach, you can watch"
               print(str1.count("you"))     
               >>3   

    => encode() : Return an encoded version of the string.   

                str1 = "you can learn, you can teach"
                print(str1.encode()) 
                >>b'you can learn, you can teach'

    => endswith() : Return true if the string ends with the specified value  

                str1 = "you can learn, you can teach"
                print(str1.endswith("ch"))  
                >>True

    => expandtabs() : Sets the tab size for the string

                str1 = "H\te\tl\tl\to"
                print(str1.expandtabs(3))
                >>H  e  l  l  o


    => find() : Search the string for a specified value and return
                return the position of where it was found. 

                str1 = "hello this is find method"
                print(str1.find("is"))   
                >>8
    => format() : Formats the string for printing it to console.

    => format_map() : Formats specified values in a string using a dictionary

    => index() : searches the string for a specified value 
                 and returns the position of where it was found.

                    str1 = "hello this is find method"
                    print(str1.index("is"))
                    >>8

    => isalnum() : returns true if all characters in the string
                   are alphanumeric.


                   str1 = "hello this is find method"
                   print(str1.isalnum())
                   >>False 

    => isdecimal() ;
    => isalpha() :
    => isdigit() :
    => isidentifier() :
    => islower() :
    => isnumeric() :
    => isprintable() :
    => isspace() :
    => istitle() :
    => isupper() :
    => join() :
    => Ijust() :
    => lower() :
    => Istrip() :
    => maketrans() :
    => partition() :
    => replace() :
    => rfind() :
    => rindex() :
    => rjust() :
    => rpartition() :
    => rsplit() :
    => rstrip() :
    => splitlines() :
    => startswith() :
    => strip() :
    => swapcase() :
    => title() :
    => translate() :
    => upper() :
    => zfill() :                   

"""

str1 = "hello this is find method"
print(str1.isalnum())