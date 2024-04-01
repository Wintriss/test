f = open('17_13088.txt')
array = [int(x) for x in f]
n = len(array)
mx = 0
k = 0
mx_sm = 0
for i in array:
    if i > mx and i%100 == 17:
        mx = i
for i in range(n-3):
    a = array[i]
    b = array[i+1]
    c = array[i+2]
    sm = a+b+c
    if sm > mx:
        if a%5 == 0 or b%5 == 0 or c%5 == 0:
            n1 = len(str(a))
            n2 = len(str(b))
            n3 = len(str(c))
            if (n1 == 4 and n2 == 4) or (n1 == 4 and n3 == 4) or (n2 == 4 and n3 == 4):
                k += 1
                if sm > mx_sm:
                    mx_sm = sm
print(k,mx_sm)
