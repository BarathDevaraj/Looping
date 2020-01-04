n=int(input('Enter the Number'))
lst=n%10
while(n>9):
    n=n//10
print('Sum of First and Last Digit is',n+lst)
