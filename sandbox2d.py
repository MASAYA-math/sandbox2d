import pygame as pg
import os


CHUNK_WIDTH = 16
CHUNK_HEIGHT = 32


# Block IDs
DEV_BLOCK_BLUE_ID = 0


chank_data_sample = []
for i in range(CHUNK_HEIGHT):
    chank_data_sample.append([])
    for j in range(CHUNK_WIDTH):
        chank_data_sample[i].append(0)


def culculate_coordinates(camera_position, block_position):
    return ((block_position[0] - camera_position[0]) * 16,
            (-(block_position[1] - camera_position[1] - 15) * 16))


class Chunk():
    def __init__(self, chunk_data, chunk_position):
        self.chunk_data = chunk_data
        self.chunk_position = chunk_position

    def draw_chunk(self, screen, camera_position):
        self.blocks = []
        for i in range(CHUNK_HEIGHT):
            for j in range(CHUNK_WIDTH):
                self.blocks.append(
                    DevBlockBlue(screen, camera_position,
                                 (j + self.chunk_position * CHUNK_WIDTH,
                                  (CHUNK_HEIGHT / 2 - 1) - i))
                    if self.chunk_data[i][j] == DEV_BLOCK_BLUE_ID else None)


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


class DevBlockBlue(Block):
    def __init__(self, screen, camera_position, position):
        super().__init__(screen, camera_position,
                         os.path.join("assets", "dev_block_blue.png"),
                         position, True)


class Dirt(Block):
    pass


# The main function.
def main():
    pg.init()
    screen = pg.display.set_mode((256, 256))
    camera_position = (0, 0)
    move_speed = 0.5
    chunk = Chunk(chank_data_sample, 0)
    while True:
        screen.fill((0, 0, 0))
        chunk.draw_chunk(screen, camera_position)
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
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        pg.display.update()


if __name__ == "__main__":
    main()
