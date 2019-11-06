import random


def random_famous(famous, count=2):
    """
    Недетерминированная функция
    :param famous: писок людей
    :param count: количество
    :return: лучайных людей

    """
    return random.sample(famous, count)