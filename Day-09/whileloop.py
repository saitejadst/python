num = int(input("Enter number: "))

while num != 0:
    print("You entered:", num)
    num = int(input("Enter number: "))

i = 0

while True:
    if i == 3:
        break
    print(i)
    i += 1

i = 0

while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

i = 0

while i < 3:
    print(i)
    i += 1
else:
    print("Loop finished")
