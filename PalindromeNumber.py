n=int(input('Enter the number '))
n1=n
rev=0
while(n>0):
    rev=rev*10+n%10
    n=n//10
print('Reverse of Number is',rev)
if n1==rev:
    print('Palindrome Number')
else:
    print('Not a Palindrome Number')
