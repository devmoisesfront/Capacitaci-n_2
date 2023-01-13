with open('./text.txt', 'r') as file:
 for line in file:
     print(line)
file.write('nuevas cosas en este archivo')
file.write()