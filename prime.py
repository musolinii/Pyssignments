prime = []
for i in range (0,101):

    count = 0

    for j in range(1,i):
        
        if i % j == 0:
            count += 1
            
    if count == 1 :
        prime.append(i)

print(prime)