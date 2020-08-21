#Create a new file called “question_2.py”.
#In the file, write a function called
#“to_camel_case(text)” that takes “text” as input/parameter and returns the camel case version of that text. For camel case every word starts with a capital letter, all other letters is lower case and all spaces are removed.
#Examples of what your “to_camel_case” function should return for different inputs:
#to_camel_case (‘hello world’) -> ‘HelloWorld’
#to_camel_case (‘My sRriNg’) -> ‘MyString’
#to_camel_case (‘tHis Is A tesT string’) -> ‘ThisIsATestString’


text = 'hello world'

def to_camel_case(text):
    text1 = '' 
    text1 += text[0].upper() 
    for i in range(1, len(text)):
        if (text[i] == ' '):
            text1 += text[i +1].upper()
            i += 1
        elif(text[i-1] != ' '):
            text1 += text[i]
    print(text1)
        
    
    