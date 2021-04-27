file = open('new_test_file.txt', 'w', encoding='utf-8')
file.write('This is a test file!')
file.close()

names = ['Terry', 'June', 'Kevin', 'Julie']
name_file = open('names.txt', 'w', encoding='utf-8')
for name in names:
    name_file.write(name + '\n')
name_file.close()

names = ['Terry\n', 'June\n', 'Kevin\n', 'Julie\n']
name_file = open('names.txt', 'w', encoding='utf-8')
name_file.writelines(names)
name_file.close()

# append on a file
# if not exist, make a new file
name_file = open('names.txt', 'a', encoding='utf-8')
name_file.write('New born baby\n')
name_file.close()

name_txt = open('names.txt', 'r')
print(name_txt.readlines())

animals = ['rabbit', 'cat', 'turtle']
animal_file = open('animals.txt', 'w', encoding='utf-8')
for animal in animals:
    animal_file.write(animal + '\n')
animal_file.close()

animal_file = open('animals.txt', 'r')
animal_space = [animal.replace('\n', ' ')
                for animal in animal_file.readlines()]
new_file = open('animals_new.txt', 'w', encoding='utf-8')
new_file.writelines(animal_space)
animal_file.close()
new_file.close()

# no need to open and close
with open('test.txt', 'r', encoding='utf-8') as in_file, \
        open('test1.txt', 'w', encoding='utf-8') as out_file:
    for line in in_file:
        out_file.write(line.lower())

with open('test.txt', 'r') as f1, \
        open('test1.txt', 'r') as f2, \
        open('test2.txt', 'w') as f3:
    first_name = f1.read()
    print(first_name)
    last_name = f2.read()
    print(last_name)
    full_name = first_name + ' ' + last_name
    print(full_name)

    f3.write(full_name)

for i in range(10):
    with open(f'file{i + 1}.txt', 'w') as f:
        f.write(str(i + 1))
        f.close()

with open('salary.txt', 'r', encoding='utf-8') as spm, \
        open('salary_year.txt', 'w', encoding='utf-8') as spy:
    # salary_year = []
    for line in spm:
        salary_year = int(line.strip()) * 12
        spy.write(str(salary_year) + '\n')
