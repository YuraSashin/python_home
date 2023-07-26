# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к
# языку.

text = 'яблоко, Дерево, игла, дерево, игрушка, еще дерево, еще игрушка, потом еще одно дерево\
    и еще дерево, дерево, игла, мячик , Дерево, берёза тоже дерево, банан не дерево, в лесу растёт ёлка и это дерево!'

delete = ".,!?;:-[]()='"

max = 0

for i in delete:
    text = text.replace(i, "")
text = text.lower()
# print(text)

my_list = text.split()
# print(my_list)

for num in my_list:
    if(my_list.count(num) >= max):
        max = my_list.count(num)

for num in my_list:
    if(my_list.count(num) == max):
        print(num)
        break


