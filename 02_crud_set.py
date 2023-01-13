set_countries = {'Colombia', 'Ecuador', 'France', 'Germany', 'Italy', 'Mexico', 'Peru', 'Spain', 'United States'}  

size = len(set_countries)
print(size)

print('Colombia' in set_countries)
print('Ecuador' in set_countries)

#add
set_countries.add('Peru')  
print(set_countries)  
set_countries.add('Peru')
print(set_countries)
size = len(set_countries)
print(size)

#update 
set_countries.update({'Argentina', 'Paraguay','Uruguay'})
size = len(set_countries)
print(set_countries)
print(size)

#remove
set_countries.remove('Colombia')
print(set_countries)  
size = len(set_countries)
print(size)

set_countries.remove('Peru')
print(set_countries)
size = len(set_countries)
print(size)
#remove all

set_countries.discard('Argentina') 
print(set_countries)  
size = len(set_countries)
print(size)
set_countries.add('Argentina')
print(set_countries)

set_countries.clear()
print(set_countries)
size = len(set_countries)
print(size)



