#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#python program for simple calculator

#now here is function to add two numbers
try:
    def add(number1,number2):
        return number1+number2
    #now here is function to substract two numbers
    def sub(number1,number2):
        return number1-number2
    #now here is function to multiply two numbers
    def mul(number1,number2):
        return number1*number2
    #now here is function to devide two numbers
    def dev(number1,number2):
        return number1/number2
except:
    print('serious issues are here')
#here the the option which is going to be select by the user
print('please selcet the operation you wanted to perfrom\n'      '1. Add\n'      '2. substraction\n'      '3. multiply\n'      '4.devision\n')
#input is taking from user for options
selcet_number=int(input('enter the number for the above operation'))
number1,number2=int(input('enter the first number:-')),int(input('enter the second number:-'))
try:
    if selcet_number==1:
        print(number1,'+',number2,'=',add(number1,number2))
    elif selcet_number==2:
        print(number1,'-',number2,'=',sub(number1,number2))
    elif selcet_number==3:
        print(number1,'*',number2,'=',mul(number1,number2))
    elif selcet_number==4:
        print(number1,'/',number2,'=',dev(number1,number2))
    else:
        print('your option is wrong')
except:
    print('serious issues with calculation part:-')

