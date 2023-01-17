from Engine.eventSystem import Event, eventType
from Engine.activeEntityMetaLogic import EntityMetaLogic, Strategy


RANGE = 3

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

class EnemyStrategyAggressive(Strategy):
    def __init__(self, _data):
        Strategy.__init__(self, _data)

    def process(self, _dt: float):
        player_pos = _toCells(self.data.env, self.data.env.player.data.position)
        pos = _toCells(self.data.env, self.data.position)
        # print(f'dist: {manhattan(self.data.position, player_pos)=}')
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
    def __init__(self, _data):
        Strategy.__init__(self, _data)

    def process(self, _dt: float):
        self.data.setInstructions([])


class EnemyStrategyFlee(Strategy):
    def __init__(self, _data):
        Strategy.__init__(self, _data)

    def process(self, _dt: float):
        player_pos = _toCells(self.data.env, self.data.env.player.data.position)
        pos = _toCells(self.data.env, self.data.position)
        # print(f'dist: {manhattan(self.data.position, player_pos)=}')
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
    def __init__(self, _data):
        Strategy.__init__(self, _data)

    def process(self, _dt: float):
        pass 


class EnemyMetaLogic(EntityMetaLogic):
    def __init__(self, _data):
        strategies = { 
            "Aggressive": EnemyStrategyAggressive,
            "Passive": EnemyStrategyPassive,
            "Flee": EnemyStrategyFlee
        }

        EntityMetaLogic.__init__(self, _data, strategies)