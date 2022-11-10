fruits = ['õun', 'pirn', 'banaan']

print('fruits')

print(fruits[0])

fruits.append('ploom')
print(fruits[-1])

fruits[2] = 'apelsiń'


if 'õun' in [el.lower() for el in fruits]:
    print('jah, õun on olemas')

print(len(fruits))

print(fruits[len(fruits)-1])

del fruits[1]
print(fruits)

fruits.reverse()
print(fruits)

fruits.sort()
print fruits()

print(fruits[1:])
