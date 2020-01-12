#Python program for printing the Pascal's Triangle till the index
#the user inputs
def digits(n):
    '''To find the digits of a number'''
    z=n
    c=0
    d=0
    while z>0:
        c=z%10
        z=z//10
        d+=1
    return(d)

def fact(n):
    '''To find the factorial of a number'''
    if n==0:
        return(1)
    i=1
    z=n
    while i<n:
        z=z*i
        i+=1
    return(z)
r=0
t=int(input("Enter the index till where you want to print Pascal's triangle\n"))
for i in range(1,t+2):
    x=max(range(t+2))
    n=i-1
    y=x+x-1
    r=0
    if x%2==0:
        for j in range(1,y+1):
            if (x+1)-i<=j<=(x-1)+i:
                if i%2!=0:
                    if j%2==0:
                        ncr=fact(n)/(fact(n-r)*(fact(r)))
                        print('%d'%(ncr),end=' '*digits(y))
                        r+=1
                    else:
                        print(' '*digits(j),end=' '*digits(y))
                elif i%2==0:
                    if j%2!=0:
                        ncr=fact(n)/(fact(n-r)*(fact(r)))
                        print('%d'%(ncr),end=' '*digits(y))
                        r+=1
                    else:
                        print(' '*digits(j),end=' '*digits(y))
            else:
                print(' '*digits(j),end=' '*digits(y))
        print()
                
    elif x%2!=0:
        for j in range(1,y+1):
            if (x+1)-i<=j<=(x-1)+i:
                if i%2!=0:
                    if j%2!=0:
                        ncr=fact(n)/(fact(n-r)*(fact(r)))
                        print('%d'%(ncr),end=' '*digits(y))
                        r+=1
                    else:
                        print(' '*digits(j),end=' '*digits(y))
                elif i%2==0:
                    if j%2==0:
                        ncr=fact(n)/(fact(n-r)*(fact(r)))
                        print('%d'%(ncr),end=' '*digits(y))
                        r+=1
                    else:
                        print(' '*digits(j),end=' '*digits(y))
            else:
                print(' '*digits(j),end=' '*digits(y))
        
        print()
