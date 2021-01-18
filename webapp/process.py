# seed the pseudorandom number generator
from random import seed
from random import randint, random


def example(test):
    print(test)
    # seed random number generator
    seed(345)
    # generate some random numbers
    hours = randint(0, 4)
    minutes = randint(0, 59)

    print("Time left: " + str(hours) + ":" + str(minutes))
    return str(hours) + ":" + str(minutes)
