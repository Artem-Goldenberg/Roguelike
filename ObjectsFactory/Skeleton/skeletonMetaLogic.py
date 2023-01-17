from Engine.activeEntityMetaLogic import EntityMetaLogic, Strategy


class SkeletonStrategyPassive(Strategy):
    def process(self, _dt):
        # actually being passive
        pass


class SkeletonMetaLogic(EntityMetaLogic):
    def __init__(self, _data):
        strategies = {
            "Passive": SkeletonStrategyPassive
        }

        EntityMetaLogic.__init__(self, _data, strategies)