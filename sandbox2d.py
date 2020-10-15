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
    def __init__(self, image_path, position, is_collision):
        self.image_path = image_path
        self.position = position
        self. is_collision = is_collision
        self.surface = self.load_image()

    def load_image(self):
        return pg.image.load(self.image_path).convert()


class Dirt(Block):
    pass


# Main function.
def main():
    pg.init()
    screen = pg.display.set_mode((256, 256))
    dev_block = Block(os.path.join("assets", "dev_block.png"), (0, 0), True)
    screen.blit(dev_block.surface, dev_block.position)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        pg.display.update()


if __name__ == "__main__":
    main()
