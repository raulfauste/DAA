def sqrt(num,a):
    if num**2 - a < 0.000001:
        return num
    else:
        num = (num-(num**2 -a)/(2*num))
        return sqrt(num,a)

n = float(input())
sol = sqrt(n,n)
print('%.4f'%sol)



