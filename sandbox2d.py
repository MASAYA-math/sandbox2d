import pygame as pg
import os


def culculate_coordinates(camera_position, block_position):
    return ((block_position[0] - camera_position[0]) * 16,
            (-(block_position[1] - camera_position[1] - 15) * 16))


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
    def __init__(self, screen, camera_position,
                 image_path, position, is_collision):
        self.screen = screen
        self.camera_position = camera_position
        self.image_path = image_path
        self.position = position
        self. is_collision = is_collision
        self.surface = self.load_image()
        self.set_block()

    def load_image(self):
        return pg.image.load(self.image_path).convert()

    def set_block(self):
        self.screen.blit(self.surface, culculate_coordinates(
            self.camera_position, self.position))


class DevBlock(Block):
    def __init__(self, screen, camera_position, position):
        super().__init__(screen, camera_position,
                         os.path.join("assets", "dev_block.png"),
                         position, True)


class Dirt(Block):
    pass


# The main function.
def main():
    pg.init()
    screen = pg.display.set_mode((256, 256))
    blocks = []
    camera_position = (0, 0)
    move_speed = 0.1
    while True:
        screen.fill((0, 0, 0))
        # for i in range(16):
        #     for j in range(16):
        #         blocks.append(DevBlock(screen, camera_position, (i, j)))
        blocks.append(DevBlock(screen, camera_position, (15, 15)))
        blocks.append(DevBlock(screen, camera_position, (14, 14)))
        blocks.append(DevBlock(screen, camera_position, (0, 0)))
        blocks.append(DevBlock(screen, camera_position, (16, 16)))
        blocks.append(DevBlock(screen, camera_position, (15, 0)))
        blocks.append(DevBlock(screen, camera_position, (0, 15)))
        blocks.append(DevBlock(screen, camera_position, (1, 14)))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if pg.key.get_pressed()[pg.K_w]:
                camera_position = (
                    camera_position[0], camera_position[1] + move_speed)
            if pg.key.get_pressed()[pg.K_a]:
                camera_position = (
                    camera_position[0] - move_speed, camera_position[1])
            if pg.key.get_pressed()[pg.K_s]:
                camera_position = (
                    camera_position[0], camera_position[1] - move_speed)
            if pg.key.get_pressed()[pg.K_d]:
                camera_position = (
                    camera_position[0] + move_speed, camera_position[1])

        pg.display.update()


if __name__ == "__main__":
    main()
