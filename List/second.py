x = [1000,89,6,4,2,7,15,200,9,199]

maxn = x[0]
sec_max = x[1]

for i in range(1,len(x)):
    if x[i] > maxn:
        sec_max = maxn
        maxn = x[i]
    elif sec_max < x[i] < maxn :
        sec_max = x[i]
print(sec_max)

