import numpy as np
def random_predict(number) -> int:
    """Компьютер угадывает рандомное число
    Args:
        number (int, optional): Загаданное число.
    Returns:
        int: Число попыток
    """
    predict_number = np.random.randint(1, 101) # получаем случайное число с помощью генератора
    count = 0 
    low_limit = 1 
    high_limit  = 100 
    while True: # сравниваем полученное число с загаданным, сужая радиус поиска 
        count += 1
        if predict_number > number:
            high_limit = predict_number - 1
            predict_number = (high_limit + low_limit) // 2
        elif predict_number < number:
            low_limit = predict_number + 1
            predict_number = (high_limit + low_limit) // 2
        else:
            # print(f'Компьютер угадал загаданное число за {count} попыток. Это число {number}')
            break 
    return(count)
# print(f'Количество попыток: {random_predict(number)}')
def score_game(random_predict) -> int:
    """ За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм
    Args:
        random_predict ([type]): функция угадывания
    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    random_array = np.random.randint(1, 101, size=(1000))  # создаем список загаданных чисел, на основе которого 
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")

score_game(random_predict)