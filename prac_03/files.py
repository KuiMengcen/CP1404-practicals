# 1
out_file = open("name.txt", "w")
name = input("What is your name? ")
print(name, file=out_file)
out_file.close()

# 2
file = open("name.txt", "r")
name = file.read().strip()
file.close()
print("Your name is", name)

# 3
total = 0
FILENAME = "numbers.txt"
in_file = open(FILENAME)
for i in range(0, 2):
    number = in_file.readline()
    total = total + int(number)
print(total)
in_file.close()

# 4
total = 0
file = open("numbers.txt", "r")
for line in file:
    number = int(line)
    total += number
file.close()
print(total)