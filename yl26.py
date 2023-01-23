data = '''Revenue

            Johnver Vanston Danbree Vansey  Mundyke
Tea             190     140    1926     14      143
Coffee          325      19     293   1491      162
Water           682      14     852     56      659
Milk            829     140     609    120       87

Expenses

            Johnver Vanston Danbree Vansey  Mundyke
Tea             120      65     890     54      430
Coffee          300      10      23    802      235
Water            50     299    1290     12      145
Milk             67     254      89    129       76'''

data_f = [line.split() for line in data.split('\n') if line]

exp_start = data_f.index(['Expenses'])

commissions = [0]*len(data_f[1])

for p in range(len(data_f[1])):
    for i in range(exp_start - 2):
        rev = int(data_f[2 + i][1 + p]) - int(data_f[2 + i + exp_start][1 + p])
        if rev > 0:
            commissions[p] += 0.062 * rev

print('\t  ', end='')
for i in data_f[1]:
    print('', i, end='')

print('\nCommission:', end='')

for indx, com in enumerate(commissions):
    for length in range(len(data_f[1][indx]) - len(str(int(com)))):
        print(' ', end='')
    print(int(com), end=' ')

