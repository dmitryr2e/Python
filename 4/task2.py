#даны N чисел
#создать список из уникальных чисел затем пройтись по основному циклу до тех пор пока не встретим каждуое число

n = int(input())

nums = list(map(int, input().split()))[:n]

#[:n] это срез он гарантирует что в список войдут строго n чисел

###uniq_nums = list(dict.fromkeys(nums))

###for i in range(n):
###    days = 1
###    cur_dress = 1
    
#возможно я усложняю код, так как платьев у нас строго 3 штуки (платье 1 платье 3 и платье 3).
#можно запустить цикл который проходит через сисок до тех пор пока не там не встретяся 1 2 и 3 либо пока список не кончится.
#заведем переменную cnt это будет счетчик дней. 

cnt = 0
is1 = False
is2 = False
is3 = False

for i in nums:
    if (is1 and is2 and is3):
        break
    cnt+=1
    if i ==1:
        is1 = True
    if i==2:
        is2 = True
    if i==3:
        is3 = True

print(cnt)

#альтернативное решение

n = int(input())
dresses = list(map(int, input().split()))

worn = set() #нвдетые платья (пустое множество set)
answer = n #заранее подготовленный ответ (последний день сезона)

for i in range(n):
    worn.add(dresses[i])
    if len(worn) == 3:
        answer = i + 1
        break
    
print(answer)

