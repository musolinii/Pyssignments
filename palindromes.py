file = open("words.txt", "r")

check = ""
revword = []
normal = []

palindrome_count = 0
for word in file:
    check = word.strip().lower()
    pointer = len(check) - 1 

    for i in range (len(check)):
        revword.append(check[pointer])
        pointer = pointer - 1
        normal.append(check[i])
        
    

    if(normal == revword):
        palindrome_count += 1
    
    revword = []
    check = ""
    normal = []

print(palindrome_count)