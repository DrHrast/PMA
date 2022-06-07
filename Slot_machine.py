from random import randint

counter = 1
win_txt = 'OSVOJEN JACKPOT!!'
lose_txt = 'Promašeni brojevi.'
while counter < 11:
    a = randint(6, 9)
    b = randint(6, 9)
    c = randint(6, 9)
    print(f'{counter}. Pokušaj od 10.')
    print(f'[{a}] [{b}] [{c}]')
    if a == b == c == 7:
        print('*' * len(win_txt))
        print(win_txt)
        break
    else:
        print('*' * len(lose_txt))
        print(lose_txt)
        counter += 1
        continue