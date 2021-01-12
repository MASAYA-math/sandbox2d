import pygame as pg
import os


CHUNK_WIDTH = 16
CHUNK_HEIGHT = 32


# Block IDs
DEV_BLOCK_BLUE_ID = 0
DEV_BLOCK_AQUA_ID = 1


chunk_data_sample = []
for i in range(CHUNK_HEIGHT):
    chunk_data_sample.append([])
    for j in range(CHUNK_WIDTH):
        if i >= 15:
            chunk_data_sample[i].append(DEV_BLOCK_BLUE_ID)
        else:
            chunk_data_sample[i].append(DEV_BLOCK_AQUA_ID)

chunk_data_sample_2 = []
for i in range(CHUNK_HEIGHT):
    chunk_data_sample_2.append([])
    for j in range(CHUNK_WIDTH):
        if i >= 12:
            chunk_data_sample_2[i].append(DEV_BLOCK_BLUE_ID)
        else:
            chunk_data_sample_2[i].append(DEV_BLOCK_AQUA_ID)


def calculate_coordinates(camera_position, block_position):
    return ((block_position[0] - camera_position[0]) * 16,
            (-(block_position[1] - camera_position[1] - 15) * 16))


def by_id_make_block(id, block_position):
    if id == DEV_BLOCK_BLUE_ID:
        return DevBlockBlue(block_position)
    elif id == DEV_BLOCK_AQUA_ID:
        return DevBlockAqua(block_position)


class Chunk():
    def __init__(self, chunk_data, chunk_position):
        self.chunk_data = chunk_data
        self.chunk_position = chunk_position
        self.blocks = []
        for i in range(CHUNK_HEIGHT):
            for j in range(CHUNK_WIDTH):
                self.blocks.append(
                    by_id_make_block(self.chunk_data[i][j],
                                     (j + self.chunk_position * CHUNK_WIDTH,
                                      (CHUNK_HEIGHT / 2 - 1) - i)))

    def draw_chunk(self, screen, camera_position):
        for i in self.blocks:
            i.draw_block(screen, camera_position)


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

    def draw_block(self, screen, camera_position):
        screen.blit(self.surface, calculate_coordinates(
            camera_position, self.position))


class DevBlockBlue(Block):
    def __init__(self, position):
        super().__init__(os.path.join("assets", "dev_block_blue.png"),
                         position, True)


class DevBlockAqua(Block):
    def __init__(self, position):
        super().__init__(os.path.join("assets", "dev_block_aqua.png"),
                         position, True)


class Dirt(Block):
    pass


# The main function.
def main():
    pg.init()
    screen = pg.display.set_mode((512, 512))
    camera_position = (0, 0)
    move_speed = 0.01
    chunk = Chunk(chunk_data_sample, 0)
    chunk_2 = Chunk(chunk_data_sample_2, 1)
    chunk_3 = Chunk(chunk_data_sample, 2)
    while True:
        screen.fill((0, 0, 0))
        chunk.draw_chunk(screen, camera_position)
        chunk_2.draw_chunk(screen, camera_position)
        chunk_3.draw_chunk(screen, camera_position)
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
