def remove_consecutive_sequences(c):
    i = 0
    while i < len(c) - 2:
        if c[i] == c[i+1] - 1 and c[i] == c[i+2] - 2:
             del c[i:i+3]
        else:
            i += 1
    print("List after removing consecutive sequences of 3 integers:", c)
b = int(input("Enter the number of integers: "))
nums = []
for a in range(b):
            num = int(input("Enter an integer: "))
            nums.append(num)
        
print("Original List:", nums)
remove_consecutive_sequences(nums)
        



    
