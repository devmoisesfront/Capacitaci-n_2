set_a = {'colombia','brasil','bolivia'}
set_b = {'bolivia','peru'}
# UNION
set_c = set_a.union(set_b)
print(set_c)
print(set_a | set_b)
# Intersección
set_c = set_a.intersection(set_b)
print(set_c)
print(set_a & set_b)
# Diferencia
print(set_a.difference(set_b))
print(set_c)
print(set_a -set_b)
print(set_a.symmetric_difference(set_b))
print(set_c)                
print(set_a ^ set_b)