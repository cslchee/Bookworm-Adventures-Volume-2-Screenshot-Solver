tile_palettes = {
    'normal': { # based on a normal 'A' block
        'multiplier': 1.00,
        'palette': [
            (228,216,153),
            (17,15,11),
            (146,132,84),
            (111,91,49),
            (246,239,216),
            (246,239,216),
            (143,116,63),
            (173,140,89)
        ]
    },
    'amethyst': {
        'multiplier': 1.15,
        'palette':[
            (246, 156, 248),
            (163, 53, 191),
            (245, 100, 248),
            (123, 40, 151),
            (200, 112, 221),
            (144, 53, 147),
            (202, 68, 242),
            (202, 61, 210)
        ]
    },
    'emerald': {
            'multiplier': 1.20,
            'palette':[
                (49,142,59),
                (112,234,93),
                (54,191,73),
                (123,195,122),
                (45,216,67),
                (47,103,51),
                (85,163,71),
                (100,204,116)
            ]
        },
    'sapphire': {
        'multiplier': 1.25,
        'palette':[
            (31,103,235),
            (85,190,252),
            (158,196,252),
            (68,157,251),
            (35,75,162),
            (61,126,235),
            (28,54,215),
            (84,140,252)
        ]
    },
    'garnet': {
        'multiplier': 1.30,
        'palette':[
            (228,131,23),
            (252,237,138),
            (152,87,6),
            (251,179,84),
            (252,191,124),
            (249,179,54),
            (193,85,24),
            (252,204,76)
        ]
    },
    'ruby': {
        'multiplier': 1.35,
        'palette':[
            (251,149,144),
            (231,25,23),
            (252,114,122),
            (152,10,6),
            (250,89,88),
            (181,11,8),
            (241,58,73),
            (252,140,124)
        ]
    },
    'crystal': {
        'multiplier': 1.50,
        'palette':[
            (251,231,250),
            (209,99,177),
            (247,187,239),
            (247,155,232),
            (238,150,209),
            (194,86,122),
            (235,120,210),
            (166,84,145)
        ]
    },
    'diamond': {
        'multiplier': 2.00,
        'palette':[
            (206,195,206),
            (110,103,100),
            (155,144,146),
            (250,247,235),
            (125,118,131),
            (164,151,170),
            (132,132,124),
            (164,164,175)
        ]
    },
}

raw_palettes = [value['palette'] for value in tile_palettes.values()]