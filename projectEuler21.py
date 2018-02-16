def d(a):
    
    divisor_sum = 0

    for i in range(1, a):

        if a%i == 0:
            divisor_sum += i
            
    return divisor_sum

total_sum = 0

#send numbers 1-10000 into d
#if it returns add it to total_sum


for a in range(1, 10001):
    b = d(a)
    if d(b) == a and a!=b:
        total_sum = total_sum + a
    

print (total_sum)
