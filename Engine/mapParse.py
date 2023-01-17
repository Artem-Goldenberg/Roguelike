import logging
from Engine.chunk import Chunk


def parseMap(_env, _file_name="map.cfg"):
    current_graphics_name = None
    current_logic_name = None
    current_meta_logic_name = None
    current_position = None
    current_inventory_items_names = []
    current_entity_instructions = None

    config_file = open(_file_name, "r")
    for line in config_file:
        stripped_line = line.split()

        if len(stripped_line) == 0:
            continue

        if stripped_line[0] == "Entity":
            past_entity_instruction = current_entity_instructions
            current_entity_instructions = stripped_line[1:]

            if current_logic_name is None:
                continue
            if current_graphics_name is None:
                continue
            if current_logic_name is None:
                continue
            if current_position is None:
                continue
            if current_meta_logic_name is not None:
                addToChunks(
                    _env.object_factory.getActiveEntity(
                        current_meta_logic_name,
                        current_logic_name,
                        current_graphics_name,
                        _pos=current_position,
                        _items_names=current_inventory_items_names
                    ),
                    past_entity_instruction,
                    _env
                )
            else:
                addToChunks(
                    _env.object_factory.getSimpleEntity(
                        current_logic_name,
                        current_graphics_name,
                        _pos=current_position,
                        _items_names=current_inventory_items_names
                    ),
                    past_entity_instruction,
                    _env
                )
            current_graphics_name = None
            current_logic_name = None
            current_meta_logic_name = None
            current_position = None
            current_inventory_items_names = []
            continue

        if stripped_line[0] == "Inventory":
            current_inventory_items_names = stripped_line[1:]
            continue

        if stripped_line[0] == "Logic":
            if len(stripped_line) != 2:
                logging.warning(f'ParseMap: wrong number of arguments in line "{line}"')
            else:
                current_logic_name = stripped_line[1]
            continue

        if stripped_line[0] == "Graphics":
            if len(stripped_line) != 2:
                logging.warning(f'ParseMap: wrong number of arguments in line "{line}"')
            else:
                current_graphics_name = stripped_line[1]
            continue

        if stripped_line[0] == "Position":
            if len(stripped_line) != 3:
                logging.warning(f'ParseMap: wrong number of arguments in line "{line}"')
            else:
                current_position = [
                    int(stripped_line[1]) * _env.grid_step,
                    int(stripped_line[2]) * _env.grid_step
                ]
            continue

        if stripped_line[0] == "MetaLogic":
            if len(stripped_line) != 2:
                logging.warning(f'ParseMap: wrong number of arguments in line "{line}"')
            else:
                current_meta_logic_name = stripped_line[1]
            continue

    if current_logic_name is None:
        return
    if current_graphics_name is None:
        return
    if current_logic_name is None:
        return
    if current_position is None:
        return
    if current_meta_logic_name is not None:
        addToChunks(
            _env.object_factory.getActiveEntity(
                current_meta_logic_name,
                current_logic_name,
                current_graphics_name,
                _pos=current_position,
                _items_names=current_inventory_items_names
            ),
            current_entity_instructions,
            _env
        )
    else:
        addToChunks(
            _env.object_factory.getSimpleEntity(
                current_logic_name,
                current_graphics_name,
                _pos=current_position,
                _items_names=current_inventory_items_names
            ),
            current_entity_instructions,
            _env
        )


def addToChunks(_obj, _instructions, _env):
    pos = _obj.data.position
    chunk_pos = (
        (pos[0] // _env.grid_step + _env.chunk_width//2) // _env.chunk_width,
        (pos[1] // _env.grid_step + _env.chunk_height//2) // _env.chunk_height
    )
    chunk_real_pos = (
        _env.grid_step*_env.chunk_width*chunk_pos[0],
        _env.grid_step*_env.chunk_height*chunk_pos[1]
    )
    print(f"Chunk: {chunk_pos}")
    desired_chunk = None

    if _env.available_chunks.__contains__(chunk_real_pos):
        desired_chunk = _env.available_chunks[chunk_real_pos]
    else:
        desired_chunk = Chunk(
            _env, [
                chunk_pos[0] * _env.chunk_width * _env.grid_step,
                chunk_pos[1] * _env.chunk_height * _env.grid_step
            ]
        )
        _env.available_chunks[chunk_real_pos] = desired_chunk

    if len(_instructions) == 0:
        logging.warning('AddToChunk: no arguments to entity')
        return

    if _instructions[0] == "BG":
        desired_chunk.addToBG(_obj)
        return
    if _instructions[0] == "FG":
        desired_chunk.addToFG(_obj)
        return
