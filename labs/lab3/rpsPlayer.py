import random


class MyPlayer:
    def __init__(self):
        pass

    def play(self):
        return random.choice(["R","P","S"])


if __name__ == "__main__":
    p = MyPlayer()
    print(p.play())