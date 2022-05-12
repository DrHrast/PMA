import gc
from random import randint

class Wallet():
    def __init__(self, balance, game_cost):
        self.balance = balance
        self.cost = game_cost #Cijena jednog spina

    def ulog(self):
        gc = int(input('Unesite ulog: '))
        return gc

    def win_calc(self, per_game):
        self.balance = self.balance + per_game * 100

    def lose_calc(self, per_game):
        self.balance = self.balance - per_game

    def calc(self, per_game):
        self.balance = self.balance + per_game * 45

    def auto_sp(self, per_game, unos):
        self.balance = self.balance - (per_game * unos)

    def auto_calc(self, per_game, wc, sc):
        self.balance = self.balance + (per_game * (wc * 100))
        self.balance = self.balance + (per_game * (sc * 45))

    
def main():    
    win_txt = 'OSVOJEN JACKPOT!!'
    lose_txt = 'Promašeni brojevi.'
    balance = Wallet(100, 1)
    per_game = 1

    while True:
        unos = input()
        a = randint(6, 9)
        b = randint(6, 9)
        c = randint(6, 9)
        if balance.balance <= 0:
            print('Nemaš para buraz.')
            break
        if unos == 'end':
            break
        elif unos == '':
            print(f'[{a}] [{b}] [{c}]')
            if a == b == c == 7:
                print('*' * len(win_txt))
                print(win_txt)
                balance.win_calc(per_game)
                continue
            elif a == b == c and a != 7:
                print('SmallWin')
                balance.calc(per_game)
            else:
                print('*' * len(lose_txt))
                print(lose_txt)
                balance.lose_calc(per_game)
                continue
        elif unos == int(unos) and int(unos) >= 1:
            if balance.balance >= per_game * int(unos):
                balance.auto_sp(int(unos))
                wc, sc = auto_spin(int(unos))
                balance.auto_calc(wc, sc)
        elif unos == 'gc':
            per_game = balance.ulog()
        elif unos == 'bal':
            print(balance.balance, '$')
        if balance.balance <= 0:
            print('Nemaš para buraz.')
            break

def imput_fail():
    pass

def auto_spin(n):
    win_txt = 'OSVOJEN JACKPOT!!'
    lose_txt = 'Promašeni brojevi.'
    win_count = 0
    small_count = 0
    for i in range(n):
        a = randint(6, 9)
        b = randint(6, 9)
        c = randint(6, 9)
        print(f'[{a}] [{b}] [{c}]')
        if a == b == c == 7:
            print('*' * len(win_txt))
            print(win_txt)
            win_count += 1
            continue
        elif a == b == c and a != 7:
            print('SmallWin')
            small_count += 1
        else:
            print('*' * len(lose_txt))
            print(lose_txt)
            continue
    return win_count, small_count

main()