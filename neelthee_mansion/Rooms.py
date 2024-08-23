from .items import *
from .creatures import *

global KEY, ROOMS

KEY = [
    '█ = wall', 
    '║ = door', 
    '☼ = drawers', 
    '╦ = rack', 
    'Γ = stand', 
    '╖ = stairs', 
    'æ = cupboards', 
    '√ = fireplace', 
    '∩ = gate', 
    '┬ = table', 
    'í = hedge', 
    '∟ = railing', 
    '↨ = sofa', 
    'š = storage device',
    '¥ = tree',
    '§ = bed',
    '╬ = wardrobe',
    'π = desk',
]

global map_dict, positions

def string_to_2d_list(map_str):
    map_str = map_str.strip()  # Remove leading/trailing whitespace
    return [list(line) for line in map_str.split('\n')]

def SetMapsAndPosiitionsDicts(map_dict, positions):
    map_dict = {}

    positions = {}
    for RoomName, RoomItem in ROOMS.items():
        if 'descovered' in RoomItem and 'position' in RoomItem and 'map' in RoomItem:
            if RoomItem['descovered']:
                map_dict[RoomName] = string_to_2d_list(RoomItem['map'])
                positions[RoomName] = RoomItem['position']
    return map_dict, positions

def combine_maps(small_maps, positions: dict):
    # Check if positions dictionary is empty
    if not positions:
        # Return an empty map and a min_z value of 0
        return [[[' ']]], 0

    # Determine the size of the largest map needed
    max_z = max(pos[0] for pos in positions.values()) + 1
    min_z = min(pos[0] for pos in positions.values())
    total_z = max_z - min_z  # Total floors including basements
    max_row = max(pos[1] for pos in positions.values()) + 9
    max_col = max(pos[2] for pos in positions.values()) + 9
    
    # Create a 3D large map with spaces
    large_map = [[[' ' for _ in range(max_col)] for _ in range(max_row)] for _ in range(total_z)]
    
    # Fill the large map with small maps
    for name, (z, row_offset, col_offset) in positions.items():
        small_map = small_maps[name]
        
        # Adjust for negative z values (basement floors)
        z_index = z - min_z
        
        for r in range(9):
            for c in range(9):
                large_map[z_index][row_offset + r][col_offset + c] = small_map[r][c]
    
    return large_map, min_z

def display_map(large_map, min_z):
    floors = []
    for z, floor in enumerate(large_map):
        if z == -min_z:
            floor_str = f"Ground Floor:\n" + '\n'.join(''.join(row) for row in floor)
        elif z > -min_z:
            floor_str = f"Floor {z + min_z}:\n" + '\n'.join(''.join(row) for row in floor)
        else:
            floor_str = f"Basement {-(-z + min_z)}:\n" + '\n'.join(''.join(row) for row in floor)
        floors.append(floor_str)
    return '\n\n'.join(floors)

def ShowMap():
    global map_dict, positions
    map_dict, positions = SetMapsAndPosiitionsDicts(map_dict, positions)
    large_map, min_z = combine_maps(map_dict, positions)
    return display_map(large_map, min_z)


map_dict = {}

positions = {}

#a dictionary linking a room to other rooms
ROOMS = {

                'Hall': {
                    'room type': 'house',
                    'position': (0, 8, 0),
                    'descovered': True,
                    'directions': {
                        'south': 'Kitchen',
                        'east': 'Dining Room',
                        'north': 'Armoury',
                        'up': 'Landing',
                        'easter': 'Cavegame',
                        },
                    'item': item('torch'),
                    'containers': {
                        'drawers': container([item('key')]),
                        },
                    'info': 'You are in the hall of the house. There is a chest of %*RED*%drawers%*RESET*% against one wall, and flaming %*BLUE*%torch%*RESET*%es on the walls. You hear a \
%*YELLOW*%smash%*RESET*% from the %*GREEN*%south%*RESET*%',
                    'map': '''
████║████
█☼☼     █
█       █
█       █
█       ║
█       █
█╖      █
█╖      █
████║████''',
                    'Hints': [
                            'Those %*RED*%drawers%*RESET*% look intresting',
                            'I wonder if those %*RED*%drawers%*RESET*% are locked',
                            "I wonder if I can get this %*BLUE*%torch%*RESET*% out of it's holder",
                            "I wonder what that %*YELLOW*%smash%*RESET*% from the %*GREEN*%south%*RESET*% was",
                            "I should probably aviod that %*YELLOW*%smash%*RESET*%ing sound",
                        ],
                    },
                
                'Cavegame': {
                    'room type': 'easter egg',
                    'directions': {
                        'back': 'Hall',
                        },
                    'info': 'Cavegame, type "go back" to leave',
                    },

                'Kitchen': {
                    'room type': 'house',
                    'position': (0, 16, 0),
                    'descovered': False,
                    'directions': {
                        'north': 'Hall',
                        'east': 'Garden',
                        },
                    'item': item('rations'),
                    'containers': {
                        'cupboards': container([item('money-pouch', 'valuable', 10)]),
                        },
                    'creatures stats': [creature(
                        'hungry bear', 
                        7, 
                        5, 
                        [item('claw')],
                        'A large 7ft 8 brown bear that looks hungry',
                        'A %*CYAN*%hungry%*RESET*% bear attacks you!',
                        ),
                    ],
                    'info': 'You are in the kitchen, there are several trashed %*RED*%cupboards%*RESET*%, one of them has a knotted cord sticking out, and a fireplace.',
                    'map': '''
████║████
█       █
█       █
█       █
█       ║
█       █
█       █
█ææææ√ææ█
█████████''',
                    'Hints': [
                        'I wonder if there is anything salvageable in the %*RED*%cupboards%*RESET*%',
                        'I should probably look around',
                    ],
                    },

                'Dining Room': {
                    'room type': 'house',
                    'position': (0, 8, 8),
                    'descovered': False,
                    'directions': {
                        'west': 'Hall',
                        'south': 'Garden',
                        'north': 'Sitting Room',
                        },
                    'item': item('potion'),
                    'containers': {
                        'chandelier': container([item('gem', 'valuable', 50)]),
                        },
                    'info': 'You are in the dining room, there is a dining table with 8 chairs around it in the middle of the room, and a %*RED*%chandelier%*RESET*% on the ceiling. You hear \
%*YELLOW*%ripping%*RESET*% from the %*GREEN*%north%*RESET*%',
                    'map': '''
████║████
█       █
█       █
█  ┬┬┬  █
║  ┬┬┬  █
█  ┬┬┬  █
█       █
█       █
████║████''',
                    'Hints': [
                        'I wonder if there is anything in the %*RED*%chandelier',
                        'I wonder if there is anything around the room',
                    ],
                    },

                'Garden': {
                    'room type': 'house',
                    'position': (0, 16, 8),
                    'descovered': False,
                    'directions': {
                        'north': 'Dining Room',
                        'west': 'Kitchen',
                        },
                    'info': 'You are in a bright garden you are in a garden with a gate out of the house.',
                    'map': '''
████║████
█       í
█       í
█       í
║       í
█       í
█       ∩
█       í
█íííííííí''',
                    'Hints': [
                        'I think I need a %*BLUE*%key%*RESET*% for the gate',
                    ],
                    },

                'Armoury': {
                    'room type': 'house',
                    'position': (0, 0, 0),
                    'descovered': False,
                    'directions': {
                        'south' :'Hall',
                        'east': 'Sitting Room',
                        'up': 'Tower Bottom',
                        },
                    'containers': {
                        'racks': container([item('sword', 'weapon', 3)]),
                        'stand': container([item('armour')]),
                        'storage': container([item('grappling-hook')]),
                        },
                    'info': 'You are in a dimly lit armoury with 3 %*RED*%racks%*RESET*% full of damaged weapons, and a armour %*RED*%stand%*RESET*% with battered armour. \n\
You notice a ''%*RED*%storage%*RESET*% device in one corner. You hear a %*YELLOW*%ripping%*RESET*% from the %*GREEN*%east%*RESET*%.',
                    'map': '''
█████████
█š     ╖█
█      ╖█
█╦      █
█       ║
█       █
█Γ      █
█       █
████║████''',
                    'Hints': [
                        'Maybe there is something salvageable on the %*RED*%racks%*RESET*%',
                        'I wonder if that armour is salvageable',
                    ],
                    },

                'Sitting Room': {
                    'room type': 'house',
                    'position': (0, 0, 8),
                    'descovered': False,
                    'directions': {
                        'west': 'Armoury',
                        'south': 'Dining Room',
                        'down': 'Basement 1',
                        },
                    'creatures stats': creature(
                        'grumpy pig',
                        3,
                        4,
                        [item('savaged cushion')],
                        'A oxford sandy & black pig with a savaged cushion on it\'s head',
                        'A %*CYAN*%grumpy pig%*RESET*% spots you and comes towards you!',
                        ),
                    'containers': {
                        'sofas': container([item('cushion')]),
                        },
                    'info': 'You are in a bright sitting room with several %*RED*%sofas%*RESET*%.',
                    'map': '''
█████████
█      ╖█
█  ↨↨↨ ╖█
█     ↨ █
║     ↨ █
█     ↨ █
█       █
█       █
████║████''',
                    'Hints': [
                        'That %*CYAN*%pig%*RESET*% seems dangerous',
                        'Those %*RED*%sofas%*RESET*% look comfy',
                        "I wonder what's %*GREEN*%down%*RESET*% those stairs",
                    ],
                    },

                'Landing': {
                    'room type': 'house',
                    'position': (1, 8, 0),
                    'descovered': False,
                    'directions': {
                        'down': 'Hall',
                        'north': 'Tower Bottom',
                        'east': 'Bedroom',
                        'south': 'Balcony',
                        },
                    'containers': {
                        'floorboards': container([item('money-pouch', 'valuable', 10)]),
                        },
                    'info': 'You are in a dark landing with creaky %*RED*%floorboards%*RESET*%.',
                    'map': '''
████║████
█       █
█       █
█       █
█       ║
█       █
█╖      █
█╖      █
████║████''',
                    'Hints': [
                        'I wonder if I can pry one of the %*RED*%floorboards%*RESET*% back'
                    ],
                    },

                'Bedroom': {
                    'room type': 'house',
                    'position': (1, 8, 8),
                    'descovered': False,
                    'directions': {
                        'west': 'Landing',
                        'north': 'Office',
                        },
                    'containers': {
                        'bed': container([item('chamber-pot')]),
                        'drawers': container([item('waterskin')]),
                        'wardrobe': container([item('pig-rod')]),
                        },
                    'info': 'You are in a dark yet airy bedroom, with a double %*RED*%bed%*RESET*%, a chest of %*RED*%drawers%*RESET*%, and a %*RED*%wardrobe%*RESET*%.',
                    'map': '''
████║████
█       █
█       █
█       █
║       █
█       █
█╬    §§█
█╬  ☼☼§§█
█████████''',
                    'Hints': [
                        "I wonder what's %*GREEN*%north%*RESET*%",
                        'I wonder if there is anything under the %*RED*%bed%*RESET*%',
                        'I wonder if there is anything in the %*RED*%drawers%*RESET*%',
                        "I wonder what's in the %*RED*%wardrobe%*RESET*%",
                    ],
                    },

                'Office': {
                    'room type': 'house',
                    'position': (1, 0, 8),
                    'descovered': False,
                    'directions': {
                        'south': 'Bedroom',
                        'west': 'Tower Bottom',
                        },
                    'containers': {
                        'storage': container([item('saddle'), item('ink-pot'), item('parchment'), item('knife', 'weapon', 2)]),
                        'desk': container([item('quill')]),
                        },
                    'info': 'You are in a bright office with a %*RED*%desk%*RESET*%, several %*RED*%storage%*RESET*% devices, and a lot of windows.',
                    'map': '''
█████████
█ š    š█
█       █
█   π š █
║   π   █
█   πš  █
█š      █
█       █
████║████''',
                    'Hints': [
                        "I wonder what's in the %*RED*%storage%*RESET*%, if anything",
                        "I wonder what's through the %*GREEN*%south%*RESET*%ern door",
                        'I wonder if there is anything on the %*RED*%desk%*RESET*%',
                    ],
                    },

                'Balcony': {
                    'room type': 'house',
                    'position': (1, 16, 0),
                    'descovered': False,
                    'directions': {
                        'north': 'Landing',
                        },
                    'info': 'You are on a balcony with an ornate railing. It is a nice day.',
                    'map': '''
████║████
∟       ∟
∟       ∟
∟       ∟
∟       ∟
∟       ∟
∟       ∟
∟       ∟
∟∟∟∟∟∟∟∟∟''',
                    'Hints': [
                        'If I had a %*BLUE*%grappling-hook%*RESET*% I might be able to throw it into the trees and swing down into the forest',
                    ],
                    },
         
                'Tower Bottom': {
                    'room type': 'house',
                    'position': (1, 0, 0),
                    'descovered': False,
                    'directions': {
                        'south': 'Landing',
                        'east': 'Office',
                        'down': 'Armoury',
                        'up': 'Tower Middle',
                        },
                    'info': 'You are in the base of a stone tower, there is a spiral staircase going up into the darkness.',
                    'map': '''
█████████
█      ╖█
█      ╖█
█       █
█       ║
█       █
█╖      █
█╖      █
████║████''',
                    'Hints': ["I wonder what's %*GREEN*%south%*RESET*%", "I wonder what's %*GREEN*%east%*RESET*%", "I wonder what's %*GREEN*%up%*RESET*%", "I wonder what's %*GREEN*%down%*RESET*%"],
                    },

                'Tower Middle': {
                    'room type': 'house',
                    'position': (2, 0, 0),
                    'descovered': False,
                    'directions': {
                        'down': 'Tower Bottom',
                        'up': 'Tower Top',
                        },
                    'containers': {
                        'stone': container([item('money-pouch', 'valuable', 25)], True),
                        },
                    'item': item('tome'),
                    'info': 'You are in the middle of a stone tower. The only light comes from above, through the cracks around the hatch to above.',
                    'map': '''
█████████
█      ╖█
█      ╖█
█       █
█       █
█       █
█╖      █
█╖      █
█████████''',
                    'Hints': [
                        'There might be an item here',
                    ],
                },

                'Tower Top' :{
                    'room type': 'house',
                    'position': (3, 0, 0),
                    'descovered': False,
                    'directions': {
                        'down': 'Tower Middle',
                        'teleport': 'Teleportation Deck',
                        },
                    'creatures stats': creature(
                        'greedy goblin',
                        5,
                        7,
                        [item('knife', 'weapon', 2), item('money-pouch', 'valuable', 5)],
                        'A 4ft 7 dirty and greedy goblin',
                        'A %*CYAN*%greedy goblin%*RESET*% spots you and your money pouch!',
                        creature_type('humanoid', 'goblin'),
                        ),
                    'info': 'You are at the top of a stone tower. There are windows in every wall',
                    'map': '''
█████████
█      ╖█
█      ╖█
█       █
█       █
█       █
█       █
█       █
█████████''',
                    'Hints': [
                        'I could %*GREEN*%teleport%*RESET*%',
                    ],
                },

                'Basement Armoury': {
                    'room type': 'house',
                    'position': (-1, 0, 0),
                    'descovered': False,
                    'directions': {
                        'south': 'Basement 3',
                        'east': 'Basement 1',
                        },
                    'item': item('torch'),
                    'containers': {
                        'rack-1': container([item('bow', 'weapon', 4)]),
                        'rack-2': container([item('spear', 'weapon', 3)]),
                        },
                    'info': 'You are in a dimly lit underground armoury (all the light in the room comes from 3 %*BLUE*%torch%*RESET*%es on the walls) with 2 racks full of damaged weapons,\n\
%*RED*%rack-1%*RESET*% has damaged bows and %*RED*%rack-2%*RESET*% has damaged spears.',
                    'map': '''
█████████
█╦      █
█      ╦█
█       █
█       ║
█       █
█       █
█       █
████║████''',
                    'Hints': [
                        'The things in %*RED*%rack-1%*RESET*% and %*RED*%rack-2%*RESET*% are salvigable',
                        "I wonder if I can get this %*BLUE*%torch%*RESET*% out of it's holder",
                    ],
                    },

                'Basement 1': {
                    'room type': 'house',
                    'position': (-1, 0, 8),
                    'descovered': False,
                    'directions': {
                        'south': 'Basement 2',
                        'west': 'Basement Armoury',
                        'up': 'Sitting Room',
                        },
                    'item': item('torch'),
                    'info': 'You are in an dimly lit underground (all the light in the room comes from 3 %*BLUE*%torch%*RESET*%es on the walls). You hear a %*YELLOW*%ripping%*RESET*% from the\
 stairs going %*GREEN*%up%*RESET*%.',
                    'map': '''
█████████
█      ╖█
█      ╖█
█       █
║       █
█       █
█       █
█       █
████║████''',
                    'Hints': [
                        "I wonder if I can get this %*BLUE*%torch%*RESET*% out of it's holder",
                    ],
                    },

                'Basement 2': {
                    'room type': 'house',
                    'position': (-1, 8, 8),
                    'descovered': False,
                    'directions': {
                        'north': 'Basement 1',
                        'west': 'Basement 3',
                        },
                    'item': item('torch'),
                    'info': 'You are in an dimly lit underground (all the light in the room comes from 3 %*BLUE*%torch%*RESET*%es on the walls).',
                    'map': '''
████║████
█       █
█       █
█       █
║       █
█       █
█       █
█       █
█████████''',
                    'Hints': [
                        "I wonder if I can get this %*BLUE*%torch%*RESET*% out of it's holder",
                    ],
                    },

                'Basement 3': {
                    'room type': 'house',
                    'position': (-1, 8, 0),
                    'descovered': False,
                    'directions': {
                        'south': 'Basement 4',
                        'east': 'Basement 2',
                        'north': 'Basement Armoury',
                        },
                    'item': item('torch'),
                    'info': 'You are in an dimly lit underground (all the light in the room comes from 3 %*BLUE*%torch%*RESET*%es on the walls).',
                    'map': '''
████║████
█       █
█       █
█       █
█       ║
█       █
█       █
█       █
████║████''',
                    'Hints': ['', '', '', ''],
                    },

                'Basement 4': {
                    'room type': 'house',
                    'position': (-1, 16, 0),
                    'descovered': False,
                    'directions': {
                        'north': 'Basement 3',
                        },
                    'item': item('torch'),
                    'info': 'You are in an dimly lit underground (all the light in the room comes from 3 %*BLUE*%torch%*RESET*%es on the walls).',
                    'map': '''
████║████
█       █
█       █
█       █
█       █
█       █
█       █
█       █
█████████''',
                    'Hints': [
                        "I wonder if I can get this %*BLUE*%torch%*RESET*% out of it's holder",
                    ],
                    },

                'Forest Clearing': {
                    'room type': 'forest',
                    'directions': {
                        'north': 'Forest Path1',
                        'east': 'Forest Path2',
                        'south': 'Forest Path1',
                        'west': 'Forest Path2',
                        },
                    'info': 'You are in a forest clearing outside the house.',
                    'map': '''
 ¥¥   ¥ ¥
¥     ¥  
 ¥     ¥¥
¥        
        ¥
       ¥¥
¥      ¥ 
 ¥   ¥¥  
  ¥  ¥   
         ''',
                    },

                'Forest Path1': {
                    'room type': 'forest',
                    'directions': {
                        'north': 'Forest Clearing',
                        'south': 'Forest Clearing',
                        },
                    'info': 'You are in a forest path outside the house.',
                    'map': '''
  ¥  ¥   
 ¥     ¥ 
¥       ¥
¥      ¥ 
¥     ¥  
¥     ¥  
 ¥¥    ¥¥
 ¥     ¥ 
 ¥¥   ¥ ¥
''',
                    },

                'Forest Path2': {
                    'room type': 'forest',
                    'directions': {
                        'east': 'Forest Clearing',
                        'west': 'Forest Clearing',
                        },
                    'info': 'You are in a forest path outside the house.',
                    'map': '''
¥¥¥¥¥  ¥ 
  ¥  ¥¥¥¥
¥¥  ¥  ¥¥
        ¥
¥¥       
¥¥¥¥¥    
  ¥  ¥¥¥¥
  ¥¥¥   ¥
 ¥   ¥¥¥ 
''',
                    },

                'Teleportation Deck': {
                    'room type': 'asteroid-1',
                    'directions': {
                        'teleport': 'Tower Top',
                        '0': 'Charter ship',
                        '1': 'The Dancing Jellyfish Inn',
                            '2': 'The Slopy Plasmoid Tapphouse',
                            '3': 'The Centaurbow Weapon Shop',
                            '4': 'The Gadabout Bakery',
                            '5': 'The Shifterspender St',
                            '6': 'The Town Hall',
                            '7': 'The Assassins Guild',
                            '8': 'The Watch Castle',
                            '9': 'The Old Manor',
                            },
                    'item': item('money-pouch', 'valuable', 10),
                    'info': '''
You are in a strange cave with many teleportation circles, as well as some ships that are floating above the floor.

Out of the gap in the side of the cave it looks black with a few twinkles of light.
There is a sign on the wall. It is a map of a city on an asteriod.
The main locations are: The Teleportation Deck, The Dancing Jellyfish Inn, The Slopy Plasmoid Tapphouse, The Centaurbow Weapon Shop, The Gadabout Bakery, The Shifterspender Store, 
The Town Hall, The Thieves Guild, The Watch Castle, and The Old Manor.

Do you want to:
%*GREEN*%0%*RESET*%. Charter a ship away (Costs 10 money).
%*GREEN*%1%*RESET*%. Go to The Dancing Jellyfish Inn.
%*GREEN*%2%*RESET*%. Go to The Slopy Plasmoid Tapphouse.
%*GREEN*%3%*RESET*%. Go to The Centaurbow Weapon Shop.
%*GREEN*%4%*RESET*%. Go to The Gadabout Bakery.
%*GREEN*%5%*RESET*%. Go to The Shifterspender St.
%*GREEN*%6%*RESET*%. Go to The Town Hall.
%*GREEN*%7%*RESET*%. Go to The Assassins Guild.
%*GREEN*%8%*RESET*%. Go to The Watch Castle.
%*GREEN*%9%*RESET*%. Go to The Old Manor.''',
                },

                'Charter ship' :{
                    'room type': 'asteroid-1',
                    'directions': {
                        '1': 'Teleportation Deck',
                        '2': 'The Dancing Jellyfish Inn',
                        '3': 'The Slopy Plasmoid Tapphouse',
                        '4': 'The Centaurbow Weapon Shop',
                        '5': 'The Gadabout Bakery',
                        '6': 'The Shifterspender St',
                        '7': 'The Town Hall',
                        '8': 'The Assassins Guild',
                        '9': 'The Watch Castle',
                        '10': 'The Old Manor',
                        '11': '2nd Teleportation Deck',
                        '12': '3rd Teleportation Deck',
                        },
                    'info': '''

You charter a ship, and the Captain says: "You can go anywhere you like before you land back on this here asteriod!"

Do you want to:
%*GREEN*%1%*RESET*%. Go to the Teleportation Deck.
%*GREEN*%2%*RESET*%. Go to The Dancing Jellyfish Inn.
%*GREEN*%3%*RESET*%. Go to The Slopy Plasmoid Tapphouse.
%*GREEN*%4%*RESET*%. Go to The Centaurbow Weapon Shop.
%*GREEN*%5%*RESET*%. Go to The Gadabout Bakery.
%*GREEN*%6%*RESET*%. Go to The Shifterspender St.
%*GREEN*%7%*RESET*%. Go to The Town Hall.
%*GREEN*%8%*RESET*%. Go to The Assassins Guild.
%*GREEN*%9%*RESET*%. Go to The Watch Castle.
%*GREEN*%10%*RESET*%. Go to The Old Manor.
%*GREEN*%11%*RESET*%. Go to The 2nd Asteriod.
%*GREEN*%12%*RESET*%. Go to The 3rd Asteriod.''',
                },

                'The Dancing Jellyfish Inn' :{
                    'room type': 'asteroid-1',
                    'directions': {
                        '1': 'Teleportation Deck',
                        '2': 'The Slopy Plasmoid Tapphouse',
                        '3': 'The Centaurbow Weapon Shop',
                        '4': 'The Gadabout Bakery',
                        '5': 'The Shifterspender St',
                        '6': 'The Town Hall',
                        '7': 'The Assassins Guild',
                        '8': 'The Watch Castle',
                        '9': 'The Old Manor',
                        },
                    'info': '''

do you want to:
%*GREEN*%1%*RESET*%. Go to the Teleportation Deck.
%*GREEN*%2%*RESET*%. Go to The Slopy Plasmoid Tapphouse.
%*GREEN*%3%*RESET*%. Go to The Centaurbow Weapon Shop.
%*GREEN*%4%*RESET*%. Go to The Gadabout Bakery.
%*GREEN*%5%*RESET*%. Go to The Shifterspender St.
%*GREEN*%6%*RESET*%. Go to The Town Hall.
%*GREEN*%7%*RESET*%. Go to The Assassins Guild.
%*GREEN*%8%*RESET*%. Go to The Watch Castle.
%*GREEN*%9%*RESET*%. Go to The Old Manor.''',
                },

                'The Slopy Plasmoid Tapphouse' :{
                    'room type': 'asteroid-1',
                    'directions': {
                        '1': 'Teleportation Deck',
                        '2': 'The Dancing Jellyfish Inn',
                        '3': 'The Centaurbow Weapon Shop',
                        '4': 'The Gadabout Bakery',
                        '5': 'The Shifterspender St',
                        '6': 'The Town Hall',
                        '7': 'The Assassins Guild',
                        '8': 'The Watch Castle',
                        '9': 'The Old Manor',
                        },
                    'info': '''

do you want to:
%*GREEN*%1%*RESET*%. Go to the Teleportation Deck.
%*GREEN*%2%*RESET*%. Go to The Dancing Jellyfish Inn.
%*GREEN*%3%*RESET*%. Go to The Centaurbow Weapon Shop.
%*GREEN*%4%*RESET*%. Go to The Gadabout Bakery.
%*GREEN*%5%*RESET*%. Go to The Shifterspender St.
%*GREEN*%6%*RESET*%. Go to The Town Hall.
%*GREEN*%7%*RESET*%. Go to The Assassins Guild.
%*GREEN*%8%*RESET*%. Go to The Watch Castle.
%*GREEN*%9%*RESET*%. Go to The Old Manor.''',
                },

                'The Centaurbow Weapon Shop' :{
                    'room type': 'asteroid-1',
                    'directions': {
                        '1': 'Teleportation Deck',
                        '2': 'The Dancing Jellyfish Inn',
                        '3': 'The Slopy Plasmoid Tapphouse',
                        '4': 'The Gadabout Bakery',
                        '5': 'The Shifterspender St',
                        '6': 'The Town Hall',
                        '7': 'The Assassins Guild',
                        '8': 'The Watch Castle',
                        '9': 'The Old Manor',
                        },
                    'info': '''

do you want to:
%*GREEN*%1%*RESET*%. Go to the Teleportation Deck.
%*GREEN*%2%*RESET*%. Go to The Dancing Jellyfish Inn.
%*GREEN*%3%*RESET*%. Go to The Slopy Plasmoid Tapphouse.
%*GREEN*%4%*RESET*%. Go to The Gadabout Bakery.
%*GREEN*%5%*RESET*%. Go to The Shifterspender St.
%*GREEN*%6%*RESET*%. Go to The Town Hall.
%*GREEN*%7%*RESET*%. Go to The Assassins Guild.
%*GREEN*%8%*RESET*%. Go to The Watch Castle.
%*GREEN*%9%*RESET*%. Go to The Old Manor.''',
                },

                'The Gadabout Bakery' :{
                    'room type': 'asteroid-1',
                    'directions': {
                        '1': 'Teleportation Deck',
                        '2': 'The Dancing Jellyfish Inn',
                        '3': 'The Slopy Plasmoid Tapphouse',
                        '4': 'The Centaurbow Weapon Shop',
                        '5': 'The Shifterspender St',
                        '6': 'The Town Hall',
                        '7': 'The Assassins Guild',
                        '8': 'The Watch Castle',
                        '9': 'The Old Manor',
                        },
                    'info': '''

do you want to:
%*GREEN*%1%*RESET*%. Go to the Teleportation Deck.
%*GREEN*%2%*RESET*%. Go to The Dancing Jellyfish Inn.
%*GREEN*%3%*RESET*%. Go to The Slopy Plasmoid Tapphouse.
%*GREEN*%4%*RESET*%. Go to The Centaurbow Weapon Shop.
%*GREEN*%5%*RESET*%. Go to The Shifterspender St.
%*GREEN*%6%*RESET*%. Go to The Town Hall.
%*GREEN*%7%*RESET*%. Go to The Assassins Guild.
%*GREEN*%8%*RESET*%. Go to The Watch Castle.
%*GREEN*%9%*RESET*%. Go to The Old Manor.''',
                },

                'The Shifterspender St' :{
                    'room type': 'asteroid-1',
                    'directions': {
                        '1': 'Teleportation Deck',
                        '2': 'The Dancing Jellyfish Inn',
                        '3': 'The Slopy Plasmoid Tapphouse',
                        '4': 'The Centaurbow Weapon Shop',
                        '5': 'The Gadabout Bakery',
                        '6': 'The Town Hall',
                        '7': 'The Assassins Guild',
                        '8': 'The Watch Castle',
                        '9': 'The Old Manor',
                        },
                    'info': '''

do you want to:
%*GREEN*%1%*RESET*%. Go to the Teleportation Deck.
%*GREEN*%2%*RESET*%. Go to The Dancing Jellyfish Inn.
%*GREEN*%3%*RESET*%. Go to The Slopy Plasmoid Tapphouse.
%*GREEN*%4%*RESET*%. Go to The Centaurbow Weapon Shop.
%*GREEN*%5%*RESET*%. Go to The Gadabout Bakery.
%*GREEN*%6%*RESET*%. Go to The Town Hall.
%*GREEN*%7%*RESET*%. Go to The Assassins Guild.
%*GREEN*%8%*RESET*%. Go to The Watch Castle.
%*GREEN*%9%*RESET*%. Go to The Old Manor.''',
                },

                'The Town Hall' :{
                    'room type': 'asteroid-1',
                    'directions': {
                        '1': 'Teleportation Deck',
                        '2': 'The Dancing Jellyfish Inn',
                        '3': 'The Slopy Plasmoid Tapphouse',
                        '4': 'The Centaurbow Weapon Shop',
                        '5': 'The Gadabout Bakery',
                        '6': 'The Shifterspender St',
                        '7': 'The Assassins Guild',
                        '8': 'The Watch Castle',
                        '9': 'The Old Manor',
                        },
                    'info': '''

do you want to:
%*GREEN*%1%*RESET*%. Go to the Teleportation Deck.
%*GREEN*%2%*RESET*%. Go to The Dancing Jellyfish Inn.
%*GREEN*%3%*RESET*%. Go to The Slopy Plasmoid Tapphouse.
%*GREEN*%4%*RESET*%. Go to The Centaurbow Weapon Shop.
%*GREEN*%5%*RESET*%. Go to The Gadabout Bakery.
%*GREEN*%6%*RESET*%. Go to The Shifterspender St.
%*GREEN*%7%*RESET*%. Go to The Assassins Guild.
%*GREEN*%8%*RESET*%. Go to The Watch Castle.
%*GREEN*%9%*RESET*%. Go to The Old Manor.''',
                },

                'The Assassins Guild' :{
                    'room type': 'asteroid-1',
                    'directions': {
                        '1': 'Teleportation Deck',
                        '2': 'The Dancing Jellyfish Inn',
                        '3': 'The Slopy Plasmoid Tapphouse',
                        '4': 'The Centaurbow Weapon Shop',
                        '5': 'The Gadabout Bakery',
                        '6': 'The Shifterspender St',
                        '7': 'The Town Hall',
                        '8': 'The Watch Castle',
                        '9': 'The Old Manor',
                        },
                    'info': ''',

do you want to:
%*GREEN*%1%*RESET*%. Go to the Teleportation Deck.
%*GREEN*%2%*RESET*%. Go to The Dancing Jellyfish Inn.
%*GREEN*%3%*RESET*%. Go to The Slopy Plasmoid Tapphouse.
%*GREEN*%4%*RESET*%. Go to The Centaurbow Weapon Shop.
%*GREEN*%5%*RESET*%. Go to The Gadabout Bakery.
%*GREEN*%6%*RESET*%. Go to The Shifterspender St.
%*GREEN*%7%*RESET*%. Go to The Town Hall.
%*GREEN*%8%*RESET*%. Go to The Watch Castle.
%*GREEN*%9%*RESET*%. Go to The Old Manor.'''
                },

                'The Watch Castle' :{
                    'room type': 'asteroid-1',
                    'directions': {
                        '1': 'Teleportation Deck',
                        '2': 'The Dancing Jellyfish Inn',
                        '3': 'The Slopy Plasmoid Tapphouse',
                        '4': 'The Centaurbow Weapon Shop',
                        '5': 'The Gadabout Bakery',
                        '6': 'The Shifterspender St',
                        '7': 'The Town Hall',
                        '8': 'The Assassins Guild',
                        '9': 'The Old Manor',
                        },
                    'info': '''

do you want to:
%*GREEN*%1%*RESET*%. Go to the Teleportation Deck.
%*GREEN*%2%*RESET*%. Go to The Dancing Jellyfish Inn.
%*GREEN*%3%*RESET*%. Go to The Slopy Plasmoid Tapphouse.
%*GREEN*%4%*RESET*%. Go to The Centaurbow Weapon Shop.
%*GREEN*%5%*RESET*%. Go to The Gadabout Bakery.
%*GREEN*%6%*RESET*%. Go to The Shifterspender St.
%*GREEN*%7%*RESET*%. Go to The Town Hall.
%*GREEN*%8%*RESET*%. Go to The Assassins Guild.
%*GREEN*%9%*RESET*%. Go to The Old Manor.''',
                },

                'The Old Manor' :{
                    'room type': 'asteroid-1',
                    'directions': {
                        '1': 'Teleportation Deck',
                        '2': 'The Dancing Jellyfish Inn',
                        '3': 'The Slopy Plasmoid Tapphouse',
                        '4': 'The Centaurbow Weapon Shop',
                        '5': 'The Gadabout Bakery',
                        '6': 'The Shifterspender St',
                        '7': 'The Town Hall',
                        '8': 'The Assassins Guild',
                        '9': 'The Watch Castle',
                        },
                    'info': '''

do you want to:
%*GREEN*%1%*RESET*%. Go to the Teleportation Deck.
%*GREEN*%2%*RESET*%. Go to The Dancing Jellyfish Inn.
%*GREEN*%3%*RESET*%. Go to The Slopy Plasmoid Tapphouse.
%*GREEN*%4%*RESET*%. Go to The Centaurbow Weapon Shop.
%*GREEN*%5%*RESET*%. Go to The Gadabout Bakery.
%*GREEN*%6%*RESET*%. Go to The Shifterspender St.
%*GREEN*%7%*RESET*%. Go to The Town Hall.
%*GREEN*%8%*RESET*%. Go to The Assassins Guild.
%*GREEN*%9%*RESET*%. Go to The Watch Castle.''',
                },

                '2nd Teleportation Deck': {
                    'room type': 'asteroid-2',
                    'directions': {
                        '1': 'Charter 2nd Ship',
                        '2': 'The 2nd Dancing Jellyfish Inn',
                        '3': 'The 2nd Slopy Plasmoid Tapphouse',
                        '4': 'The 2nd GiffHammer Weapon Shop',
                        '5': 'The 2nd Gadabout Bakery',
                        '6': 'The 2nd Githspender St',
                        '7': 'The 2nd Town Hall',
                        '8': 'The 2nd Thieves Guild',
                        '9': 'The 2nd Watch Castle',
                        },
                        '10': 'The 2nd Old Manor',
                    'info': '''
You are in a strange cave with many teleportation circles, as well as some ships that are floating above the floor.

Out of the gap in the side of the cave it looks black with a few twinkles of light.
There is a sign on the wall. It is a map of a city on an asteriod.
The main locations are: The Teleportation Deck, The Dancing Jellyfish Inn, The Slopy Plasmoid Tapphouse, The GiffHammer Weapon Shop, The Gadabout Bakery, The Githspender Store,
The Town Hall, The Thieves Guild, The Watch Castle, and The Old Manor.
do you want to:
%*GREEN*%1%*RESET*%. Charter a ship away.
%*GREEN*%2%*RESET*%. Go to The Dancing Jellyfish Inn.
%*GREEN*%3%*RESET*%. Go to The Slopy Plasmoid Tapphouse.
%*GREEN*%4%*RESET*%. Go to The Giffhammer Weapon Shop.
%*GREEN*%5%*RESET*%. Go to The Gadabout Bakery.
%*GREEN*%6%*RESET*%. Go to The Githspender St.
%*GREEN*%7%*RESET*%. Go to The Town Hall.
%*GREEN*%8%*RESET*%. Go to The Thieves Guild.
%*GREEN*%9%*RESET*%. Go to The Watch Castle.
%*GREEN*%10%*RESET*%. Go to The Old Manor.''',
                },

                'Charter 2nd Ship' :{
                    'room type': 'asteroid-2',
                    'directions': {
                        '1': '2nd Teleportation Deck',
                        '2': 'The 2nd Dancing Jellyfish Inn',
                        '3': 'The 2nd Slopy Plasmoid Tapphouse',
                        '4': 'The 2nd GiffHammer Weapon Shop',
                        '5': 'The 2nd Gadabout Bakery',
                        '6': 'The 2nd Githspender St',
                        '7': 'The 2nd Town Hall',
                        '8': 'The 2nd Thieves Guild',
                        '9': 'The 2nd Watch Castle',
                        '10': 'The Old 2nd Manor',
                        '11': 'Teleportation Deck',
                        '12': '3rd Teleportation Deck',
                        },
                    'creatures stats': creature(
                        'hull leech', 
                        15, 
                        2, 
                        [item('spike', 'weapon', 1)],
                        'A barnacle-like creature that is attached to the hull of the ship',
                        'You see a spike on a tentacle stabed through the hull of the ship',
                        creature_type('plant'),
                        ),
                    'info': '''

You charter a ship, and the Captain says: "You can go anywhere you like before you land back on this here asteriod!"

Do you want to:
%*GREEN*%1%*RESET*%. Go to the Teleportation Deck.
%*GREEN*%2%*RESET*%. Go to The Dancing Jellyfish Inn.
%*GREEN*%3%*RESET*%. Go to The Slopy Plasmoid Tapphouse.
%*GREEN*%4%*RESET*%. Go to The GiffHammer Weapon Shop.
%*GREEN*%5%*RESET*%. Go to The Gadabout Bakery.
%*GREEN*%6%*RESET*%. Go to The Githspender St.
%*GREEN*%7%*RESET*%. Go to The Town Hall.
%*GREEN*%8%*RESET*%. Go to The Thieves Guild.
%*GREEN*%9%*RESET*%. Go to The Watch Castle.
%*GREEN*%10%*RESET*%. Go to The Old Manor.
%*GREEN*%11%*RESET*%. Go to The 1st Asteriod.
%*GREEN*%12%*RESET*%. Go to The 3rd Asteriod.''',
                },

                'The 2nd Dancing Jellyfish Inn' :{
                    'room type': 'asteroid-2',
                    'directions': {
                        '1': '2nd Teleportation Deck',
                        '2': 'The 2nd Slopy Plasmoid Tapphouse',
                        '3': 'The 2nd GiffHammer Weapon Shop',
                        '4': 'The 2nd Gadabout Bakery',
                        '5': 'The 2nd Githspender St',
                        '6': 'The 2nd Town Hall',
                        '7': 'The 2nd Thieves Guild',
                        '8': 'The 2nd Watch Castle',
                        '9': 'The 2nd Old Manor',
                        },
                    'info': '''

do you want to:
%*GREEN*%1%*RESET*%. Go to the Teleportation Deck.
%*GREEN*%2%*RESET*%. Go to The Slopy Plasmoid Tapphouse.
%*GREEN*%3%*RESET*%. Go to The GiffHammer Weapon Shop.
%*GREEN*%4%*RESET*%. Go to The Gadabout Bakery.
%*GREEN*%5%*RESET*%. Go to The Shifterspender St.
%*GREEN*%6%*RESET*%. Go to The Town Hall.
%*GREEN*%7%*RESET*%. Go to The Thieves Guild.
%*GREEN*%8%*RESET*%. Go to The Watch Castle.
%*GREEN*%9%*RESET*%. Go to The Old Manor.''',
                },

                'The 2nd Slopy Plasmoid Tapphouse' :{
                    'room type': 'asteroid-2',
                    'directions': {
                        '1': '2nd Teleportation Deck',
                        '2': 'The 2nd Dancing Jellyfish Inn',
                        '3': 'The 2nd GiffHammer Weapon Shop',
                        '4': 'The 2nd Gadabout Bakery',
                        '5': 'The 2nd Githspender St',
                        '6': 'The 2nd Town Hall',
                        '7': 'The 2nd Thieves Guild',
                        '8': 'The 2nd Watch Castle',
                        '9': 'The 2nd Old Manor',
                        },
                    'info': '''

do you want to:
%*GREEN*%1%*RESET*%. Go to the Teleportation Deck.
%*GREEN*%2%*RESET*%. Go to The Dancing Jellyfish Inn.
%*GREEN*%3%*RESET*%. Go to The GiffHammer Weapon Shop.
%*GREEN*%4%*RESET*%. Go to The Gadabout Bakery.
%*GREEN*%5%*RESET*%. Go to The Githspender St.
%*GREEN*%6%*RESET*%. Go to The Town Hall.
%*GREEN*%7%*RESET*%. Go to The Thieves Guild.
%*GREEN*%8%*RESET*%. Go to The Watch Castle.
%*GREEN*%9%*RESET*%. Go to The Old Manor.''',
                },

                'The 2nd GiffHammer Weapon Shop' :{
                    'room type': 'asteroid-2',
                    'directions': {
                        '1': '2nd Teleportation Deck',
                        '2': 'The 2nd Dancing Jellyfish Inn',
                        '3': 'The 2nd Slopy Plasmoid Tapphouse',
                        '4': 'The 2nd Gadabout Bakery',
                        '5': 'The 2nd Githspender St',
                        '6': 'The 2nd Town Hall',
                        '7': 'The 2nd Thieves Guild',
                        '8': 'The 2nd Watch Castle',
                        '9': 'The 2nd Old Manor',
                        },
                    'info': '''

do you want to:
%*GREEN*%1%*RESET*%. Go to the Teleportation Deck.
%*GREEN*%2%*RESET*%. Go to The Dancing Jellyfish Inn.
%*GREEN*%3%*RESET*%. Go to The Slopy Plasmoid Tapphouse.
%*GREEN*%4%*RESET*%. Go to The Gadabout Bakery.
%*GREEN*%5%*RESET*%. Go to The Githspender St.
%*GREEN*%6%*RESET*%. Go to The Town Hall.
%*GREEN*%7%*RESET*%. Go to The Thieves Guild.
%*GREEN*%8%*RESET*%. Go to The Watch Castle.
%*GREEN*%9%*RESET*%. Go to The Old Manor.''',
                },

                'The 2nd Gadabout Bakery' :{
                    'room type': 'asteroid-2',
                    'directions': {
                        '1': '2nd Teleportation Deck',
                        '2': 'The 2nd Dancing Jellyfish Inn',
                        '3': 'The 2nd Slopy Plasmoid Tapphouse',
                        '4': 'The 2nd GiffHammer Weapon Shop',
                        '5': 'The 2nd Githspender St',
                        '6': 'The 2nd Town Hall',
                        '7': 'The 2nd Thieves Guild',
                        '8': 'The 2nd Watch Castle',
                        '9': 'The 2nd Old Manor',
                        },
                    'info': '''

do you want to:
%*GREEN*%1%*RESET*%. Go to the Teleportation Deck.
%*GREEN*%2%*RESET*%. Go to The Dancing Jellyfish Inn.
%*GREEN*%3%*RESET*%. Go to The Slopy Plasmoid Tapphouse.
%*GREEN*%4%*RESET*%. Go to The GiffHammer Weapon Shop.
%*GREEN*%5%*RESET*%. Go to The Githspender St.
%*GREEN*%6%*RESET*%. Go to The Town Hall.
%*GREEN*%7%*RESET*%. Go to The Thieves Guild.
%*GREEN*%8%*RESET*%. Go to The Watch Castle.
%*GREEN*%9%*RESET*%. Go to The Old Manor.''',
                },

                'The 2nd Githspender St' :{
                    'room type': 'asteroid-2',
                    'directions': {
                        '1': '2nd Teleportation Deck',
                        '2': 'The 2nd Dancing Jellyfish Inn',
                        '3': 'The 2nd Slopy Plasmoid Tapphouse',
                        '4': 'The 2nd GiffHammer Weapon Shop',
                        '5': 'The 2nd Gadabout Bakery',
                        '6': 'The 2nd Town Hall',
                        '7': 'The 2nd Thieves Guild',
                        '8': 'The 2nd Watch Castle',
                        '9': 'The 2nd Old Manor',
                        },
                    'info': '''

do you want to:
%*GREEN*%1%*RESET*%. Go to the Teleportation Deck.
%*GREEN*%2%*RESET*%. Go to The Dancing Jellyfish Inn.
%*GREEN*%3%*RESET*%. Go to The Slopy Plasmoid Tapphouse.
%*GREEN*%4%*RESET*%. Go to The GiffHammer Weapon Shop.
%*GREEN*%5%*RESET*%. Go to The Gadabout Bakery.
%*GREEN*%6%*RESET*%. Go to The Town Hall.
%*GREEN*%7%*RESET*%. Go to The Thieves Guild.
%*GREEN*%8%*RESET*%. Go to The Watch Castle.
%*GREEN*%9%*RESET*%. Go to The Old Manor.''',
                },

                'The 2nd Town Hall' :{
                    'room type': 'asteroid-2',
                    'directions': {
                        '1': '2nd Teleportation Deck',
                        '2': 'The 2nd Dancing Jellyfish Inn',
                        '3': 'The 2nd Slopy Plasmoid Tapphouse',
                        '4': 'The 2nd GiffHammer Weapon Shop',
                        '5': 'The 2nd Gadabout Bakery',
                        '6': 'The 2nd Githspender St',
                        '7': 'The 2nd Thieves Guild',
                        '8': 'The 2nd Watch Castle',
                        '9': 'The 2nd Old Manor',
                        },
                    'info': '''

do you want to:
%*GREEN*%1%*RESET*%. Go to the Teleportation Deck.
%*GREEN*%2%*RESET*%. Go to The Dancing Jellyfish Inn.
%*GREEN*%3%*RESET*%. Go to The Slopy Plasmoid Tapphouse.
%*GREEN*%4%*RESET*%. Go to The GiffHammer Weapon Shop.
%*GREEN*%5%*RESET*%. Go to The Gadabout Bakery.
%*GREEN*%6%*RESET*%. Go to The Githspender St.
%*GREEN*%7%*RESET*%. Go to The Thieves Guild.
%*GREEN*%8%*RESET*%. Go to The Watch Castle.
%*GREEN*%9%*RESET*%. Go to The Old Manor.''',
                },

                'The 2nd Thieves Guild' :{
                    'room type': 'asteroid-2',
                    'directions': {
                        '1': '2nd Teleportation Deck',
                        '2': 'The 2nd Dancing Jellyfish Inn',
                        '3': 'The 2nd Slopy Plasmoid Tapphouse',
                        '4': 'The 2nd GiffHammer Weapon Shop',
                        '5': 'The 2nd Gadabout Bakery',
                        '6': 'The 2nd Githspender St',
                        '7': 'The 2nd Town Hall',
                        '8': 'The 2nd Watch Castle',
                        '9': 'The 2nd Old Manor',
                        },
                    'creatures stats': creature(
                        'thief', 
                        10, 
                        4, 
                        [item('knife', 'weapon', 2), item('money-pouch', 'valuable', 25)],
                        'A hooded 5ft 11 humanoid thief, thief level 3',
                        'You see a %*CYAN*%thief%*RESET*% at the door',
                        creature_type('humanoid', 'cowfolk'),
                        ),
                    'info': '''

do you want to:
%*GREEN*%1%*RESET*%. Go to the Teleportation Deck.
%*GREEN*%2%*RESET*%. Go to The Dancing Jellyfish Inn.
%*GREEN*%3%*RESET*%. Go to The Slopy Plasmoid Tapphouse.
%*GREEN*%4%*RESET*%. Go to The GiffHammer Weapon Shop.
%*GREEN*%5%*RESET*%. Go to The Gadabout Bakery.
%*GREEN*%6%*RESET*%. Go to The Githspender St.
%*GREEN*%7%*RESET*%. Go to The Town Hall.
%*GREEN*%8%*RESET*%. Go to The Watch Castle.
%*GREEN*%9%*RESET*%. Go to The Old Manor.''',
                },

                'The 2nd Watch Castle' :{
                    'room type': 'asteroid-2',
                    'directions': {
                        '1': '2nd Teleportation Deck',
                        '2': 'The 2nd Dancing Jellyfish Inn',
                        '3': 'The 2nd Slopy Plasmoid Tapphouse',
                        '4': 'The 2nd GiffHammer Weapon Shop',
                        '5': 'The 2nd Gadabout Bakery',
                        '6': 'The 2nd Githspender St',
                        '7': 'The 2nd Town Hall',
                        '8': 'The 2nd Thieves Guild',
                        '9': 'The 2nd Old Manor',
                        },
                    'info': '''

do you want to:
%*GREEN*%1%*RESET*%. Go to the Teleportation Deck.
%*GREEN*%2%*RESET*%. Go to The Dancing Jellyfish Inn.
%*GREEN*%3%*RESET*%. Go to The Slopy Plasmoid Tapphouse.
%*GREEN*%4%*RESET*%. Go to The GiffHammer Weapon Shop.
%*GREEN*%5%*RESET*%. Go to The Gadabout Bakery.
%*GREEN*%6%*RESET*%. Go to The Githspender St.
%*GREEN*%7%*RESET*%. Go to The Town Hall.
%*GREEN*%8%*RESET*%. Go to The Thieves Guild.
%*GREEN*%9%*RESET*%. Go to The Old Manor.''',
                },

                'The 2nd Old Manor' :{
                    'room type': 'asteroid-2',
                    'directions': {
                        '1': '2nd Teleportation Deck',
                        '2': 'The 2nd Dancing Jellyfish Inn',
                        '3': 'The 2nd Slopy Plasmoid Tapphouse',
                        '4': 'The 2nd GiffHammer Weapon Shop',
                        '5': 'The 2nd Gadabout Bakery',
                        '6': 'The 2nd Githspender St',
                        '7': 'The 2nd Town Hall',
                        '8': 'The 2nd Thieves Guild',
                        '9': 'The 2nd Watch Castle',
                        },
                    'info': '''

do you want to:
%*GREEN*%1%*RESET*%. Go to the Teleportation Deck.
%*GREEN*%2%*RESET*%. Go to The Dancing Jellyfish Inn.
%*GREEN*%3%*RESET*%. Go to The Slopy Plasmoid Tapphouse.
%*GREEN*%4%*RESET*%. Go to The GiffHammer Weapon Shop.
%*GREEN*%5%*RESET*%. Go to The Gadabout Bakery.
%*GREEN*%6%*RESET*%. Go to The Githspender St.
%*GREEN*%7%*RESET*%. Go to The Town Hall.
%*GREEN*%8%*RESET*%. Go to The Thieves Guild.
%*GREEN*%9%*RESET*%. Go to The Watch Castle.''',
                },

                '3rd Teleportation Deck': {
                    'room type': 'asteroid-2',
                    'directions': {
                        '1': 'Charter 3rd Ship',
                        '2': 'The Main Guildhall',
                        '3': 'The Order of the Arcane Scribes',
                        '4': 'The Wayfarers\' Brotherhood',
                        '5': 'The Artisans\' Collective',
                        '6': 'The Silent Shadows Syndicate',
                        '7': 'The Guardians of the Wilds',
                        '8': 'The Mercantile Consortium',
                        '9': 'The Sentinels of the Shield',
                        },
                        '10': 'The 3rd Old Manor',
                    'info': '''
You are in a strange cave with many teleportation circles, as well as some ships that are floating above the floor.

Out of the gap in the side of the cave it looks black with a few twinkles of light.
There is a sign on the wall. It is a map of a city on an asteriod.
The main locations are: The Teleportation Deck, The Dancing Jellyfish Inn, The Slopy Plasmoid Tapphouse, The GiffHammer Weapon Shop, The Gadabout Bakery, The Githspender Store,
The Town Hall, The Thieves Guild, The Watch Castle, and The Old Manor.
do you want to:
%*GREEN*%1%*RESET*%. Charter a ship away.
%*GREEN*%2%*RESET*%. Go to The Main Guildhall.
%*GREEN*%3%*RESET*%. Go to The Magic Guild.
%*GREEN*%4%*RESET*%. Go to The Explorers' Guild.
%*GREEN*%5%*RESET*%. Go to The Craftsmen's Guild.
%*GREEN*%6%*RESET*%. Go to The Stealth Guild.
%*GREEN*%7%*RESET*%. Go to The Nature Guild.
%*GREEN*%8%*RESET*%. Go to The Trade Guild.
%*GREEN*%9%*RESET*%. Go to The Watch Castle.
%*GREEN*%10%*RESET*%. Go to The Old Manor.''',
                },

                'Charter 3rd Ship' :{
                    'room type': 'asteroid-3',
                    'directions': {
                        '1': 'Teleportation Deck',
                        '2': 'The Main Guildhall',
                        '3': 'The Order of the Arcane Scribes',
                        '4': 'The Wayfarers\' Brotherhood',
                        '5': 'The Artisans\' Collective',
                        '6': 'The Silent Shadows Syndicate',
                        '7': 'The Guardians of the Wilds',
                        '8': 'The Mercantile Consortium',
                        '9': 'The Sentinels of the Shield',
                        '10': 'The 3rd Old Manor',
                        '11': 'Teleportation Deck',
                        '12': '2nd Teleportation Deck',
                        },
                    'info': '''

You charter a ship, and the Captain says: "You can go anywhere you like before you land back on this here asteriod!"

Do you want to:
%*GREEN*%1%*RESET*%. Go to The Teleportation Deck.
%*GREEN*%2%*RESET*%. Go to The Main Guildhall.
%*GREEN*%3%*RESET*%. Go to The Magic Guild.
%*GREEN*%4%*RESET*%. Go to The Explorers' Guild.
%*GREEN*%5%*RESET*%. Go to The Craftsmen's Guild.
%*GREEN*%6%*RESET*%. Go to The Stealth Guild.
%*GREEN*%7%*RESET*%. Go to The Nature Guild.
%*GREEN*%8%*RESET*%. Go to The Trade Guild.
%*GREEN*%9%*RESET*%. Go to The Guards Guild.
%*GREEN*%10%*RESET*%. Go to The Old Manor.
%*GREEN*%11%*RESET*%. Go to The 1st Asteriod.
%*GREEN*%12%*RESET*%. Go to The 2nd Asteriod.''',
                },

                'The Main Guildhall' :{
                    'description': '''
The Forge of Heroes

Theme: Valor and Heroism
Purpose: The Forge of Heroes is a legendary guildhall dedicated to the training, inspiration, and celebration of heroes. Its towering spires and majestic architecture evoke a sense of awe and 
reverence, inspiring all who enter to aspire to greatness. Within its hallowed halls, aspiring adventurers undergo rigorous training regimes, learning the arts of combat, leadership, and 
selflessness under the guidance of seasoned mentors and legendary champions. In addition to training, the Forge also serves as a repository of heroic deeds, with its walls adorned with 
tapestries, statues, and artifacts commemorating the triumphs of the past. Whether preparing for epic quests, honing their skills in the arena, or seeking guidance from wise sages, heroes 
from across the realm flock to the Forge, drawn by the promise of glory and the chance to make their mark on history.''',
                    'room type': 'asteroid-3',
                    'directions': {
                        '1': '2nd Teleportation Deck',
                        '2': 'The Order of the Arcane Scribes',
                        '3': 'The Wayfarers\' Brotherhood',
                        '4': 'The Artisans\' Collective',
                        '5': 'The Silent Shadows Syndicate',
                        '6': 'The Guardians of the Wilds',
                        '7': 'The Mercantile Consortium',
                        '8': 'The Sentinels of the Shield',
                        '9': 'The 3rd Old Manor',
                        '10': 'The Grand Coliseum',
                        },
                    'info': '''

do you want to:
%*GREEN*%1%*RESET*%. Go to The Teleportation Deck.
%*GREEN*%2%*RESET*%. Go to The Magic Guild.
%*GREEN*%3%*RESET*%. Go to The Explorers' Guild.
%*GREEN*%4%*RESET*%. Go to The Craftsmen's Guild.
%*GREEN*%5%*RESET*%. Go to The Stealth Guild.
%*GREEN*%6%*RESET*%. Go to The Nature Guild.
%*GREEN*%7%*RESET*%. Go to The Trade Guild.
%*GREEN*%8%*RESET*%. Go to The Guards Guild.
%*GREEN*%9%*RESET*%. Go to The Old Manor.
%*GREEN*%10%*RESET*%. Go to The Arena''',
                },

                'The Grand Coliseum' :{
                    'description': '''
The Grand Coliseum

Theme: Gladiatorial Combat and Spectacle
Purpose: The Grand Coliseum is an ancient and revered arena where warriors from across the realm come to test their mettle in epic battles of skill and strength. Its towering walls and 
majestic architecture evoke the grandeur of a bygone era, harkening back to a time when gladiators fought for glory and the adulation of the masses. Within its vast amphitheater, spectators 
from all walks of life gather to witness the spectacle of combat, cheering on their favorite champions and reveling in the excitement of the arena. But the Grand Coliseum is more than just a 
venue for bloodsport—it is a symbol of honor, valor, and the indomitable spirit of competition. Warriors who prove themselves in the crucible of the arena earn not only fame and fortune but 
also the respect of their peers and the adoration of the crowds. Whether battling for supremacy in one-on-one duels, facing off against fearsome beasts in savage contests, or participating in 
elaborate tournaments of skill and strategy, the fighters of the Grand Coliseum embody the virtues of courage, determination, and resilience. As the premier arena of its kind, the Grand 
Coliseum stands as a testament to the enduring appeal of gladiatorial combat and the timeless allure of the warrior's path.''',
                    'room type': 'asteroid-3',
                    'directions': {
                        '1': 'The Main Guildhall',
                        },
                    'creatures stats': creature(
                        'gladiator',
                        15,
                        6,
                        [item('longsword', 'weapon', 4)],
                        'A large 6ft 7 humaniod gladiator',
                        'As you enter the Arena a hulking %*CYAN*%gladiator%*RESET*% walks up to you and says: "You sould run while you still can or face me!"',
                        creature_type('humaniod', 'goliath'),
                    ),
                    'info': '''

do you want to:
%*GREEN*%1%*RESET*%. Go to The The Main Guildhall.''',
                },

                'The Order of the Arcane Scribes' :{
                    'description': '''
Order of the Arcane Scribes

Theme: Magic and Knowledge
Purpose: The Order of the Arcane Scribes is a venerable guild steeped in the mysteries of magic and the pursuit of knowledge. Comprised of wizards, scholars, and scribes, their primary mission
is the preservation, study, and advancement of the arcane arts. Within their ancient guildhall, which stands as a testament to centuries of magical scholarship, members pore over ancient 
tomes, decipher cryptic runes, and experiment with new spells. Their work encompasses a wide range of magical disciplines, from elemental manipulation to divination and healing magic. Beyond 
their scholarly pursuits, the Order also offers magical services to the community, providing everything from enchantments and potion brewing to mystical consultations and magical education. 
Whether delving into the depths of forgotten lore or harnessing the power of the elements, the Arcane Scribes are dedicated to unraveling the secrets of the cosmos and mastering the forces of 
magic.''',
                    'room type': 'asteroid-3',
                    'directions': {
                        '1': '3rd Teleportation Deck',
                        '2': 'The Main Guildhall',
                        '3': 'The Wayfarers\' Brotherhood',
                        '4': 'The Artisans\' Collective',
                        '5': 'The Silent Shadows Syndicate',
                        '6': 'The Guardians of the Wilds',
                        '7': 'The Mercantile Consortium',
                        '8': 'The Sentinels of the Shield',
                        '9': 'The 3rd Old Manor',
                        },
                    'info': '''

do you want to:
%*GREEN*%1%*RESET*%. Go to the Teleportation Deck.
%*GREEN*%2%*RESET*%. Go to The Main Guildhall.
%*GREEN*%3%*RESET*%. Go to The Explorers' Guild.
%*GREEN*%4%*RESET*%. Go to The Craftsmen's Guild.
%*GREEN*%5%*RESET*%. Go to The Stealth Guild.
%*GREEN*%6%*RESET*%. Go to The Nature Guild.
%*GREEN*%7%*RESET*%. Go to The Trade Guild.
%*GREEN*%8%*RESET*%. Go to The Guards Guild.
%*GREEN*%9%*RESET*%. Go to The Old Manor.''',
                },

                'The Wayfarers\' Brotherhood' :{
                    'description': '''
Wayfarers' Brotherhood

Theme: Exploration and Adventure
Purpose: The Wayfarers' Brotherhood is a renowned guild of intrepid adventurers, explorers, and seekers of the unknown. Theirs is a life dedicated to the thrill of discovery, the pursuit of 
treasure, and the exploration of uncharted realms. From the towering peaks of distant mountains to the depths of forgotten dungeons, members of the Wayfarers' Brotherhood traverse the world in 
search of adventure and fortune. Their guildhall, a bustling hub of activity and excitement, serves as a meeting place for like-minded individuals to share tales of daring exploits, plan 
ambitious expeditions, and seek companions for their journeys. Guided by a spirit of curiosity and a thirst for discovery, the Wayfarers embody the adventurous spirit of exploration, ever 
eager to uncover the mysteries that lie beyond the horizon.''',
                    'room type': 'asteroid-3',
                    'directions': {
                        '1': '3rd Teleportation Deck',
                        '2': 'The Main Guildhall',
                        '3': 'The Order of the Arcane Scribes',
                        '4': 'The Artisans\' Collective',
                        '5': 'The Silent Shadows Syndicate',
                        '6': 'The Guardians of the Wilds',
                        '7': 'The Mercantile Consortium',
                        '8': 'The Sentinels of the Shield',
                        '9': 'The 3rd Old Manor',
                        },
                    'info': '''

do you want to:
%*GREEN*%1%*RESET*%. Go to the Teleportation Deck.
%*GREEN*%2%*RESET*%. Go to The Main Guildhall.
%*GREEN*%3%*RESET*%. Go to The Magic Guild.
%*GREEN*%4%*RESET*%. Go to The Craftsmen's Guild.
%*GREEN*%5%*RESET*%. Go to The Stealth Guild.
%*GREEN*%6%*RESET*%. Go to The Nature Guild.
%*GREEN*%7%*RESET*%. Go to The Trade Guild.
%*GREEN*%8%*RESET*%. Go to The Guards Guild.
%*GREEN*%9%*RESET*%. Go to The Old Manor.''',
                },

                'The Artisans\' Collective' :{
                    'description': '''
Artisans' Collective

Theme: Craftsmanship and Creativity
Purpose: The Artisans' Collective is a guild dedicated to the celebration of craftsmanship, creativity, and the pursuit of artistic excellence. Within their bustling guildhall, master 
artisans, craftsmen, and artists of all disciplines gather to hone their skills, showcase their creations, and inspire one another with their passion for their craft. From the ringing of 
anvils in the blacksmith's forge to the delicate brushstrokes of the painter's canvas, members of the Artisans' Collective excel in a diverse array of trades and artistic endeavors. Their 
guildhall doubles as a vibrant workshop and gallery, where members collaborate on projects, share techniques, and exhibit their finest works to the public. Whether forging weapons of legendary 
quality, crafting intricate works of jewelry, or painting breathtaking landscapes, the Artisans' Collective stands as a testament to the enduring power of creativity and the transformative 
potential of skilled craftsmanship.''',
                    'room type': 'asteroid-3',
                    'directions': {
                        '1': '3rd Teleportation Deck',
                        '2': 'The Main Guildhall',
                        '3': 'The Order of the Arcane Scribes',
                        '4': 'The Wayfarers\' Brotherhood',
                        '5': 'The Silent Shadows Syndicate',
                        '6': 'The Guardians of the Wilds',
                        '7': 'The Mercantile Consortium',
                        '8': 'The Sentinels of the Shield',
                        '9': 'The 3rd Old Manor',
                        },
                    'info': '''

do you want to:
%*GREEN*%1%*RESET*%. Go to the Teleportation Deck.
%*GREEN*%2%*RESET*%. Go to The Main Guildhall.
%*GREEN*%3%*RESET*%. Go to The Magic Guild.
%*GREEN*%4%*RESET*%. Go to The Explorers' Guild.
%*GREEN*%5%*RESET*%. Go to The Stealth Guild.
%*GREEN*%6%*RESET*%. Go to The Nature Guild.
%*GREEN*%7%*RESET*%. Go to The Trade Guild.
%*GREEN*%8%*RESET*%. Go to The Guards Guild.
%*GREEN*%9%*RESET*%. Go to The Old Manor.''',
                },

                'The Silent Shadows Syndicate' :{
                    'description': '''
Silent Shadows Syndicate

Theme: Stealth and Subterfuge
Purpose: Operating from the shadows, the Silent Shadows Syndicate is a clandestine guild of spies, thieves, and assassins who specialize in the arts of stealth, subterfuge, and infiltration. 
Their clandestine operations span the realms of espionage, sabotage, and intelligence gathering, making them a formidable force in the world of intrigue. Within their secretive guildhall, 
concealed from prying eyes and hidden from public view, members of the Syndicate plot and scheme, carrying out covert missions on behalf of their clients or furthering their own clandestine 
agendas. Masters of disguise, experts in surveillance, and lethal in combat, the members of the Silent Shadows Syndicate operate with precision and finesse, striking swiftly and decisively 
before melting back into the shadows from whence they came. Though their methods may be controversial, their services are in high demand by those who require the services of skilled operatives 
willing to operate outside the boundaries of conventional morality.''',
                    'room type': 'asteroid-3',
                    'directions': {
                        '1': '3rd Teleportation Deck',
                        '2': 'The Main Guildhall',
                        '3': 'The Order of the Arcane Scribes',
                        '4': 'The Wayfarers\' Brotherhood',
                        '5': 'The Artisans\' Collective',
                        '6': 'The Guardians of the Wilds',
                        '7': 'The Mercantile Consortium',
                        '8': 'The Sentinels of the Shield',
                        '9': 'The 3rd Old Manor',
                        },
                    'info': '''

do you want to:
%*GREEN*%1%*RESET*%. Go to the Teleportation Deck.
%*GREEN*%2%*RESET*%. Go to The Main Guildhall.
%*GREEN*%3%*RESET*%. Go to The Magic Guild.
%*GREEN*%4%*RESET*%. Go to The Explorers' Guild.
%*GREEN*%5%*RESET*%. Go to The Craftsmen's Guild.
%*GREEN*%6%*RESET*%. Go to The Nature Guild.
%*GREEN*%7%*RESET*%. Go to The Trade Guild.
%*GREEN*%8%*RESET*%. Go to The Guards Guild.
%*GREEN*%9%*RESET*%. Go to The Old Manor.''',
                },

                'The Guardians of the Wilds' :{
                    'description': '''
Guardians of the Wilds

Theme: Nature and Conservation
Purpose: The Guardians of the Wilds are a dedicated guild of druids, rangers, and nature enthusiasts who have devoted themselves to the protection and preservation of the natural world. Deeply 
connected to the land and its inhabitants, members of the Guardians of the Wilds serve as stewards of the wilderness, safeguarding forests, rivers, and mountains from the depredations of 
civilization and the encroachment of dark forces. Within their secluded guildhall, nestled amidst the ancient trees of a sacred grove, members commune with nature, honing their connection to 
the primal forces that sustain all life. Through their efforts, they seek to promote harmony between civilization and the wild, advocating for sustainable practices and opposing those who 
would exploit nature for profit or power. Whether embarking on quests to thwart the schemes of eco-terrorists, guiding travelers through treacherous terrain, or tending to the needs of injured 
wildlife, the Guardians of the Wilds stand as vigilant protectors of the natural world, sworn to defend it against all who would seek to do it harm.''',
                    'room type': 'asteroid-3',
                    'directions': {
                        '1': '3rd Teleportation Deck',
                        '2': 'The Main Guildhall',
                        '3': 'The Order of the Arcane Scribes',
                        '4': 'The Wayfarers\' Brotherhood',
                        '5': 'The Artisans\' Collective',
                        '6': 'The Silent Shadows Syndicate',
                        '7': 'The Mercantile Consortium',
                        '8': 'The Sentinels of the Shield',
                        '9': 'The 3rd Old Manor',
                        },
                    'info': '''

do you want to:
%*GREEN*%1%*RESET*%. Go to the Teleportation Deck.
%*GREEN*%2%*RESET*%. Go to The Main Guildhall.
%*GREEN*%3%*RESET*%. Go to The Magic Guild.
%*GREEN*%4%*RESET*%. Go to The Explorers' Guild.
%*GREEN*%5%*RESET*%. Go to The Craftsmen's Guild.
%*GREEN*%6%*RESET*%. Go to The Stealth Guild.
%*GREEN*%7%*RESET*%. Go to The Trade Guild.
%*GREEN*%8%*RESET*%. Go to The Guards Guild.
%*GREEN*%9%*RESET*%. Go to The Old Manor.''',
                },

                'The Mercantile Consortium' :{
                    'description': '''
Mercantile Consortium

Theme: Trade and Commerce
Purpose: The Mercantile Consortium is a formidable guild of merchants, traders, and entrepreneurs who wield considerable influence in the realm of commerce and finance. Their sprawling network 
of trade routes, marketplaces, and financial institutions spans continents, facilitating the flow of goods, wealth, and information across the known world. Within their opulent guildhall, a 
bustling nexus of commerce and negotiation, members of the Consortium broker lucrative deals, negotiate favorable terms, and vie for dominance in the cutthroat world of business. Masters of 
strategy, experts in logistics, and adept at navigating the complexities of international trade, members of the Mercantile Consortium are driven by a relentless pursuit of profit and power. 
Though their methods may be ruthless and their ambitions vast, their guild stands as a pillar of the global economy, shaping the course of history through the power of commerce and the pursuit 
of wealth.''',
                    'room type': 'asteroid-3',
                    'directions': {
                        '1': '3rd Teleportation Deck',
                        '2': 'The Main Guildhall',
                        '3': 'The Order of the Arcane Scribes',
                        '4': 'The Wayfarers\' Brotherhood',
                        '5': 'The Artisans\' Collective',
                        '6': 'The Silent Shadows Syndicate',
                        '7': 'The Guardians of the Wilds',
                        '8': 'The Sentinels of the Shield',
                        '9': 'The 3rd Old Manor',
                        },
                    'info': '''

do you want to:
%*GREEN*%1%*RESET*%. Go to the Teleportation Deck.
%*GREEN*%2%*RESET*%. Go to The Main Guildhall.
%*GREEN*%3%*RESET*%. Go to The Magic Guild.
%*GREEN*%4%*RESET*%. Go to The Explorers' Guild.
%*GREEN*%5%*RESET*%. Go to The Craftsmen's Guild.
%*GREEN*%6%*RESET*%. Go to The Stealth Guild.
%*GREEN*%7%*RESET*%. Go to The Trade Guild.
%*GREEN*%8%*RESET*%. Go to The Guards Guild.
%*GREEN*%9%*RESET*%. Go to The Old Manor.''',
                },

                'The Sentinels of the Shield' :{
                    'description': '''
Sentinels of the Shield

Theme: Protection and Security
- Purpose: The Sentinels of the Shield are an elite guild of guards and defenders dedicated to maintaining law, order, and safety within their jurisdiction. Comprised of highly trained 
warriors, vigilant sentries, and skilled law enforcers, they stand as bastions of protection against threats both mundane and supernatural. Whether guarding cities, patrolling borders, or 
protecting important figures, the Sentinels are renowned for their unwavering dedication and martial prowess.
- Specialties: They specialize in a wide array of skills including combat training, crowd control, investigation, and crisis management. Additionally, some members may possess magical 
abilities or specialized equipment tailored for their duties.
- Guildhall: Their guildhall serves as a fortress-like headquarters, strategically positioned within the heart of the city or at key points along the borders. It is heavily fortified and 
equipped with advanced surveillance systems, armories, training grounds, and detention facilities. The guildhall also houses administrative offices where leaders coordinate patrols, issue 
directives, and manage resources.
- Code of Conduct: Members of the Sentinels adhere to a strict code of conduct that emphasizes integrity, honor, and duty. They are sworn to protect the innocent, uphold the law, and serve the 
greater good, even at the risk of their own lives. Betrayal, corruption, or dereliction of duty are met with severe consequences, ensuring the trust and respect of the communities they 
safeguard.
- Training and Recruitment: Prospective members undergo rigorous training and screening processes to ensure they possess the necessary skills, discipline, and loyalty required to join the 
guild. Training programs cover various aspects of combat, law enforcement techniques, conflict resolution, and ethical decision-making. Experienced veterans provide mentorship and guidance to 
new recruits, fostering a sense of camaraderie and unity among the ranks.''',
                    'room type': 'asteroid-3',
                    'directions': {
                        '1': '3rd Teleportation Deck',
                        '2': 'The Main Guildhall',
                        '3': 'The Order of the Arcane Scribes',
                        '4': 'The Wayfarers\' Brotherhood',
                        '5': 'The Artisans\' Collective',
                        '6': 'The Silent Shadows Syndicate',
                        '7': 'The Guardians of the Wilds',
                        '8': 'The Mercantile Consortium',
                        '9': 'The 3rd Old Manor',
                        },
                    'info': '''

do you want to:
%*GREEN*%1%*RESET*%. Go to the Teleportation Deck.
%*GREEN*%2%*RESET*%. Go to The Main Guildhall.
%*GREEN*%3%*RESET*%. Go to The Magic Guild.
%*GREEN*%4%*RESET*%. Go to The Explorers' Guild.
%*GREEN*%5%*RESET*%. Go to The Craftsmen's Guild.
%*GREEN*%6%*RESET*%. Go to The Stealth Guild.
%*GREEN*%7%*RESET*%. Go to The Nature Guild.
%*GREEN*%8%*RESET*%. Go to The Trade Guild.
%*GREEN*%9%*RESET*%. Go to The Old Manor.''',
                },

                'The 3rd Old Manor' :{
                    'room type': 'asteroid-3',
                    'directions': {
                        '1': '3rd Teleportation Deck',
                        '2': 'The Main Guildhall',
                        '3': 'The Order of the Arcane Scribes',
                        '4': 'The Wayfarers\' Brotherhood',
                        '5': 'The Artisans\' Collective',
                        '6': 'The Silent Shadows Syndicate',
                        '7': 'The Guardians of the Wilds',
                        '8': 'The Mercantile Consortium',
                        '9': 'The Sentinels of the Shield',
                        },
                    'info': '''

do you want to:
%*GREEN*%1%*RESET*%. Go to the Teleportation Deck.
%*GREEN*%2%*RESET*%. Go to The Main Guildhall.
%*GREEN*%3%*RESET*%. Go to The Magic Guild.
%*GREEN*%4%*RESET*%. Go to The Explorers' Guild.
%*GREEN*%5%*RESET*%. Go to The Craftsmen's Guild.
%*GREEN*%6%*RESET*%. Go to The Stealth Guild.
%*GREEN*%7%*RESET*%. Go to The Nature Guild.
%*GREEN*%8%*RESET*%. Go to The Trade Guild.
%*GREEN*%9%*RESET*%. Go to The Guards Guild.''',
                },

            }
