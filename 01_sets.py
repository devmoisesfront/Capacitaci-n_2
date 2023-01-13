set_countries ={'Colombia', 'Ecuador', 'France', 'Germany', 'Italy', 'Mexico', 'Peru', 'Spain', 'United States'}
print(set_countries)
print(type(set_countries))

set_numbers ={1, 2, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,}  
print(set_numbers)

set_types ={'int','str', 'float', 'bool', 'list', 'tuple', 'dict', 'set', 'frozenset', 'generator', 'generator', 'generator', 'generator', }
print(set_types)

set_from_strings = set( 'hola')
print(set_from_strings)

set_from_tuples = set( ('abc', 'cbv', 'as','abc'))  
print(set_from_tuples)

numbers = [1, 2, 3, 3, 5, 6, 7, 8, 9, 10, 11, 12, 14, 14, 15, 16, 17, 18, 19, 4, 1, 2, 2, 24]
set_numbers = set(numbers)
print(set_numbers)
unique_numbers = list(set_numbers)
print(unique_numbers)