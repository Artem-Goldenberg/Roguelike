import random

from Engine.eventSystem import Event, eventType
from Engine.activeEntityMetaLogic import EntityMetaLogic, Strategy


RANGE = 5
PANIC_HP = 10
CONFUSE_RANGE = 3
TOTAL_TIME_CONFUSED = 10


def sign(num):
    if num > 0:
        return 1
    return -1


def manhattan(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def _toCells(_env, pos):
    return (
            pos[0] // _env.grid_step, 
            pos[1] // _env.grid_step
        )


def _checkConfused(data):
    for event in data.env.pastEvents.getEvents(eventType.MassiveAttack):
        pos = _toCells(data.env, data.position)
        if event.data[0] == pos[0] and event.data[1] == pos[1]:
            return True
    return False


class EnemyStrategyAggressive(Strategy):
    def __init__(self, _data, _previous_strategy):
        Strategy.__init__(self, _data, _previous_strategy)

    def process(self, _dt: float):
        if self.data.hp <= PANIC_HP:
            self.data.meta_state = "Flee"
            return 

        if _checkConfused(self.data):
            self.data.meta_state = "Confused"
            return

        player_pos = _toCells(self.data.env, self.data.env.player.data.position)
        pos = _toCells(self.data.env, self.data.position)
        if manhattan(pos, player_pos) <= RANGE:
            # player in the range, attack him
            self.data.setInstructions(self._instructionsToPlayer())
        else:
            # no one to chase
            self.data.setInstructions([])

    def _instructionsToPlayer(self):
        player_pos = self.data.env.player.data.position
        pos = self.data.position
        dx =  player_pos[0] - pos[0]
        dy =  player_pos[1] - pos[1]

        if dx == dy == 0: # already at the player 
            return []

        if abs(dy) > abs(dx): # move vertically
            data = (0, sign(dy))
        else: # move horizontally
            data = (sign(dx), 0)
        
        return [Event(eventType.Move, self, data)]


class EnemyStrategyPassive(Strategy):
    def __init__(self, _data, _previous_strategy):
        Strategy.__init__(self, _data, _previous_strategy)

    def process(self, _dt: float):
        if _checkConfused(self.data):
            self.data.meta_state = "Confused"
            return

        self.data.setInstructions([])


class EnemyStrategyFlee(Strategy):
    def __init__(self, _data, _previous_strategy):
        self.previous_strategy = _previous_strategy
        Strategy.__init__(self, _data, _previous_strategy)

    def process(self, _dt: float):
        if self.data.hp > PANIC_HP and self.previous_strategy is not None:
            self.data.meta_state = self.previous_strategy
            return

        if _checkConfused(self.data):
            self.data.meta_state = "Confused"
            return

        player_pos = _toCells(self.data.env, self.data.env.player.data.position)
        pos = _toCells(self.data.env, self.data.position)
        if manhattan(pos, player_pos) <= RANGE:
            # player in the range, attack him
            self.data.setInstructions(self._instructionsFromPlayer())
        else:
            # no one to chase
            self.data.setInstructions([])
    
    def _instructionsFromPlayer(self):
        # backwards to '_instructionToPlayer`
        player_pos = self.data.env.player.data.position
        pos = self.data.position
        dx =  player_pos[0] - pos[0]
        dy =  player_pos[1] - pos[1]

        if dx == dy == 0: # already at the player 
            return []

        if abs(dy) > abs(dx): # move vertically
            data = (0, -sign(dy))
        else: # move horizontally
            data = (-sign(dx), 0)
        
        return [Event(eventType.Move, self, data)] 


class EnemyStrategyConfused(Strategy):
    def __init__(self, _data, _previous_strategy):
        self.original_strategy = _previous_strategy

        # will just look in random direction without it
        self.time_delay = 0.3
        self.current_delay = 0.0

        self.time_lasts = 0.0
        Strategy.__init__(self, _data, _previous_strategy)

    def process(self, _dt: float):
        if _checkConfused(self.data):
            # reset timer
            self.time_lasts = 0
            return

        self.time_lasts += _dt
        if self.time_lasts >= TOTAL_TIME_CONFUSED:
            self.data.meta_state = self.original_strategy
            return

        self.current_delay += _dt
        if self.current_delay < self.time_delay: return
        else: self.current_delay = 0
        
        # confusing code, ha-ha
        cell = random.randint(0, 3)
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.data.setInstructions([Event(eventType.Move, self, neighbors[cell])])


class EnemyMetaLogic(EntityMetaLogic):
    def __init__(self, _data):
        strategies = { 
            "Aggressive": EnemyStrategyAggressive,
            "Passive": EnemyStrategyPassive,
            "Flee": EnemyStrategyFlee,
            "Confused": EnemyStrategyConfused
        }

        EntityMetaLogic.__init__(self, _data, strategies)