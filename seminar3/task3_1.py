# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов. [1, 2, 3, 1, 2, 4, 5] -> [1, 2]

my_list = [1, 2, 3, 1, 2, 4, 5, 2]
res = []

for num in my_list:
    while (my_list.count(num) > 1):
        if(res.count(num) < 1):
            res.append(num)
        my_list.remove(num)

print(res)