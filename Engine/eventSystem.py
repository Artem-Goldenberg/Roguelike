import enum
import pygame
import time
import logging


class eventType(enum.Enum):
    PickUp = 1,
    Pickable = 2
    Atack = 3,
    Move = 4,
    MoveProhibited = 5,
    Moved = 6,
    MassiveAttack = 7,
    SomeoneThere = 8,
    Custom = 9


class Event:
    def __init__(self, _event_type, _origin, _data=None):
        self.event_type = _event_type
        self.origin = _origin
        self.data = _data


class EventSystem:
    def __init__(self):
        self.events = []

    def sendEvent(self, _event):
        self.events.append(_event)
        logging.info("EventSystem: new event: " + str(_event.event_type) + ": " + str(_event.data))

    def getEvents(self, _eventType):
        return [e for e in self.events if e.event_type == _eventType]

    def clearEvents(self):
        self.events = []


class KeyboardEventSystem():
    def __init__(self):
        self.events = []
        self.time_last_pressed = {}
        self.press_timeout = 0.0

    def updateKeyPress(self, _key, _event_type, _data=None):
        if not self.time_last_pressed.__contains__(_key):
            self.time_last_pressed[_key] = time.time()
            self.events.append(Event(_event_type, self, _data))
        elif time.time() - self.time_last_pressed[_key] > self.press_timeout:
            self.events.append(Event(_event_type, self, _data))
            self.time_last_pressed[_key] = time.time()

    def updateKeysPresed(self):
        self.events = []
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.updateKeyPress(pygame.K_UP, eventType.Move, (0, -1))
        if keys[pygame.K_DOWN]:
            self.updateKeyPress(pygame.K_DOWN, eventType.Move, (0, 1))
        if keys[pygame.K_LEFT]:
            self.updateKeyPress(pygame.K_LEFT, eventType.Move, (-1, 0))
        if keys[pygame.K_RIGHT]:
            self.updateKeyPress(pygame.K_RIGHT, eventType.Move, (1, 0))
        if keys[pygame.K_i]:
            self.updateKeyPress(pygame.K_i, eventType.Custom, "ToggleInventory")
        if keys[pygame.K_m]:
            self.updateKeyPress(pygame.K_m, eventType.Custom, "ToggleMap")
        if keys[pygame.K_x]:
            self.updateKeyPress(pygame.K_x, eventType.Atack, "Normal")
        if keys[pygame.K_z]:
            self.updateKeyPress(pygame.K_z, eventType.Atack, "Massive")
        if keys[pygame.K_c]:
            self.updateKeyPress(pygame.K_c, eventType.PickUp)
        if keys[pygame.K_ESCAPE]:
            self.updateKeyPress(pygame.K_ESCAPE, eventType.Custom, "Settings")
        if keys[pygame.K_1]:
            self.updateKeyPress(pygame.K_1, eventType.Custom, "InventoryItem1")
        if keys[pygame.K_2]:
            self.updateKeyPress(pygame.K_2, eventType.Custom, "InventoryItem2")
        if keys[pygame.K_3]:
            self.updateKeyPress(pygame.K_3, eventType.Custom, "InventoryItem3")
        if keys[pygame.K_4]:
            self.updateKeyPress(pygame.K_4, eventType.Custom, "InventoryItem4")
        if keys[pygame.K_5]:
            self.updateKeyPress(pygame.K_5, eventType.Custom, "InventoryItem5")
        if keys[pygame.K_6]:
            self.updateKeyPress(pygame.K_6, eventType.Custom, "InventoryItem6")
        if keys[pygame.K_7]:
            self.updateKeyPress(pygame.K_7, eventType.Custom, "InventoryItem7")
        if keys[pygame.K_8]:
            self.updateKeyPress(pygame.K_8, eventType.Custom, "InventoryItem8")
        if keys[pygame.K_9]:
            self.updateKeyPress(pygame.K_9, eventType.Custom, "InventoryItem9")
        if keys[pygame.K_a]:
            self.updateKeyPress(pygame.K_a, eventType.Custom, "UseItem")

    def getEvents(self, _eventType=None):
        if _eventType is not None:
            return [e for e in self.events if e.event_type == _eventType]
        return self.events
