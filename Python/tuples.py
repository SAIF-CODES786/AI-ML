# immutable sequence of values
 
tup = (1, 2, 3, 4, 5)
print(tup) # (1, 2, 3, 4, 5)
print(len(tup)) # 5
print(type(tup)) # <class 'tuple'>
tup[2] = 6 # TypeError: 'tuple' object does not support item assignment
sum = 0
for num in tup:
    sum += num
print(sum) # 15

#tuples methods
tup = (1, 2, 3, 4, 5)
tup.index(3) # 2
tup.count(2) # 1