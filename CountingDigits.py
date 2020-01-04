n=int(input('Enter the Number'))
count=0
while(n>9):
    count+=1
    n=n//10
print('Number of Digits is 'count+1)
