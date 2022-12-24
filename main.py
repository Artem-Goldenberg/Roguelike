# import time

import entity
from environment import Environment

if __name__ == "__main__":

    env = Environment()

    while env.running:
        env.updateScreen()
