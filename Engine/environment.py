import logging
import pygame
import time
import sys

# from math import fabs

# from entity import Entity
from Engine.chunk import Chunk
from Engine.eventSystem import EventSystem, KeyboardEventSystem
from Player.player import Player
from ObjectsFactory.objectFactory import ObjectFactory


def sign(num):
    if num > 0:
        return 1
    return -1


class Environment:
    def __init__(self):

        logFormatter = logging.Formatter(
            fmt="%(asctime)s.%(msecs)03d [%(levelname)s]  %(message)s",
            datefmt='%H:%M:%S'
        )
        rootLogger = logging.getLogger()
        rootLogger.setLevel(logging.INFO)

        fileHandler = logging.FileHandler(filename="rogue_like.log")
        fileHandler.setFormatter(logFormatter)
        rootLogger.addHandler(fileHandler)

        consoleHandler = logging.StreamHandler(sys.stdout)
        consoleHandler.setFormatter(logFormatter)
        rootLogger.addHandler(consoleHandler)

        logging.info("Initing pygame")
        pygame.init()
        logging.info("Pygame inited")

        self.clock = pygame.time.Clock()

        logging.info("Initing window")
        self.screen = pygame.display.set_mode([800, 600], pygame.RESIZABLE)
        self.window_height = self.screen.get_height()
        self.window_width = self.screen.get_width()
        logging.info("Window inited")

        logging.info("Initing constants")
        self.grid_step = 75
        self.chunk_gap = 1
        self.chunk_width = 19
        self.chunk_height = 11
        self.running = True
        self.bg_color = (0, 0, 0)
        self.camera_position = [0, 0]
        self.time = time.time()
        self.camera_move_speed = 150
        logging.info("Constants inited")

        logging.info("Initing object factory")
        self.object_factory = ObjectFactory()
        logging.info("Object factory inited")


        logging.info("Initing chunks")
        self.available_chunks = {}
        self.active_chunks = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                new_chunk = Chunk(
                    self,
                    [
                        self.grid_step*self.chunk_width*i,
                        self.grid_step*self.chunk_height*j
                    ]
                )
                self.available_chunks[(i, j)] = new_chunk
                self.active_chunks.append(new_chunk)
        logging.info("Chunks inited")

        logging.info("Initing event systems")
        self.pastEvents = EventSystem()
        self.futureEvents = EventSystem()
        self.keyboardEvents = KeyboardEventSystem()
        logging.info("Event systems inited")

        logging.info("Initing player")
        self.player = Player(self)
        logging.info("Player inited")

    def updateScreen(self):

        #    ____                    __
        #   / __/ _  __ ___   ___   / /_  ___
        #  / _/  | |/ // -_) / _ \ / __/ (_-<
        # /___/  |___/ \__/ /_//_/ \__/ /___/

        for event in pygame.event.get():
            if event.type == pygame.VIDEORESIZE:
                self.window_height = event.h
                self.window_width = event.w
                logging.info("Window resize: " + str(self.window_height) + "x" + str(self.window_width))
            if event.type == pygame.QUIT:
                self.running = False

        self.keyboardEvents.updateKeysPresed()

        #   _____  __                 __              __                 __
        #  / ___/ / /   __ __  ___   / /__  ___      / /  ___  ___ _ ___/ /
        # / /__  / _ \ / // / / _ \ /  '_/ (_-<     / /__/ _ \/ _ `// _  /
        # \___/ /_//_/ \_,_/ /_//_//_/\_\ /___/    /____/\___/\_,_/ \_,_/

        def sign(num):
            if num > 0:
                return 1
            return -1

        self.active_chunks = [
            ch if
                abs(ch.pos[0] - self.player.data.position[0]) < 1.5 * self.chunk_width * self.grid_step and
                abs(ch.pos[1] - self.player.data.position[1]) < 1.5 * self.chunk_height * self.grid_step
            else
                self.load_chunk(
                    (
                        ch.pos[0] - 3*self.grid_step*self.chunk_width*sign(ch.pos[0] - self.player.data.position[0])
                        if
                            abs(ch.pos[0] - self.player.data.position[0]) > 1.5 * self.chunk_width * self.grid_step
                        else
                            ch.pos[0]
                        ,
                        ch.pos[1] - 3*self.grid_step*self.chunk_height*sign(ch.pos[1] - self.player.data.position[1])
                        if
                            abs(ch.pos[1] - self.player.data.position[1]) > 1.5 * self.chunk_height * self.grid_step
                        else
                            ch.pos[1]
                    )
                )
            for
                ch
            in
                self.active_chunks
        ]

        #   __  __           __        __                   __       _
        #  / / / / ___   ___/ / ___ _ / /_ ___       ___   / /      (_)
        # / /_/ / / _ \ / _  / / _ `// __// -_)     / _ \ / _ \    / /
        # \____/ / .__/ \_,_/  \_,_/ \__/ \__/      \___//_.__/ __/ /
        #       /_/                                            |___/

        dt = time.time() - self.time
        # print("fps: " + str(1/dt))
        self.time = time.time()

        self.player.logic.handleEvents(dt)

        for chunk in self.active_chunks:
            for entity in chunk.entities:
                entity.logic.handleEvents(dt)

        self.pastEvents = self.futureEvents
        self.futureEvents = EventSystem()

        #   _____
        #  / ___/ ___ _  __ _   ___   ____ ___ _
        # / /__  / _ `/ /  ' \ / -_) / __// _ `/
        # \___/  \_,_/ /_/_/_/ \__/ /_/   \_,_/

        if self.player.data.position[0] - self.camera_position[0] < self.window_width/3:
            self.camera_position[0] -= dt * self.camera_move_speed
        if self.player.data.position[0] - self.camera_position[0] > self.window_width*2/3:
            self.camera_position[0] += dt * self.camera_move_speed
        if self.player.data.position[1] - self.camera_position[1] < self.window_height/3:
            self.camera_position[1] -= dt * self.camera_move_speed
        if self.player.data.position[1] - self.camera_position[1] > self.window_height*2/3:
            self.camera_position[1] += dt * self.camera_move_speed

        self.screen.fill(self.bg_color)

        #    ___                                 __                __
        #   / _ \  ____ ___ _ _    __     ____  / /  __ __  ___   / /__
        #  / // / / __// _ `/| |/|/ /    / __/ / _ \/ // / / _ \ /  '_/
        # /____/ /_/   \_,_/ |__,__/     \__/ /_//_/\_,_/ /_//_//_/\_\

        for chunk in self.active_chunks:
            chunk.drawChunk(self.screen, self.camera_position)

        #    ____        __    _   __    _
        #   / __/ ___   / /_  (_) / /_  (_) ___   ___
        #  / _/  / _ \ / __/ / / / __/ / / / -_) (_-<
        # /___/ /_//_/ \__/ /_/  \__/ /_/  \__/ /___/

        for chunk in self.active_chunks:
            chunk.drawEntities(dt, self.screen, self.camera_position)

        #    ___    __
        #   / _ \  / / ___ _  __ __ ___   ____
        #  / ___/ / / / _ `/ / // // -_) / __/
        # /_/    /_/  \_,_/  \_, / \__/ /_/
        #                   /___/

        self.player.draw(dt, self.screen, self.camera_position)


        pygame.display.flip()

    def addChunk(self, pos, chunk):
        self.chunks[pos] = chunk

    def load_chunk(self, pos):
        if self.available_chunks.__contains__(pos):
            return self.available_chunks[pos]
        new_chunk = Chunk(self, pos)
        self.available_chunks[pos] = new_chunk
        return new_chunk
