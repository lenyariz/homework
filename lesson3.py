#Простой вариант
pair = input("Введите товары: ").split(",")

product1, count1 = pair[0].split(":")
product2, count2 = pair[1].split(":")
product3, count3 = pair[2].split(":")
product4, count4 = pair[3].split(":")

dict1 = {product1: 0, product2: 0, product3: 0, product4: 0}
dict1[product1] += int(count1)
dict1[product2] += int(count2)
dict1[product3] += int(count3)
dict1[product4] += int(count4)

print("Простой вариант:", dict1)


#Сложный вариант
dict1 = {}
dict2 = {dict1.update({value.split(":")[0]: int(value.split(":")[1]) + dict1.get(value.split(":")[0], 0)}) for value in pair}
print("Сложный вариант:", dict1)

#Доп. задание
list_str = list(sorted([f"{key} - {value}" for key, value in dict1.items()]))
print("Отсортированный список:", list_str)