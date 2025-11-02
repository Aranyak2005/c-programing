a=int(input('Enter a Number'))
sum=0
temp=a
while temp>0:
 c=temp%10
 sum+=c**3
 temp=temp//10

if a==sum:
    print('Armstrong Number')
else:
      print('Not Armstrong Number')  