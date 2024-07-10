import random
from random import shuffle

list_ = [11, 9, 12, 7, 3]
counter = 0


def sort_algorithm(li, counter):
    shuffle(li)
    for i in range(1, len(li)):
        if li[i - 1] > li[i]:
            counter += 1
            if counter > 900:
                break
            # print(f"failed - {counter}")
            li, counter = sort_algorithm(li, counter)
            break
    return li, counter


def average():
    counts = 0
    counter_ = 0
    count_li = []

    for i in range(0, 10000):
        li, count = sort_algorithm(list_, counter)
        print(count)
        count_li.append(count)
        counts += count
        counter_ += 1
    return (counts / counter_), max(count_li), min(count_li)


if __name__ == "__main__":
    av = average()
    print(av)
