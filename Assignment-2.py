
n = int(input())

def seriesValue(n):
    
    if n%2 == 0:
        return n**2-1
    else:
        return n**2+1
print(seriesValue(n))