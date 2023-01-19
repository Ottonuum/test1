me = {
    'first_name': 'Otto',
    'last_name': 'Nuum',
    'birth_year': 2005,
    'place_of_living': 'Upa',
    'dessert': 'Kirju koer'
}

# print(me.get('place_of_living'))
# print(me['place_of_living'])

me['dessert'] = 'ice cream'

for k, v in me.items():
    print(k, v)

print(me.keys())

print(me.values())

if 'id' in me:
    print('id')
else:
    print('No id')

print(len(me))

me.update({'lenght': len(me)})

me.pop('birth_year')

del me 
