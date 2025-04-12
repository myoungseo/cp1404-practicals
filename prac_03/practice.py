'''
Write a program to read a file and print ONLY the lines that start with a #
The user should enter the file name
'''
file_name = input("Enter file name: ")
in_file = open(file_name, 'r')
for line in in_file:
    if line.startswith('#'):
        print(line)
in_file.close()

s="\t python, Monty \n"
print(s)
print(s[1], '.', sep="")
print(len(s))
#print(s.strip(), '.', sep="")
#print(s.lstrip(), '.', sep="")
#print(s.strip().split(",")

'''
Rewrite the following to use with
name = input("Name: ")
out_file = open("name.txt", "w")
print(name, file = out_file)
out_file.close()
print("Done")
'''
name = input("Name: ")
with open("name.txt", "w") as out_file:
    print(name, file=out_file)
print("Done")

'''
Write a code that creates files from a list of strings.
Each file should be named with the value of the string with a .txt extension.
If the string is "Bob", create a file called "Bob.txt".
Write the string to the file.
'''
names = ["Alice", "Bob", "Charlie", "David"]  # Example list of strings
for name in names:
    with open(f"{name}.txt", "w") as file:
        file.write(name)
print("Done")

'''
Version 2:
Write the position in the list to the file, starting from 1
'''
names = input("Enter names separated by commas: ").split(",")

for i in range(len(names)):
    name = names[i].strip()
    with open(f"{name}.txt", "w") as file:
        file.write(f"{i+1}. {name}")

print("Files created successfully.")

'''
Write a code to read a file like this and print each data pair, like "Bob was
born in NZ"
Bob\n
NZ\n
Jane\n
Myanmar\n
Derek\n
Australia\n
'''
with open("data.txt", "r") as file:
    lines = file.readlines()

for i in range(0, len(lines), 2):
    name = lines[i].strip()
    country = lines[i+1].strip()
    print(f"{name} was born in {country}")

'''
complete this code
is_finished = False
while #TODO what's the condition?
    try: 
       result = int(input("Enter a valid integer: "))
       #TODO this line
    except #TODO ??? add the exception to catch:
        print("Please enter a valid integer")
print("Valid result is: ". result)
'''
is_finished = False
while not is_finished:  # 반복 조건: 유효한 정수를 입력할 때까지 반복
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True  # 유효한 정수를 입력하면 반복 종료
    except ValueError:  # 정수가 아닌 값을 입력하면 예외 처리
        print("Please enter a valid integer")

print("Valid result is:", result)

'''
What's wrong with the demo in video 1?
def load_number(filename):
   try: 
      infile = open(filename, "r")
      number = int(infile.read())
   except ValueError:
      print(f"Invalid contents in {filename}")
      number = 6
   except FileNotFoundError:
      print(f"{filename} not found")
      number = 4
   else:
      infile.close()
   return number
'''