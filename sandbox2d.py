import pygame as pg
import os


# Life entities
class Player():
    pass


class Mob():
    pass


class Animal(Mob):
    pass


class Enemy(Mob):
    pass


class Pig(Animal):
    pass


class Zombie(Enemy):
    pass


# Block entities.
class Block():
    def __init__(self, image_path, x_pos, y_pos, is_collision):
        self.image_path = image_path
        self.x_pos = x_pos
        self.y_pos = y_pos
        self. is_collision = is_collision


class Dirt(Block):
    pass


# Main function.
def main():
    pg.init()
    screen = pg.display.set_mode((256, 256))
    dev_block = Block(os.path.join("assets", "dev_block.png"), 0, 0, True)
    screen.blit(pg.image.load(dev_block.image_path).convert(), (0, 0))
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        pg.display.update()


if __name__ == "__main__":
    main()
