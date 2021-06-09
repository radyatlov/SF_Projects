import numpy as np


def game_core_v2(number):
    count = 1
    predict = np.random.randint(1, 101)
    min_ = 0
    max_ = 101
    while number != predict:
        count += 1
        if number > predict:
            min_ = predict
            predict = predict + ((max_ - predict) // 2)
        elif number < predict:
            max_ = predict
            predict = min_ + ((predict - min_) // 2)
        else:
            break
    return count  # выход из цикла, если угадали


def score_game(game_core):
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


score_game(game_core_v2)
