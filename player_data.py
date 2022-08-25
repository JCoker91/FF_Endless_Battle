from source.util.custom_enum import PlayerSide

CHARACTERS = [
    {
        'name': 'Lightning',
        'stats': {
            'level': 1, 'hp': 500, 'mp': 50, 'break_power': 20, 'strength': 100, 'magic': 50, 'defense': 100, 'magic_defense': 50, 'speed': 55, 'mp_regen': 5
        },
        'resistance': {
            'physical': 0, 'magic': 0, 'lightning': 0, 'fire': 0, 'water': 0, 'ice': 0, 'wind': 0, 'earth': 0, 'dark': 0, 'light': 0
        },
        'skill_data': {
            'skill_1':  {
                'particle_effects': ['slash', 'slash', 'slash', 'slash', 'shards', 'shards', 'shards'],
                'particle_action_frames': [3,  12,  17,  22, 27, 28, 29],
                'damage_weight': [3, 3, 3, 3, 2, 2, 2]}
        },
        'limit_break_data': {
            'limit_break':  {
                'particle_effects': ['slash', 'slash', 'slash', 'slash','slash', 'shards', 'shards', 'shards', 'shards', 'slash', 'slash', 'slash'],
                'particle_action_frames': [6,9,12,18,23,28,30,34,41,47,50,52],
                'damage_weight': [1,1,1,1,1,1,1,1,1,1,1,1]}
        },
        'off_set': {
            'left':
            {
                'idle': (0, 0),
                'attack': (-15, -73),
                'magic_attack': (0, 0),
                'magic_standby': (0, 0),
                'attack_standby': (0, 0),
                'limit_break': (-60, -90),
                'dying': (5, 10),
                'dead': (0, 15),
                'move': (0, 0),
                'jump': (0, 0),
            },
            'right':        {
                'idle': (0, 0),
                'attack': (-160, -73),
                'magic_attack': (0, 0),
                'magic_standby': (0, 0),
                'attack_standby': (0, 0),
                'limit_break': (-170, -90),
                'dying': (0, 10),
                'dead': (0, 15),
                'move': (0, 0),
                'jump': (0, 0),
            },
        },
        'side': PlayerSide.LEFT,
    },
    {
        'name': 'Cloud',
        'stats': {
            'level': 1, 'hp': 500, 'mp': 50, 'break_power': 20, 'strength': 100, 'magic': 50, 'defense': 100, 'magic_defense': 50, 'speed': 48, 'mp_regen': 5
        },
        'resistance': {
            'physical': 0, 'magic': 0, 'lightning': 0, 'fire': 0, 'water': 0, 'ice': 0, 'wind': 0, 'earth': 0, 'dark': 0, 'light': 0
        },
        'skill_data': {
            'skill_1':  {
                'particle_effects': ['slash'],
                'particle_action_frames': [2],
                'damage_weight': [1],
            },
        },
        'limit_break_data': {
            'limit_break':  {
                'particle_effects': ['slash', 'slash', 'slash', 'slash','slash','slash','slash','slash','slash','slash','slash','slash','slash','slash','slash','slash'],
                'particle_action_frames': [44,45,49,52,60,63,66,72,75,79,83,90,94,97,103,122],
                'damage_weight': [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,10]
            },
        },
        'off_set': {
            'left':
            {
                'idle': (0, 0),
                'attack': (-25, -32),
                'magic_attack': (0, 0),
                'magic_standby': (0, 0),
                'attack_standby': (0, 0),
                'limit_break': (-47, -162),
                'dying': (8, 18),
                'dead': (0, 40),
                'move': (0, 0),
                'jump': (0, 0),
            },
            'right':        {
                'idle': (0, 0),
                'attack': (-52, -32),
                'magic_attack': (0, 0),
                'magic_standby': (0, 0),
                'attack_standby': (0, 0),
                'limit_break': (-185, -162),
                'dying': (-7, 18),
                'dead': (0, 40),
                'move': (0, 0),
                'jump': (0, 0),
            },
        },
        'side': PlayerSide.LEFT,
    },
    {
        'name': 'Tidus',
        'stats': {
            'level': 1, 'hp': 500, 'mp': 50, 'break_power': 20, 'strength': 100, 'magic': 50, 'defense': 100, 'magic_defense': 50, 'speed': 55, 'mp_regen': 5
        },
        'resistance': {
            'physical': 0, 'magic': 0, 'lightning': 0, 'fire': 0, 'water': 0, 'ice': 0, 'wind': 0, 'earth': 0, 'dark': 0, 'light': 0
        },
        'skill_data': {
            'skill_1': {
                'particle_effects': ['slash'],
                'particle_action_frames': [3],
                'damage_weight': [1],
            },
        },
        'limit_break_data': {
            'limit_break':  {
                'particle_effects': ['slash', 'slash', 'slash', 'slash', 'shards', 'shards', 'shards'],
                'particle_action_frames': [3,  12,  17,  22, 27, 28, 29],
                'damage_weight': [3, 3, 3, 3, 2, 2, 2]
            },
        },
        'off_set': {
            'left':
            {
                'idle': (0, 0),
                'attack': (0, -31),
                'magic_attack': (0, 0),
                'magic_standby': (0, 0),
                'attack_standby': (0, 0),
                'limit_break': (-60, -125),
                'dying': (0, 5),
                'dead': (0, 20),
                'move': (0, 0),
                'jump': (0, 0),
            },
            'right':        {
                'idle': (0, 0),
                'attack': (-70, -31),
                'magic_attack': (0, 0),
                'magic_standby': (0, 0),
                'attack_standby': (0, 0),
                'limit_break': (-125, -125),
                'dying': (25, 5),
                'dead': (0, 20),
                'move': (0, 0),
                'jump': (0, 0),
            },
        },
        'side': PlayerSide.RIGHT,
    },
    {
        'name': 'Firion',
        'stats': {
            'level': 1, 'hp': 500, 'mp': 50, 'break_power': 20, 'strength': 100, 'magic': 50, 'defense': 100, 'magic_defense': 50, 'speed': 52, 'mp_regen': 5
        },
        'resistance': {
            'physical': 0, 'magic': 0, 'lightning': 0, 'fire': 0, 'water': 0, 'ice': 0, 'wind': 0, 'earth': 0, 'dark': 0, 'light': 0
        },
        'skill_data': {
            'skill_1':  {
                'particle_effects': ['slash', 'slash'],
                'particle_action_frames': [3, 9],
                'damage_weight': [1, 1],
            },
        },
        'limit_break_data': {
            'limit_break':  {
                'particle_effects': ['slash', 'slash', 'slash', 'slash', 'shards', 'shards', 'shards'],
                'particle_action_frames': [3,  12,  17,  22, 27, 28, 29],
                'damage_weight': [3, 3, 3, 3, 2, 2, 2]
            },
        },
        'off_set': {
            'left':
            {
                'idle': (0, 0),
                'attack': (3, -27),
                'magic_attack': (0, 0),
                'magic_standby': (0, 0),
                'attack_standby': (0, 0),
                'limit_break': (0, 0),
                'dying': (0, 0),
                'dead': (0, 0),
                'move': (0, 0),
                'jump': (0, 0),
            },
            'right':        {
                'idle': (0, 0),
                'attack': (-34, -27),
                'magic_attack': (0, 0),
                'magic_standby': (0, 0),
                'attack_standby': (0, 0),
                'limit_break': (0, 0),
                'dying': (0, 0),
                'dead': (0, 0),
                'move': (0, 0),
                'jump': (0, 0),
            },
        },
        'side': PlayerSide.RIGHT,
    },
    {
        'name': 'Cecil',
        'stats': {
            'level': 1, 'hp': 500, 'mp': 50, 'break_power': 20, 'strength': 100, 'magic': 50, 'defense': 100, 'magic_defense': 42, 'speed': 50, 'mp_regen': 5
        },
        'resistance': {
            'physical': 0, 'magic': 0, 'lightning': 0, 'fire': 0, 'water': 0, 'ice': 0, 'wind': 0, 'earth': 0, 'dark': 0, 'light': 0
        },
        'skill_data': {
            'skill_1':  {
                'name': 'Attack',
                'particle_effects': ['slash'],
                'particle_action_frames': [8],
                'damage_weight': [1],
            },
        },
        'limit_break_data': {
            'limit_break':  {
                'particle_effects': ['slash', 'slash', 'slash', 'slash', 'shards', 'shards', 'shards'],
                'particle_action_frames': [3,  12,  17,  22, 27, 28, 29],
                'damage_weight': [3, 3, 3, 3, 2, 2, 2]
            },
        },
        'off_set': {
            'left':
            {
                'idle': (0, 0),
                'attack': (-30, -44),
                'magic_attack': (0, 0),
                'magic_standby': (0, 0),
                'attack_standby': (0, 0),
                'limit_break': (0, 0),
                'dying': (0, 0),
                'dead': (0, 0),
                'move': (0, 0),
                'jump': (0, 0),
            },
            'right':        {
                'idle': (0, 0),
                'attack': (-127, -44),
                'magic_attack': (0, 0),
                'magic_standby': (0, 0),
                'attack_standby': (0, 0),
                'limit_break': (0, 0),
                'dying': (0, 0),
                'dead': (0, 0),
                'move': (0, 0),
                'jump': (0, 0),
            },
        },
        'side': PlayerSide.LEFT,
    },
    {
        'name': 'Bartz',
        'stats': {
            'level': 1, 'hp': 500, 'mp': 50, 'break_power': 20, 'strength': 100, 'magic': 50, 'defense': 100, 'magic_defense': 50, 'speed': 53, 'mp_regen': 5
        },
        'resistance': {
            'physical': 0, 'magic': 0, 'lightning': 0, 'fire': 0, 'water': 0, 'ice': 0, 'wind': 0, 'earth': 0, 'dark': 0, 'light': 0
        },
        'skill_data': {
            'skill_1': {
                'particle_effects': ['slash', 'slash'],
                'particle_action_frames': [0, 6],
                'damage_weight': [1, 1],
            },
        },
        'limit_break_data': {
            'limit_break':  {
                'particle_effects': ['slash', 'slash', 'slash', 'slash', 'shards', 'shards', 'shards'],
                'particle_action_frames': [3,  12,  17,  22, 27, 28, 29],
                'damage_weight': [3, 3, 3, 3, 2, 2, 2]
            },
        },
        'off_set': {
            'left':
            {
                'idle': (0, 0),
                'attack': (-13, -21),
                'magic_attack': (0, 0),
                'magic_standby': (0, 0),
                'attack_standby': (0, 0),
                'limit_break': (0, 0),
                'dying': (0, 0),
                'dead': (0, 0),
                'move': (0, 0),
                'jump': (0, 0),
            },
            'right':        {
                'idle': (0, 0),
                'attack': (-140, -21),
                'magic_attack': (0, 0),
                'magic_standby': (0, 0),
                'attack_standby': (0, 0),
                'limit_break': (0, 0),
                'dying': (0, 0),
                'dead': (0, 0),
                'move': (0, 0),
                'jump': (0, 0),
            },
        },
        'side': PlayerSide.RIGHT,
    },
    {
        'name': 'Zidane',
        'stats': {
            'level': 1, 'hp': 500, 'mp': 50, 'break_power': 20, 'strength': 100, 'magic': 50, 'defense': 100, 'magic_defense': 50, 'speed': 60, 'mp_regen': 5
        },
        'resistance': {
            'physical': 0, 'magic': 0, 'lightning': 0, 'fire': 0, 'water': 0, 'ice': 0, 'wind': 0, 'earth': 0, 'dark': 0, 'light': 0
        },
        'skill_data': {
            'skill_1': {
                'particle_effects': ['slash', 'slash', 'slash'],
                'particle_action_frames': [1, 4, 7],
                'damage_weight': [1, 1, 2],
            },
        },
        'limit_break_data': {
            'limit_break':  {
                'particle_effects': ['slash', 'slash', 'slash', 'slash', 'shards', 'shards', 'shards'],
                'particle_action_frames': [3,  12,  17,  22, 27, 28, 29],
                'damage_weight': [3, 3, 3, 3, 2, 2, 2]
            },
        },
        'off_set': {
            'left':
            {
                'idle': (0, 0),
                'attack': (-1, -20),
                'magic_attack': (0, 0),
                'magic_standby': (0, 0),
                'attack_standby': (0, 0),
                'limit_break': (0, 0),
                'dying': (0, 0),
                'dead': (0, 0),
                'move': (0, 0),
                'jump': (0, 0),
            },
            'right':        {
                'idle': (0, 0),
                'attack': (-50, -20),
                'magic_attack': (0, 0),
                'magic_standby': (0, 0),
                'attack_standby': (0, 0),
                'limit_break': (0, 0),
                'dying': (0, 0),
                'dead': (0, 0),
                'move': (0, 0),
                'jump': (0, 0),
            },
        },
        'side': PlayerSide.RIGHT,
    },
    {
        'name': 'Tera',
        'stats': {
            'level': 1, 'hp': 500, 'mp': 50, 'break_power': 20, 'strength': 100, 'magic': 50, 'defense': 100, 'magic_defense': 50, 'speed': 49, 'mp_regen': 5
        },
        'resistance': {
            'physical': 0, 'magic': 0, 'lightning': 0, 'fire': 0, 'water': 0, 'ice': 0, 'wind': 0, 'earth': 0, 'dark': 0, 'light': 0
        },
        'skill_data': {
            'skill_1': {
                'particle_effects': ['shards', 'shards', 'shards', 'shards', 'shards', ],
                'particle_action_frames': [3, 4, 5, 6, 7],
                'damage_weight': [1, 1, 1, 1, 1],
            },
        },
        'limit_break_data': {
            'limit_break':  {
                'particle_effects': ['slash', 'slash', 'slash', 'slash', 'shards', 'shards', 'shards'],
                'particle_action_frames': [3,  12,  17,  22, 27, 28, 29],
                'damage_weight': [3, 3, 3, 3, 2, 2, 2]
            },
        },
        'off_set': {
            'left':
            {
                'idle': (0, 0),
                'attack': (0, 2),
                'magic_attack': (0, 0),
                'magic_standby': (0, 0),
                'attack_standby': (0, 0),
                'limit_break': (0, 0),
                'dying': (0, 0),
                'dead': (0, 0),
                'move': (0, 0),
                'jump': (0, 0),
            },
            'right':        {
                'idle': (0, 0),
                'attack': (-127, 2),
                'magic_attack': (0, 0),
                'magic_standby': (0, 0),
                'attack_standby': (0, 0),
                'limit_break': (0, 0),
                'dying': (0, 0),
                'dead': (0, 0),
                'move': (0, 0),
                'jump': (0, 0),
            },
        },
        'side': PlayerSide.LEFT,
    },
    {
        'name': 'Noctis',
        'stats': {
            'level': 1, 'hp': 500, 'mp': 50, 'break_power': 20, 'strength': 100, 'magic': 50, 'defense': 100, 'magic_defense': 50, 'speed': 52, 'mp_regen': 5
        },
        'resistance': {
            'physical': 0, 'magic': 0, 'lightning': 0, 'fire': 0, 'water': 0, 'ice': 0, 'wind': 0, 'earth': 0, 'dark': 0, 'light': 0
        },
        'skill_data': {
            'skill_1': {
                'particle_effects': ['shards', 'slash', 'slash'],
                'particle_action_frames': [12, 16, 19],
                'damage_weight': [5, 4, 4],
            },
        },
        'limit_break_data': {
            'limit_break':  {
                'particle_effects': ['slash', 'slash', 'slash', 'slash', 'shards', 'shards', 'shards'],
                'particle_action_frames': [3,  12,  17,  22, 27, 28, 29],
                'damage_weight': [3, 3, 3, 3, 2, 2, 2]
            },
        },
        'off_set': {
            'left':
            {
                'idle': (0, 0),
                'attack': (-139, -50),
                'magic_attack': (0, 0),
                'magic_standby': (0, 0),
                'attack_standby': (0, 0),
                'limit_break': (0, 0),
                'dying': (0, 0),
                'dead': (0, 0),
                'move': (0, 0),
                'jump': (0, 0),
            },
            'right':        {
                'idle': (0, 0),
                'attack': (-78, -50),
                'magic_attack': (0, 0),
                'magic_standby': (0, 0),
                'attack_standby': (0, 0),
                'limit_break': (0, 0),
                'dying': (0, 0),
                'dead': (0, 0),
                'move': (0, 0),
                'jump': (0, 0),
            },
        },
        'side': PlayerSide.LEFT,
    },
    {
        'name': 'Squall',
        'stats': {
            'level': 1, 'hp': 500, 'mp': 50, 'break_power': 20, 'strength': 100, 'magic': 50, 'defense': 100, 'magic_defense': 50, 'speed': 50, 'mp_regen': 5
        },
        'resistance': {
            'physical': 0, 'magic': 0, 'lightning': 0, 'fire': 0, 'water': 0, 'ice': 0, 'wind': 0, 'earth': 0, 'dark': 0, 'light': 0
        },
        'skill_data': {
            'skill_1': {
                'particle_effects': ['slash'],
                'particle_action_frames': [3],
                'damage_weight': [1],
            },
        },
        'limit_break_data': {
            'limit_break':  {
                'particle_effects': ['slash', 'slash', 'slash', 'slash', 'shards', 'shards', 'shards'],
                'particle_action_frames': [3,  12,  17,  22, 27, 28, 29],
                'damage_weight': [3, 3, 3, 3, 2, 2, 2]
            },
        },
        'off_set': {
            'left':
            {
                'idle': (0, 0),
                'attack': (-10, -9),
                'magic_attack': (0, 0),
                'magic_standby': (0, 0),
                'attack_standby': (0, 0),
                'limit_break': (0, 0),
                'dying': (0, 0),
                'dead': (0, 0),
                'move': (0, 0),
                'jump': (0, 0),
            },
            'right':        {
                'idle': (0, 0),
                'attack': (-80, -9),
                'magic_attack': (0, 0),
                'magic_standby': (0, 0),
                'attack_standby': (0, 0),
                'limit_break': (0, 0),
                'dying': (0, 0),
                'dead': (0, 0),
                'move': (0, 0),
                'jump': (0, 0),
            },
        },
        'side': PlayerSide.LEFT,
    },
]
