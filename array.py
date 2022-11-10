from array import *
a = array('i', [])
k = int(input("Enter size of array: "))

for i in range(k):
    a.append(int(input('enter number :\t')))

for i in range (k):
    print(a[i], end =" ")

a.append(int(input('\nEnter element to append  ')))
print('Updated array is :')
for i in a:
    print(i, end =" ")