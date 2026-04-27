my_list = [1, 2, 3, 'apple', 'banana']
print(my_list)

print(my_list[0])   # first element #list indexing
print(my_list[3])   # 'apple'

print(len(my_list))

my_list.append(4)
print(my_list)

my_list.remove('apple')
print(my_list)

subset = my_list[1:4]
print(subset)

new_list = my_list + [5, 6]
print(new_list)

numbers = [5, 2, 9, 1]
numbers.sort()
print(numbers)

print('banana' in my_list)
print('apple' in my_list)