n=int(input('Enter the Number'))
print('Last Digit is',n%10)
while(n>9):
    n=n//10
print('First Digit is',n)
