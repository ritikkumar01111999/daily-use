#program for the checking the value is plindrome or not
def cal(i):
    j=i[::-1]
    
#condiiton to check for the palindrome
    if i==j:
        print('the value of the string is palindrome ')
    else:
        print('the value is not a plindrome',len(j)//2)


i=input('enter the number string:-')
cal(i)
