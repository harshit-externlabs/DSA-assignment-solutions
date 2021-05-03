a=[]
print("Enter the no. of elements to be inserted:\n")
N=int(input())
a=[0]*N
print("Enter the elements:\n")
n=int(input())
a[0]=n
for i in range(1,N):
    n=int(input())
    while(i>0 and a[i-1]>n):
        a[i]=a[i-1]
        i=i-1
    a[i]=n
print("Elements in array sorted using insertion sort are:")
print(a)
