weekdag = 'dinsdag'
dag = 25
maand = 'maart'
uur = 14
minuten = 15

print('{} {} {}'.format(weekdag, dag, maand))

print('{} {} {} om {}.{} uur'.format(weekdag, dag, maand, uur, minuten))

for i in range(1, 8):
    print('{} {:2} {:3}')