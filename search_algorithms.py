from math import sqrt


def linear(leaf:list, target):
    for i in range(len(leaf)):
        if target == leaf[i]:
            print(f'\nBroj {target} je pronađen u listi na poziciji {i + 1}.\n')
            return
        elif target < leaf[i]:
            print(f'\nNema traženog broja u listi.\n')
            return

def recurzion_binary(leaf, target, low, high):
    if low > high:
        print(f'\nNema traženog broja u listi.\n')
        return
    else:
        mid = int((low + high) / 2)
        if target == leaf[mid]:
            print(f'\nBroj {target} je pronađen u listi na poziciji {mid + 1}.\n')
            return
        elif leaf[mid] < target:
            return recurzion_binary(leaf, target, mid + 1, high)
        else:
            return recurzion_binary(leaf, target, low, mid - 1)

def noRec_binary(leaf, target): 
    high = len(leaf) - 1
    low = 0
    mid = int((high + low) / 2)
    pozition = mid
    while low <= high:
        if leaf[mid] == target:
            print(f'\nBroj {target} je pronađen u listi na poziciji {pozition + 1}.\n')
            return
        elif leaf[mid] < target:
            low = mid + 1
            mid = int((low + high) / 2)
            pozition = mid
        else:
            high = mid - 1
            mid = int((low + high) / 2)
            pozition = mid
    print(f'\nNema traženog broja u listi.\n')

def jump(leaf, target):
    step = int(sqrt(len(leaf)))
    prev = 0
    while True:
        if leaf[step] == target:
            print(f'\nBroj {target} je pronađen u listi na poziciji {step}.\n')
            return
        if leaf[step] > target:
            for i in range(step):
                if leaf[prev + i] == target:
                    print(f'\nBroj {target} je pronađen u listi na poziciji {prev + i + 1}.\n')
                    return
                elif leaf[prev + i] > target:
                    print(f'\nNema traženog broja u listi.\n')
                    return
        prev = step
        step += int(sqrt(len(leaf)))
        if step > len(leaf) - 1:
            for i in range(prev + 1,len(leaf)):
                if leaf[i] == target:
                    print(f'\nBroj {target} je pronađen u listi na poziciji {i + 1}.\n')
                    return   
            print(f'\nNema traženog broja u listi.\n')
            return
            


num_list = [1,2,3,5,8,10,11,15,16,18,20,22,31,44,45,46,47,48,50]

while True:
    print('*' * 40)
    print('LST - Pregled liste')
    print('1. Linearno pretraživanje') #Linear search algorithm
    print('2. Rakurzivno binarno pretraživanje') #Binary search algorithm
    print('3. Nerekurzivno binarno pretraživanje') #Binary search algorithm
    print('4. Skokovito pretraživanje') #Jump serach algorithm
    print('EXT - Exit')
    print('*' * 40)
    user_input = input('Unesite redni broj algoritma. ')
    if user_input == '1' or user_input == '1.':
        while True:
            num = input('Unesite broj koji bi pretražili: ')
            if num.isdigit():
                break
        linear(num_list, int(num))
    elif user_input == '2' or user_input == '2.':
        while True:
            num = input('Unesite broj koji bi pretražili: ')
            if num.isdigit():
                break
        recurzion_binary(num_list, int(num), 0, len(num_list) - 1)
    elif user_input == '3' or user_input == '3.':
        while True:
            num = input('Unesite broj koji bi pretražili: ')
            if num.isdigit():
                break
        noRec_binary(num_list, int(num))
    elif user_input == '4' or user_input == '4.':
        while True:
            num = input('Unesite broj koji bi pretražili: ')
            if num.isdigit():
                break
        jump(num_list, int(num))
    elif user_input.upper() == 'LST':
        print()
        print(num_list)
        print()
    elif user_input.upper() == 'EXT':
        break
    else:
        continue