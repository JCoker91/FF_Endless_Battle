from source.util.custom_enum import PlayerSide

CHARACTERS = [
    {
        'name': 'Lightning',
        'stats': {
            'level': 1, 'hp': 500, 'mp': 50, 'break_power': 20, 'strength': 50, 'magic': 50, 'defense': 50, 'magic_defense': 50, 'speed': 55
        },
        'abilities': {
            'basic_attack': {
                'name': 'Basic Attack',
                'particle_effects': ['slash', 'slash', 'slash', 'slash', 'shards', 'shards', 'shards'],
                'particle_action_frames': [3,  12,  17,  22, 27, 28, 29],
                'damage_weight': [3, 3, 3, 3, 2, 2, 2],
            }
        },
        'off_set': {
            'left':
            {
                'idle': (0, 0),
                'attack': (-15, -73),
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
                'attack': (-160, -73),
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
        'name': 'Cloud',
        'stats': {
            'level': 1, 'hp': 500, 'mp': 50, 'break_power': 20, 'strength': 50, 'magic': 50, 'defense': 50, 'magic_defense': 50, 'speed': 48
        },
        'abilities': {
            'basic_attack': {
                'particle_effects': ['slash'],
                'particle_action_frames': [2],
                'damage_weight': [1],
            }
        },
        'off_set': {
            'left':
            {
                'idle': (0, 0),
                'attack': (-25, -32),
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
                'attack': (-52, -32),
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
        'name': 'Tidus',
        'stats': {
            'level': 1, 'hp': 500, 'mp': 50, 'break_power': 20, 'strength': 50, 'magic': 50, 'defense': 50, 'magic_defense': 50, 'speed': 55
        },
        'abilities': {
            'basic_attack': {
                'particle_effects': ['slash'],
                'particle_action_frames': [3],
                'damage_weight': [1],
            }
        },
        'off_set': {
            'left':
            {
                'idle': (0, 0),
                'attack': (0, -31),
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
                'attack': (-70, -31),
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
        'name': 'Firion',
        'stats': {
            'level': 1, 'hp': 500, 'mp': 50, 'break_power': 20, 'strength': 50, 'magic': 50, 'defense': 50, 'magic_defense': 50, 'speed': 52
        },
        'abilities': {
            'basic_attack': {
                'particle_effects': ['slash', 'slash'],
                'particle_action_frames': [3, 9],
                'damage_weight': [1, 1],
            }
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
            'level': 1, 'hp': 500, 'mp': 50, 'break_power': 20, 'strength': 50, 'magic': 50, 'defense': 50, 'magic_defense': 42, 'speed': 50
        },
        'abilities': {
            'basic_attack': {
                'particle_effects': ['slash'],
                'particle_action_frames': [8],
                'damage_weight': [1],
            }
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
            'level': 1, 'hp': 500, 'mp': 50, 'break_power': 20, 'strength': 50, 'magic': 50, 'defense': 50, 'magic_defense': 50, 'speed': 53
        },
        'abilities': {
            'basic_attack': {
                'particle_effects': ['slash', 'slash'],
                'particle_action_frames': [0, 6],
                'damage_weight': [1, 1],
            }
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
            'level': 1, 'hp': 500, 'mp': 50, 'break_power': 20, 'strength': 50, 'magic': 50, 'defense': 50, 'magic_defense': 50, 'speed': 60
        },
        'abilities': {
            'basic_attack': {
                'particle_effects': ['slash', 'slash', 'slash'],
                'particle_action_frames': [1, 4, 7],
                'damage_weight': [1, 1, 2],
            }
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
            'level': 1, 'hp': 500, 'mp': 50, 'break_power': 20, 'strength': 50, 'magic': 50, 'defense': 50, 'magic_defense': 50, 'speed': 49
        },
        'abilities': {
            'basic_attack': {
                'particle_effects': ['shards', 'shards', 'shards', 'shards', 'shards', ],
                'particle_action_frames': [3, 4, 5, 6, 7],
                'damage_weight': [1, 1, 1, 1, 1],
            }
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
            'level': 1, 'hp': 500, 'mp': 50, 'break_power': 20, 'strength': 50, 'magic': 50, 'defense': 50, 'magic_defense': 50, 'speed': 52
        },
        'abilities': {
            'basic_attack': {
                'particle_effects': ['shards', 'slash', 'slash'],
                'particle_action_frames': [12, 16, 19],
                'damage_weight': [5, 4, 4],
            }
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
            'level': 1, 'hp': 500, 'mp': 50, 'break_power': 20, 'strength': 50, 'magic': 50, 'defense': 50, 'magic_defense': 50, 'speed': 50
        },
        'abilities': {
            'basic_attack': {
                'particle_effects': ['slash'],
                'particle_action_frames': [3],
                'damage_weight': [1],
            }
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
