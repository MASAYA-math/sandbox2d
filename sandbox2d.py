import pygame as pg
import os


# Block IDs
DEV_BLOCK_ID = 0


chank_data_sample = []
for i in range(64):
    chank_data_sample.append([])
    for j in range(16):
        chank_data_sample[i].append(0)


def culculate_coordinates(camera_position, block_position):
    return ((block_position[0] - camera_position[0]) * 16,
            (-(block_position[1] - camera_position[1] - 15) * 16))


def draw_map(screen, camera_position):
    blocks = []
    blocks.append(DevBlock(screen, camera_position, (15, 15)))
    blocks.append(DevBlock(screen, camera_position, (14, 14)))
    blocks.append(DevBlock(screen, camera_position, (0, 0)))
    blocks.append(DevBlock(screen, camera_position, (16, 16)))
    blocks.append(DevBlock(screen, camera_position, (15, 0)))
    blocks.append(DevBlock(screen, camera_position, (0, 15)))
    blocks.append(DevBlock(screen, camera_position, (1, 14)))


class Chunk():
    def __init__(self, chunk_data, chunk_position):
        self.chunk_data = chunk_data
        self.chunk_position = chunk_position

    def draw_chunk(self, screen, camera_position):
        self.blocks = []
        for i in range(64):
            for j in range(16):
                self.blocks.append(
                    DevBlock(screen, camera_position,
                             (j + self.chunk_position * 16, 31 - i))
                    if self.chunk_data[i][j] == 0 else None)


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
    camera_position = (0, 0)
    move_speed = 1
    chunk = Chunk(chank_data_sample, 0)
    while True:
        screen.fill((0, 0, 0))
        # draw_map(screen, camera_position)
        chunk.draw_chunk(screen, camera_position)
        # for i in range(16):
        #     for j in range(16):
        #         blocks.append(DevBlock(screen, camera_position, (i, j)))
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
