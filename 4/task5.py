kozir = input()

masti = ["Spades", "Hearts", "Diamonds", "Clubs"]
dostoinstva = ["6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

nums = {}

n = int(input())

for i in range(n):
    first = input().split()
    second = input().split()
    
    id1 = dostoinstva.index(first[0])
    id2 = dostoinstva.index(second[0])
        
    if first[1] == second[1]:
        if id1 < id2:
            nums[i] = 1
        else:
            nums[i] = 0
        
    elif second[1] == kozir:
            nums[i] = 1
    
    else:
        nums[i] = 0

print(*nums.values())