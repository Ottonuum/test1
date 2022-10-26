n = int(input('Sisesta aasta number: '))

if n % 400 == 0 or (n % 4 == 0 and n % 100 != 0): 
    print(n, 'on liigaasta: ')
else:
    print(n, 'on lihtaasta: ')

