# import time

from Engine.environment import Environment

if __name__ == "__main__":

    env = Environment()

    while env.running:
        env.updateScreen()
