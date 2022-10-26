a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

if a + b > c and a + c > b and b + c > a:
   
    if a == b == c:
        print('kolmnurk on võrdkülgne')
    elif a == b or b == c or c == a:
        print('kolmnurk on võrdhaarne')
    else:
        print('kolmnurk on võrdkülgne')

else:
    print('Selliste küljepikkustega kolmnurka ei saa eksisteerida')

