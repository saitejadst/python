my_tuple = (1, 2, 'apple', 'banana')
print(my_tuple)

print(my_tuple[0])
print(my_tuple[2])

print(len(my_tuple))

coordinates = (3, 4)
x, y = coordinates

print(x)
print(y)

new_tuple = my_tuple + (3.14, 'cherry')
print(new_tuple)

print('apple' in my_tuple)
print('orange' in my_tuple)

def get_coordinates():
    return (3, 4)

x, y = get_coordinates()

print(x)
print(y)