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
    def __init__(self, screen, image_path, position, is_collision):
        self.screen = screen
        self.image_path = image_path
        self.position = position
        self. is_collision = is_collision
        self.surface = self.load_image()
        self.set_block()

    def load_image(self):
        return pg.image.load(self.image_path).convert()

    def set_block(self):
        self.screen.blit(self.surface, [n*16 for n in self.position])


class DevBlock(Block):
    def __init__(self, screen, position):
        super().__init__(screen, os.path.join("assets", "dev_block.png"),
                         position, True)


class Dirt(Block):
    pass


# The main function.
def main():
    pg.init()
    screen = pg.display.set_mode((256, 256))
    blocks = []
    for i in range(16):
        for j in range(16):
            blocks.append(DevBlock(screen, (i, j)))
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        pg.display.update()


if __name__ == "__main__":
    main()
