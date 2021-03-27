x = int(input())
y = int(input())
a = int(input())
b = int(input())


def calculateValue(x,y,a,b):
    
    return x**(a+b)/y**(a+b)
    

if x == 0 and y == 0:
    print("x and y can not be 0")
else:
    print(calculateValue(x,y,a,b))