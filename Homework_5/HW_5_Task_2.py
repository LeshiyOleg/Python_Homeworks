# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Тот, кто берет последнюю конфету - проиграл.
# a) Добавьте игру против бота
# b) Подумайте, как наделить бота "интеллектом"

from methods import check_value_is_positive_integer_and_return_it as check
import random

# функция запускает игру в конфеты человека против человека, когда 
# каждый игрок поочередно делает ход, начиная со случайно выбранного

# def game_candies (total_amount, step_max_amount, players):
#     rest_amount = total_amount
#     while rest_amount > 0:
#         step_amount = check(f'\nThe rest is {rest_amount}. \n{players[0]} Input amount of candies for your turn: ')
#         if 0 < step_amount <= step_max_amount:
#             rest_amount -= step_amount
#             players[0], players[1] = players[1], players[0]
#             game_candies(rest_amount, step_max_amount, players)
#         else:
#             print (f'Input 1 <= amount <= {step_max_amount}!!!')
#     else:
#         print (f'\nThe winner is {players[0]}')
#         exit()

# total_amount = check ('Input total start amount of candies: ')
# step_max_amount = check ('Input max amount of candies to be taken for a step: ')
# player_1 = input('Input player_1 name: ')
# player_2 = input('Input player_2 name: ')
# players = [player_1, player_2]
# random.shuffle(players)
# game_candies(total_amount, step_max_amount, players)


# функция запускает игру в конфеты человека против бота, когда 
# поочередно делаются ходы, начиная со случайно выбранного, и бот берет рандомное количество конфет 
# от 1 до максимально возможных за ход

# def game_candies_vs_bot (total_amount, step_max_amount, players):
#     rest_amount = total_amount
#     while rest_amount > 0:
#         if players[0] != 'Bot':
#             step_amount = check(f'\nThe rest is {rest_amount}. \n{players[0]}, input amount of candies for your turn: ')
#         else:
#             step_amount = random.randint(1,step_max_amount)
#             print(f'\nThe rest is {rest_amount}. \n{players[0]} has taken {step_amount} candies')
#         if 0 < step_amount <= step_max_amount:
#             rest_amount -= step_amount
#             players[0], players[1] = players[1], players[0]
#             game_candies_vs_bot(rest_amount, step_max_amount, players)
#         else:
#             print (f'Input 1 <= amount <= {step_max_amount}!!!')

#     else:
#         print (f'\nThe winner is {players[0]}')
#         exit()

# total_amount = check ('Input total start amount of candies: ')
# step_max_amount = check ('Input max amount of candies to be taken for a step: ')
# player_1 = input('Input player_1 name: ')
# player_2 = 'Bot'
# players = [player_1, player_2]
# random.shuffle(players)
# game_candies_vs_bot(total_amount, step_max_amount, players)


# функция запускает игру в конфеты человека против бота, когда 
# поочередно делаются ходы, начиная со случайно выбранного, и бот берет определенное 
# количество конфет - он же умный бот)
def game_candies_vs_clever_bot (total_amount, step_max_amount, players):
    rest_amount = total_amount
    list_of_loser = [1+(step_max_amount+1)*i for i in range((rest_amount-1)//(step_max_amount+1)+1)]
    while rest_amount > 0:
        if players[0] != 'Bot':
            step_amount = check(f'\nThe rest is {rest_amount}. \n{players[0]}, input amount of candies for your turn: ')
        else:
            step_amount = rest_amount - list_of_loser[-1]
            if step_amount == 0:
                step_amount = 1
            print(f'\nThe rest is {rest_amount}. \n{players[0]} has taken {step_amount} candies')
        if 0 < step_amount <= step_max_amount:
            rest_amount -= step_amount
            players[0], players[1] = players[1], players[0]
            game_candies_vs_clever_bot(rest_amount, step_max_amount, players)
        else:
            print (f'Input 1 <= amount <= {step_max_amount}!!!')

    else:
        print (f'\nThe winner is {players[0]}')
        exit()

total_amount = check ('Input total start amount of candies: ')
step_max_amount = check ('Input max amount of candies to be taken for a step: ')
player_1 = input('Input player_1 name: ')
player_2 = 'Bot'
players = [player_1, player_2]
random.shuffle(players)
game_candies_vs_clever_bot(total_amount, step_max_amount, players)
