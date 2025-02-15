from .items import *
from .creatures import *
from .Books import *

global KEY, ROOMS

KEY = [
    "█ = wall",
    "║ = door",
    "☼ = drawers",
    "╦ = rack",
    "Γ = stand",
    "╖ = stairs",
    "æ = cupboards",
    "√ = fireplace",
    "∩ = gate",
    "┬ = table",
    "í = hedge",
    "∟ = railing",
    "↨ = sofa",
    "š = storage device",
    "¥ = tree",
    "§ = bed",
    "╬ = wardrobe",
    "π = desk",
]


class RandomEvent:
    def __init__(
        self,
        name="Event name",
        probability=0.0,  # Probability of the event running (0.1 = 10% chance)
        condition=lambda player: True,  # Condition under which the event can occur
        effect=lambda player: None,
    ):  # Define the effect of the event
        self.name = name
        self.probability = probability
        self.condition = condition
        self.effect = effect

    def check_and_trigger(self, player):
        """Check if the event can occur based on its condition and probability, and trigger the effect."""
        import random

        if self.condition(player) and random.random() < self.probability:
            self.effect(player)


class Door:
    def __init__(self, RoomName, KeyCode=None) -> None:
        self.destination = RoomName
        self.lock = Lock(KeyCode) if KeyCode else None
        self.reveal_count = 0

    def Unlock(self, key: Key, player):
        return self.lock.unlock(key, player)

    def GetRoom(self, currentroom):
        if not self.lock.is_locked if isinstance(self.lock, Lock) else True:
            return self.destination
        else:
            type_text("The door is locked.")
            return currentroom

    def __str__(self) -> str:
        return self.lock.CurentRevealStr if self.lock else ""


class SwitchDoor(Door):
    def __init__(self, RoomOneName, RoomTwoName, KeyCode=None) -> None:
        super().__init__(RoomOneName, KeyCode)
        self.switch_destination = RoomTwoName

    def GetRoom(self, currentroom):
        if not self.lock.is_locked if isinstance(self.lock, Lock) else True:
            return self.destination
        else:
            return self.switch_destination


global map_dict, positions


def string_to_2d_list(map_str):
    map_str = map_str.strip()  # Remove leading/trailing whitespace
    return [list(line) for line in map_str.split("\n")]


def SetMapsAndPosiitionsDicts(map_dict, positions):
    map_dict = {}

    positions = {}
    for RoomName, RoomItem in ROOMS.items():
        if "descovered" in RoomItem and "position" in RoomItem and "map" in RoomItem:
            if RoomItem["descovered"]:
                map_dict[RoomName] = string_to_2d_list(RoomItem["map"])
                positions[RoomName] = RoomItem["position"]
    return map_dict, positions


def combine_maps(small_maps, positions: dict):
    # Check if positions dictionary is empty
    if not positions:
        # Return an empty map and a min_z value of 0
        return [[[" "]]], 0

    # Determine the size of the largest map needed
    max_z = max(pos[0] for pos in positions.values()) + 1
    min_z = min(pos[0] for pos in positions.values())
    total_z = max_z - min_z  # Total floors including basements
    max_row = max(pos[1] for pos in positions.values()) + 9
    max_col = max(pos[2] for pos in positions.values()) + 9

    # Create a 3D large map with spaces
    large_map = [
        [[" " for _ in range(max_col)] for _ in range(max_row)] for _ in range(total_z)
    ]

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
            floor_str = f"Ground Floor:\n" + "\n".join("".join(row) for row in floor)
        elif z > -min_z:
            floor_str = f"Floor {z + min_z}:\n" + "\n".join(
                "".join(row) for row in floor
            )
        else:
            floor_str = f"Basement {-(-z + min_z)}:\n" + "\n".join(
                "".join(row) for row in floor
            )
        floors.append(floor_str)
    return "\n\n".join(floors)


def ShowMap():
    global map_dict, positions
    map_dict, positions = SetMapsAndPosiitionsDicts(map_dict, positions)
    large_map, min_z = combine_maps(map_dict, positions)
    return display_map(large_map, min_z)


map_dict = {}

positions = {}

# a dictionary linking a room to other rooms
ROOMS = {
    "Hall": {
        "room type": "house",
        "position": (0, 8, 0),
        "descovered": True,
        "directions": {
            "south": Door("Kitchen"),
            "east": Door("Dining Room"),
            "north": Door("Armoury"),
            "up": Door("Landing"),
            "easter": Door("Cavegame"),
        },
        "items": {
            "torch": item("torch"),
        },
        "containers": {
            "drawers": container([
                Book(
                    "founder's journal",
                    """
Entry 1 - Beginnings of a Dream
“I have begun the construction of the mansion. The site was perfect: secluded, hidden in the shadow of the mountains, far from the prying eyes of the world. This will be my legacy—a 
grand estate that will stand as a testament to my success. But it will be more than just a home. This place will be a sanctuary. For what, I am not yet sure, but I feel as though I 
am building something that will outlast me. Something... greater.”

Entry 7 - The Architect's Warnings
“I’ve received strange advice from the architect. He suggests that the mansion be built not just to endure the ravages of time, but to manipulate it. He speaks of a force beyond our 
understanding, something that could sustain us, even preserve us for eternity. I am beginning to think he knows more than he’s letting on. Is it possible? Time itself, as fluid as 
the air we breathe, could be contained within these walls? I am intrigued... and yet, wary.”

Entry 13 - Neel-thee’s Influence
“He has arrived. Neel-thee. I do not know where he comes from, nor do I understand his true purpose, but his presence is undeniable. He claims to be an expert in the study of the 
mind. He has offered to assist me with the mansion’s ‘true potential.’ There are whispers of immortality, of breaking free from the boundaries of time. I am not entirely convinced, 
but he has a peculiar way about him. A quiet power, and a gaze that chills me to the core. I have agreed to allow him to stay, for now.”

Entry 22 - The Pact
“Neel-thee’s influence has grown. It is clear that he is not simply an academic. He has performed experiments in the mansion’s hidden chambers—secret rituals, something that bends 
the very laws of nature. The walls seem to pulse with a strange energy now, an unseen force that makes me feel both powerful and fearful. We’ve come to an agreement: he will oversee 
the mansion’s true purpose, and in return, I will give him access to its most hidden secrets. I have committed myself to this, for better or worse.”

Entry 31 - A Changing Mind
“Something is wrong. The mansion is no longer just a building. It is alive. The air is thick with a sense of dread, and the once calm halls now echo with whispers I cannot explain. 
Neel-thee has begun to speak of ‘preserving the mansion’s essence’—his words are becoming less coherent, and his requests more bizarre. I fear he has crossed a line, one that cannot 
be undone. I must find a way to stop him, but I am unsure of how. Perhaps... perhaps it is already too late.”

Entry 38 - Neel-thee is Gone
“Neel-thee has been gone for three days now. I do not know when he will return, but I hope he will return soon”

Entry 39 - Neel-thee's Return
“Neel-thee has returned now. He seems angry. I have not seen him since he stomped through the door. I wonder what is bothering him?”

Entry 40 - The Price of Immortality
“The pact has been sealed. Neel-thee has shown me the cost of eternal life, and I am now bound to this place. I have seen the future, and I do not like what I have seen. The mansion 
is a prison, its walls closing in on us, its time-frozen halls trapping us in an endless loop. I will never escape. Neither will Neel-thee. And yet, he seems unperturbed. He remains 
obsessed with his work, his experiments, his need to control everything—everything but the very thing that will consume him in the end. I wonder if I am already beyond saving. 
Perhaps the mansion is not just a building. It is the keeper of souls.”

Entry 78 - The Change
“There is another price of immortality. Over the last 34 days I have been changing, and soon I will not be able to write in this diary anymore. This is the last thing I will put in my diary. This is the last thing you will hear from Geraldo Times.”
"""
                )
    ]),
        },
        "info": "You are in the hall of the house. There is a chest of drawers against one wall, and flaming torches on the walls. You hear a \
smash from the south.",
        "map": """
████║████
█☼☼     █
█       █
█       █
█       ║
█       █
█╖      █
█╖      █
████║████""",
        "Hints": [
            "Those drawers look intresting.",
            "I wonder if those drawers are locked.",
            "I wonder if I can get this torch out of it's holder.",
            "I wonder what that smash from the south was.",
            "I should probably aviod that smashing sound.",
        ],
    },
    "Cavegame": {
        "room type": "easter egg",
        "directions": {
            "back": Door("Hall"),
        },
        "info": 'Cavegame, type "go back" to leave.',
    },
    "Kitchen": {
        "room type": "house",
        "position": (0, 16, 0),
        "descovered": False,
        "directions": {
            "north": Door("Hall"),
            "east": Door("Garden"),
        },
        "items": {
            "rations": item("rations"),
        },
        "containers": {
            "cupboards": container([item("money-pouch", "valuable", 10)]),
        },
        "creatures stats": [
            creature(
                "hungry bear",
                7,
                5,
                [item("claw", "valuable", 1)],
                "A large 7ft 8 brown bear that looks hungry",
                "A hungry bear attacks you!",
            ),
        ],
        "info": "You are in the kitchen, there are several trashed cupboards, one of them has a knotted cord sticking out, and a fireplace.",
        "map": """
████║████
█       █
█       █
█       █
█       ║
█       █
█       █
█ææææ√ææ█
█████████""",
        "Hints": [
            "I wonder if there is anything salvageable in the cupboards.",
            "I should probably look around.",
        ],
        "random_events": [
            RandomEvent(
                name="Empty cupboards",
                probability=0.15,  # Adjust this for the probability of the event running (e.g., 0.1 is 10% chance)
                condition=lambda player: True,  # Condition under which the event can occur
                effect=lambda player: ROOMS["Kitchen"]["containers"][
                    "cupboards"
                ].take_contents(),  # Define the effect of the event
            )
        ],
    },
    "Dining Room": {
        "room type": "house",
        "position": (0, 8, 8),
        "descovered": False,
        "directions": {
            "west": Door("Hall"),
            "south": Door("Garden"),
            "north": Door("Sitting Room"),
        },
        "items": {
            "": item("potion"),
        },
        "containers": {
            "chandelier": container([item("gem", "valuable", 50)]),
        },
        "info": "You are in the dining room, there is a dining table with 8 chairs around it in the middle of the room, and a chandelier on the ceiling. You hear \
ripping from the north.",
        "map": """
████║████
█       █
█       █
█  ┬┬┬  █
║  ┬┬┬  █
█  ┬┬┬  █
█       █
█       █
████║████""",
        "Hints": [
            "I wonder if there is anything in the chandelier.",
            "I wonder if there is anything around the room.",
        ],
    },
    "Garden": {
        "room type": "house",
        "position": (0, 16, 8),
        "descovered": False,
        "directions": {
            "north": Door("Dining Room"),
            "west": Door("Kitchen"),
        },
        "items": {
            "recorder": Recorder(
                "recorder 143",
                "The prince is out of control! Neel-thee's gone crazy! Get him to the safehouse!"
            )
        },
        "info": "You are in a bright garden you are in a garden with a gate out of the house.",
        "map": """
████║████
█       í
█       í
█       í
║       í
█       í
█       ∩
█       í
█íííííííí""",
        "Hints": [
            "I think I need a key for the gate.",
        ],
    },
    "Armoury": {
        "room type": "house",
        "position": (0, 0, 0),
        "descovered": False,
        "directions": {
            "south": Door("Hall"),
            "east": Door("Sitting Room"),
            "up": Door("Tower Bottom"),
        },
        "containers": {
            "racks": container([item("sword", "weapon", 3)]),
            "stand": container([item("armour")]),
            "storage": container([item("grappling-hook")]),
        },
        "info": "You are in a dimly lit armoury with 3 racks full of damaged weapons, and a armour stand with battered armour. \n\
You notice a "
        "storage device in one corner. You hear a ripping from the east.",
        "map": """
█████████
█š     ╖█
█      ╖█
█╦      █
█       ║
█       █
█Γ      █
█       █
████║████""",
        "Hints": [
            "Maybe there is something salvageable on the racks.",
            "I wonder if that armour is salvageable.",
        ],
    },
    "Sitting Room": {
        "room type": "house",
        "position": (0, 0, 8),
        "descovered": False,
        "directions": {
            "west": Door("Armoury"),
            "south": Door("Dining Room"),
            "down": Door("Basement 1"),
        },
        "creatures stats": [
            creature(
                "grumpy pig",
                3,
                4,
                [item("savaged cushion")],
                "A oxford sandy & black pig with a savaged cushion on it's head",
                "A grumpy pig spots you and comes towards you!",
            ),
        ],
        "containers": {
            "sofas": container([item("cushion")]),
        },
        "info": "You are in a bright sitting room with several sofas.",
        "map": """
█████████
█      ╖█
█  ↨↨↨ ╖█
█     ↨ █
║     ↨ █
█     ↨ █
█       █
█       █
████║████""",
        "Hints": [
            "That pig seems dangerous.",
            "Those sofas look comfy.",
            "I wonder what's down those stairs.",
        ],
    },
    "Landing": {
        "room type": "house",
        "position": (1, 8, 0),
        "descovered": False,
        "directions": {
            "down": Door("Hall"),
            "north": Door("Tower Bottom"),
            "east": Door("Bedroom"),
            "south": Door("Balcony"),
        },
        "containers": {
            "floorboards": container([item("money-pouch", "valuable", 10)]),
        },
        "info": "You are in a dark landing with creaky floorboards.",
        "map": """
████║████
█       █
█       █
█       █
█       ║
█       █
█╖      █
█╖      █
████║████""",
        "Hints": ["I wonder if I can pry one of the floorboards back."],
    },
    "Bedroom": {
        "room type": "house",
        "position": (1, 8, 8),
        "descovered": False,
        "directions": {
            "west": Door("Landing"),
            "north": Door("Office"),
        },
        "containers": {
            "bed": container([item("chamber-pot")]),
            "drawers": container([item("waterskin")]),
            "wardrobe": container([item("pig-rod")]),
        },
        "info": "You are in a dark yet airy bedroom, with a double bed, a chest of drawers, and a wardrobe.",
        "map": """
████║████
█       █
█       █
█       █
║       █
█       █
█╬    §§█
█╬  ☼☼§§█
█████████""",
        "Hints": [
            "I wonder what's north.",
            "I wonder if there is anything under the bed.",
            "I wonder if there is anything in the drawers.",
            "I wonder what's in the wardrobe.",
        ],
    },
    "Office": {
        "room type": "house",
        "position": (1, 0, 8),
        "descovered": False,
        "directions": {
            "south": Door("Bedroom"),
            "west": Door("Tower Bottom"),
        },
        "containers": {
            "storage": container(
                [
                    item("saddle"),
                    item("ink-pot"),
                    item("parchment"),
                    item("knife", "weapon", 2),
                ]
            ),
            "desk": container([item("quill")]),
        },
        "info": "You are in a bright office with a desk, several storage devices, and a lot of windows.",
        "map": """
█████████
█ š    š█
█       █
█   π š █
║   π   █
█   πš  █
█š      █
█       █
████║████""",
        "Hints": [
            "I wonder what's in the storage, if anything.",
            "I wonder what's through the southern door.",
            "I wonder if there is anything on the desk.",
        ],
    },
    "Balcony": {
        "room type": "house",
        "position": (1, 16, 0),
        "descovered": False,
        "directions": {
            "north": Door("Landing"),
        },
        "info": "You are on a balcony with an ornate railing. It is a nice day.",
        "map": """
████║████
∟       ∟
∟       ∟
∟       ∟
∟       ∟
∟       ∟
∟       ∟
∟       ∟
∟∟∟∟∟∟∟∟∟""",
        "Hints": [
            "If I had a grappling-hook I might be able to throw it into the trees and swing down into the forest.",
        ],
    },
    "Tower Bottom": {
        "room type": "house",
        "position": (1, 0, 0),
        "descovered": False,
        "directions": {
            "south": Door("Landing"),
            "east": Door("Office"),
            "down": Door("Armoury"),
            "up": Door("Tower Middle"),
        },
        "info": "You are in the base of a stone tower, there is a spiral staircase going up into the darkness.",
        "map": """
█████████
█      ╖█
█      ╖█
█       █
█       ║
█       █
█╖      █
█╖      █
████║████""",
        "Hints": [
            "I wonder what's south.",
            "I wonder what's east.",
            "I wonder what's up.",
            "I wonder what's down.",
        ],
    },
    "Tower Middle": {
        "room type": "house",
        "position": (2, 0, 0),
        "descovered": False,
        "directions": {
            "down": Door("Tower Bottom"),
            "up": Door("Tower Top"),
        },
        "containers": {
            "stone": container(
                [item("money-pouch", "valuable", 25), Key("key", "629.IdnXwnt")], True
            ),
        },
        "items": {
            "": item("tome"),
        },
        "info": "You are in the middle of a stone tower. The only light comes from above, through the cracks around the hatch to above.",
        "map": """
█████████
█      ╖█
█      ╖█
█       █
█       █
█       █
█╖      █
█╖      █
█████████""",
        "Hints": [
            "There might be an item here.",
        ],
    },
    "Tower Top": {
        "room type": "house",
        "position": (3, 0, 0),
        "descovered": False,
        "directions": {
            "down": Door("Tower Middle"),
            "teleport": Door("Teleportation Deck"),
        },
        "creatures stats": [
            creature(
                "greedy goblin",
                5,
                7,
                [item("knife", "weapon", 2), item("money-pouch", "valuable", 5)],
                "A 4ft 7 dirty and greedy goblin",
                "A greedy goblin spots you and your money pouch!",
                creature_type("humanoid", "goblin"),
            ),
        ],
        "info": "You are at the top of a stone tower. There are windows in every wall.",
        "map": """
█████████
█      ╖█
█      ╖█
█       █
█       █
█       █
█       █
█       █
█████████""",
        "Hints": [
            "I could teleport.",
        ],
    },
    "Basement Armoury": {
        "room type": "house",
        "position": (-1, 0, 0),
        "descovered": False,
        "directions": {
            "south": Door("Basement 3"),
            "east": Door("Basement 1"),
            "north": Door("DND"),
        },
        "items": {
            "torch": item("torch"),
        },
        "containers": {
            "rack-1": container([item("bow", "weapon", 4)]),
            "rack-2": container([item("spear", "weapon", 3)]),
        },
        "info": "You are in a dimly lit underground armoury (all the light in the room comes from 3 torches on the walls) with 2 racks full of damaged weapons,\n\
rack-1 has damaged bows and rack-2 has damaged spears.",
        "map": """
██████║██
█╦      █
█      ╦█
█       █
█       ║
█       █
█       █
█       █
████║████""",
        "Hints": [
            "The things in rack-1 and rack-2 are salvigable.",
            "I wonder if I can get this torch out of it's holder.",
        ],
    },
    "Basement 1": {
        "room type": "house",
        "position": (-1, 0, 8),
        "descovered": False,
        "directions": {
            "south": Door("Basement 2"),
            "west": Door("Basement Armoury"),
            "up": Door("Sitting Room"),
        },
        "items": {
            "torch": item("torch"),
        },
        "info": "You are in an dimly lit underground (all the light in the room comes from 3 torches on the walls). You hear a ripping from the\
 stairs going up.",
        "map": """
█████████
█      ╖█
█      ╖█
█       █
║       █
█       █
█       █
█       █
████║████""",
        "Hints": [
            "I wonder if I can get this torch out of it's holder.",
        ],
    },
    "Basement 2": {
        "room type": "house",
        "position": (-1, 8, 8),
        "descovered": False,
        "directions": {
            "north": Door("Basement 1"),
            "west": Door("Basement 3"),
        },
        "items": {
            "torch": item("torch"),
        },
        "info": "You are in an dimly lit underground (all the light in the room comes from 3 torches on the walls).",
        "map": """
████║████
█       █
█       █
█       █
║       █
█       █
█       █
█       █
█████████""",
        "Hints": [
            "I wonder if I can get this torch out of it's holder.",
        ],
    },
    "Basement 3": {
        "room type": "house",
        "position": (-1, 8, 0),
        "descovered": False,
        "directions": {
            "south": Door("Basement 4"),
            "east": Door("Basement 2"),
            "north": Door("Basement Armoury"),
        },
        "items": {
            "torch": item("torch"),
        },
        "info": "You are in an dimly lit underground (all the light in the room comes from 3 torches on the walls).",
        "map": """
████║████
█       █
█       █
█       █
█       ║
█       █
█       █
█       █
████║████""",
    },
    "Basement 4": {
        "room type": "house",
        "position": (-1, 16, 0),
        "descovered": False,
        "directions": {
            "north": Door("Basement 3"),
            "east": Door("Library"),
            "shoot": Door("Cavern 1"),
        },
        "items": {
            "torch": item("torch"),
        },
        "info": "You are in an dimly lit underground (all the light in the room comes from 3 torches on the walls). there is a choot in the floor (type: 'go shoot' to go down the shoot).",
        "map": """
████║████
█       █
█       █
█       █
█       ║
█       █
█       █
█       █
█████████""",
        "Hints": [
            "I wonder if I can get this torch out of it's holder.",
        ],
    },
    "Library": {
        "room type": "house",
        "position": (-1, 16, 8),
        "descovered": False,
        "directions": {
            "west": Door("Room name"),
            "bookcase": Door("Cavern 3"),
        },
        "creatures stats": [Geraldo()],
        "containers": {
            "bookcases": container(sample(books, 3)),
        },
        "info": "Towering bookcases filled with odd, mismatched books line the walls. A cat named geraldo times. Some have faded titles, others are blank, arranged almost deliberately. One bookcase stands slightly forward, leaving a faint scrape on the floor. The air is still, as if waiting for you to notice.",
        "map": """
█████████
█       █
█       █
█       █
║       █
█       █
█       █
█       █
█████████""",
        "Hints": [
            'Is it just me or are the first letters of all of those book names spelling the words "He\'s watching you"',
        ],
    },
                'DND': {
                    'room type': 'type',
                    'position': (-1, -8, 0),
                    'descovered': False,
                    'directions': {
                        'north': Door('Room name'),
                        'south': Door("Basement Armoury"),
                    },
                    'creatures stats': [
                        NPC(
                            "dungeon master",
                            1000,
                            100,
                            type=creature_type("god", "dungeon master"),
                            responses={
                                "introduction": "I see you’ve come to the next stage of your quest, player. But remember—your choices, even the smallest ones, will shape your fate.\
Oh and before I forget, If you go through the door to the north, there wil be no turning back. You will ether have to join Neel-thee or fight him.",
                                "map": "Oh, the map! That's the map of one of my favourite places! Sword Coast is an amazing place to be! I hope you can go there one day.",
                                "you": "Me? I'm a prymodrial being from beyond the stars that can alter reality. You can call me the Dungeon Master."
                            },
                            keyword_variations={
                                "introduction": ["hello", "hi ", "greetings", "hey"],
                                "map": ["the map", "map", "sword coast", "strange map"],
                                "you": ["you"],
                            },
                            generic_response="I will not answer that question at this time."
                        ),
                    ],
                    'containers': {
                        'table': container([item("unknown map", "map", "This map is of some strange land, far away. At the top of the map, it says 'Sword Coast.'")]),
                    },
                    'info': 'You are in a dimly lit room with a table in the middle of it, and a looming figure to your left. The figure has a name badge that says "dungeon master".',
                    'map': '''
████║████
█       █
█       █
█  ┬┬┬  █
█  ┬┬┬  █
█  ┬┬┬  █
█       █
█       █
██████║██''',
                    'random_events': [
                        RandomEvent(
                            name='rumble',
                            probability=0.4,  # Adjust this for the probability of the event running (e.g., 0.1 is 10% chance)
                            condition=lambda player: True,  # Condition under which the event can occur
                            effect=lambda player: type_text("You hear a strange rumbling sound."),  # Define the effect of the event
                        )
                    ],
                    'random_events': [
                        RandomEvent(
                            name='fire',
                            probability=0.3,  # Adjust this for the probability of the event running (e.g., 0.1 is 10% chance)
                            condition=lambda player: True,  # Condition under which the event can occur
                            effect=lambda player: type_text("Fire comes gushing out of a crack in the roof and into the wall."),  # Define the effect of the event
                        )
                    ],
                    },
    "Cavern 1": {
        "room type": "cavern",
        "position": (-2, 0, 0),
        "descovered": False,
        "directions": {
            "up": Door("Basement 4"),
            "down": Door("Cavern 2"),
        },
        "info": "you are in a dark cavern with the only light coming from the shoot you came through. A voice in the back of your head says: 'Do not go down the shoot, leave while you still can!'",
        "map": """
█████████
█       █
█       █
█       █
█       █
█       █
█       █
█       █
█████████""",
        "Hints": [
            "I should probably go up the shoot I came from.",
        ],
    },
    "Cavern 2": {
        "room type": "cavern",
        "position": (-3, 0, 0),
        "descovered": False,
        "directions": {"up": SwitchDoor("Cavern 1", "Cavern 3", "7k69fImz4y")},
        "info": "you are in a dark cavern with the only light coming from the shoot you came through. A voice in the back of your head says: 'You fool! You can never get back now!'",
        "map": """
█████████
█       █
█       █
█       █
█       █
█       █
█       █
█       █
█████████""",
        "Hints": [
            "I should probably go back up so I'm not here forever.",
            "I wander what the voice was talking about.",
        ],
    },
    "Cavern 3": {
        "room type": "cavern",
        "position": (-2, 8, 0),
        "descovered": False,
        "directions": {
            "down": Door("Cavern 2"),
            "bookcase": Door("Library"),
        },
        "info": "you are in a dark cavern with the only light coming from the crack behind a bookcase. A voice in the back of your head says: 'I give up.'",
        "map": """
█████████
█       █
█       █
█       █
█       █
█       █
█       █
█       █
█████████""",
        "Hints": [
            "I wander what's behind that bookcase.",
        ],
    },
    "Forest Clearing": {
        "room type": "forest",
        "directions": {
            "north": Door("Forest Path1"),
            "east": Door("Forest Path2"),
            "south": Door("Forest Path1"),
            "west": Door("Forest Path2"),
        },
        "info": "You are in a forest clearing outside the house.",
        "map": """
 ¥¥   ¥ ¥
¥     ¥  
 ¥     ¥¥
¥        
        ¥
       ¥¥
¥      ¥ 
 ¥   ¥¥  
  ¥  ¥   
         """,
    },
    "Forest Path1": {
        "room type": "forest",
        "directions": {
            "north": Door("Forest Clearing"),
            "south": Door("Forest Clearing"),
        },
        "info": "You are in a forest path outside the house.",
        "map": """
  ¥  ¥   
 ¥     ¥ 
¥       ¥
¥      ¥ 
¥     ¥  
¥     ¥  
 ¥¥    ¥¥
 ¥     ¥ 
 ¥¥   ¥ ¥
""",
    },
    "Forest Path2": {
        "room type": "forest",
        "directions": {
            "east": Door("Forest Clearing"),
            "west": Door("Forest Clearing"),
        },
        "info": "You are in a forest path outside the house.",
        "map": """
¥¥¥¥¥  ¥ 
  ¥  ¥¥¥¥
¥¥  ¥  ¥¥
        ¥
¥¥       
¥¥¥¥¥    
  ¥  ¥¥¥¥
  ¥¥¥   ¥
 ¥   ¥¥¥ 
""",
    },
    "Teleportation Deck": {
        "room type": "asteroid-1",
        "directions": {
            "teleport": Door("Tower Top"),
            "0": Door("Charter ship"),
            "1": Door("The Dancing Jellyfish Inn"),
            "2": Door("The Slopy Plasmoid Tapphouse"),
            "3": Door("The Centaurbow Weapon Shop"),
            "4": Door("The Gadabout Bakery"),
            "5": Door("The Shifterspender St"),
            "6": Door("The Town Hall"),
            "7": Door("The Assassins Guild"),
            "8": Door("The Watch Castle"),
            "9": Door("The Old Manor"),
        },
        "items": {
            "money-pouch": item("money-pouch", "valuable", 10),
        },
        "info": """
You are in a strange cave with many teleportation circles, as well as some ships that are floating above the floor.

Out of the gap in the side of the cave it looks black with a few twinkles of light.
There is a sign on the wall. It is a map of a city on an asteriod.
The main locations are: The Teleportation Deck, The Dancing Jellyfish Inn, The Slopy Plasmoid Tapphouse, The Centaurbow Weapon Shop, The Gadabout Bakery, The Shifterspender Store, 
The Town Hall, The Thieves Guild, The Watch Castle, and The Old Manor.

Do you want to:
0. Charter a ship away (Costs 10 money).
1. Go to The Dancing Jellyfish Inn.
2. Go to The Slopy Plasmoid Tapphouse.
3. Go to The Centaurbow Weapon Shop.
4. Go to The Gadabout Bakery.
5. Go to The Shifterspender St.
6. Go to The Town Hall.
7. Go to The Assassins Guild.
8. Go to The Watch Castle.
9. Go to The Old Manor.""",
    },
    "Charter ship": {
        "room type": "asteroid-1",
        "directions": {
            "1": Door("Teleportation Deck"),
            "2": Door("The Dancing Jellyfish Inn"),
            "3": Door("The Slopy Plasmoid Tapphouse"),
            "4": Door("The Centaurbow Weapon Shop"),
            "5": Door("The Gadabout Bakery"),
            "6": Door("The Shifterspender St"),
            "7": Door("The Town Hall"),
            "8": Door("The Assassins Guild"),
            "9": Door("The Watch Castle"),
            "10": Door("The Old Manor"),
            "11": Door("2nd Teleportation Deck"),
            "12": Door("3rd Teleportation Deck"),
        },
        "info": """

You charter a ship, and the Captain says: "You can go anywhere you like before you land back on this here asteriod!"

Do you want to:
1. Go to the Teleportation Deck.
2. Go to The Dancing Jellyfish Inn.
3. Go to The Slopy Plasmoid Tapphouse.
4. Go to The Centaurbow Weapon Shop.
5. Go to The Gadabout Bakery.
6. Go to The Shifterspender St.
7. Go to The Town Hall.
8. Go to The Assassins Guild.
9. Go to The Watch Castle.
10. Go to The Old Manor.
11. Go to The 2nd Asteriod.
12. Go to The 3rd Asteriod.""",
    },
    "The Dancing Jellyfish Inn": {
        "room type": "asteroid-1",
        "directions": {
            "1": Door("Teleportation Deck"),
            "2": Door("The Slopy Plasmoid Tapphouse"),
            "3": Door("The Centaurbow Weapon Shop"),
            "4": Door("The Gadabout Bakery"),
            "5": Door("The Shifterspender St"),
            "6": Door("The Town Hall"),
            "7": Door("The Assassins Guild"),
            "8": Door("The Watch Castle"),
            "9": Door("The Old Manor"),
        },
        "info": """

do you want to:
1. Go to the Teleportation Deck.
2. Go to The Slopy Plasmoid Tapphouse.
3. Go to The Centaurbow Weapon Shop.
4. Go to The Gadabout Bakery.
5. Go to The Shifterspender St.
6. Go to The Town Hall.
7. Go to The Assassins Guild.
8. Go to The Watch Castle.
9. Go to The Old Manor.""",
    },
    "The Slopy Plasmoid Tapphouse": {
        "room type": "asteroid-1",
        "directions": {
            "1": Door("Teleportation Deck"),
            "2": Door("The Dancing Jellyfish Inn"),
            "3": Door("The Centaurbow Weapon Shop"),
            "4": Door("The Gadabout Bakery"),
            "5": Door("The Shifterspender St"),
            "6": Door("The Town Hall"),
            "7": Door("The Assassins Guild"),
            "8": Door("The Watch Castle"),
            "9": Door("The Old Manor"),
        },
        "info": """

do you want to:
1. Go to the Teleportation Deck.
2. Go to The Dancing Jellyfish Inn.
3. Go to The Centaurbow Weapon Shop.
4. Go to The Gadabout Bakery.
5. Go to The Shifterspender St.
6. Go to The Town Hall.
7. Go to The Assassins Guild.
8. Go to The Watch Castle.
9. Go to The Old Manor.""",
    },
    "The Centaurbow Weapon Shop": {
        "room type": "asteroid-1",
        "directions": {
            "1": Door("Teleportation Deck"),
            "2": Door("The Dancing Jellyfish Inn"),
            "3": Door("The Slopy Plasmoid Tapphouse"),
            "4": Door("The Gadabout Bakery"),
            "5": Door("The Shifterspender St"),
            "6": Door("The Town Hall"),
            "7": Door("The Assassins Guild"),
            "8": Door("The Watch Castle"),
            "9": Door("The Old Manor"),
        },
        "info": """

do you want to:
1. Go to the Teleportation Deck.
2. Go to The Dancing Jellyfish Inn.
3. Go to The Slopy Plasmoid Tapphouse.
4. Go to The Gadabout Bakery.
5. Go to The Shifterspender St.
6. Go to The Town Hall.
7. Go to The Assassins Guild.
8. Go to The Watch Castle.
9. Go to The Old Manor.""",
    },
    "The Gadabout Bakery": {
        "room type": "asteroid-1",
        "directions": {
            "1": Door("Teleportation Deck"),
            "2": Door("The Dancing Jellyfish Inn"),
            "3": Door("The Slopy Plasmoid Tapphouse"),
            "4": Door("The Centaurbow Weapon Shop"),
            "5": Door("The Shifterspender St"),
            "6": Door("The Town Hall"),
            "7": Door("The Assassins Guild"),
            "8": Door("The Watch Castle"),
            "9": Door("The Old Manor"),
        },
        "info": """

do you want to:
1. Go to the Teleportation Deck.
2. Go to The Dancing Jellyfish Inn.
3. Go to The Slopy Plasmoid Tapphouse.
4. Go to The Centaurbow Weapon Shop.
5. Go to The Shifterspender St.
6. Go to The Town Hall.
7. Go to The Assassins Guild.
8. Go to The Watch Castle.
9. Go to The Old Manor.""",
    },
    "The Shifterspender St": {
        "room type": "asteroid-1",
        "directions": {
            "1": Door("Teleportation Deck"),
            "2": Door("The Dancing Jellyfish Inn"),
            "3": Door("The Slopy Plasmoid Tapphouse"),
            "4": Door("The Centaurbow Weapon Shop"),
            "5": Door("The Gadabout Bakery"),
            "6": Door("The Town Hall"),
            "7": Door("The Assassins Guild"),
            "8": Door("The Watch Castle"),
            "9": Door("The Old Manor"),
        },
        "info": """

do you want to:
1. Go to the Teleportation Deck.
2. Go to The Dancing Jellyfish Inn.
3. Go to The Slopy Plasmoid Tapphouse.
4. Go to The Centaurbow Weapon Shop.
5. Go to The Gadabout Bakery.
6. Go to The Town Hall.
7. Go to The Assassins Guild.
8. Go to The Watch Castle.
9. Go to The Old Manor.""",
    },
    "The Town Hall": {
        "room type": "asteroid-1",
        "directions": {
            "1": Door("Teleportation Deck"),
            "2": Door("The Dancing Jellyfish Inn"),
            "3": Door("The Slopy Plasmoid Tapphouse"),
            "4": Door("The Centaurbow Weapon Shop"),
            "5": Door("The Gadabout Bakery"),
            "6": Door("The Shifterspender St"),
            "7": Door("The Assassins Guild"),
            "8": Door("The Watch Castle"),
            "9": Door("The Old Manor"),
        },
        "info": """

do you want to:
1. Go to the Teleportation Deck.
2. Go to The Dancing Jellyfish Inn.
3. Go to The Slopy Plasmoid Tapphouse.
4. Go to The Centaurbow Weapon Shop.
5. Go to The Gadabout Bakery.
6. Go to The Shifterspender St.
7. Go to The Assassins Guild.
8. Go to The Watch Castle.
9. Go to The Old Manor.""",
    },
    "The Assassins Guild": {
        "room type": "asteroid-1",
        "directions": {
            "1": Door("Teleportation Deck"),
            "2": Door("The Dancing Jellyfish Inn"),
            "3": Door("The Slopy Plasmoid Tapphouse"),
            "4": Door("The Centaurbow Weapon Shop"),
            "5": Door("The Gadabout Bakery"),
            "6": Door("The Shifterspender St"),
            "7": Door("The Town Hall"),
            "8": Door("The Watch Castle"),
            "9": Door("The Old Manor"),
        },
        "info": """,

do you want to:
1. Go to the Teleportation Deck.
2. Go to The Dancing Jellyfish Inn.
3. Go to The Slopy Plasmoid Tapphouse.
4. Go to The Centaurbow Weapon Shop.
5. Go to The Gadabout Bakery.
6. Go to The Shifterspender St.
7. Go to The Town Hall.
8. Go to The Watch Castle.
9. Go to The Old Manor.""",
    },
    "The Watch Castle": {
        "room type": "asteroid-1",
        "directions": {
            "1": Door("Teleportation Deck"),
            "2": Door("The Dancing Jellyfish Inn"),
            "3": Door("The Slopy Plasmoid Tapphouse"),
            "4": Door("The Centaurbow Weapon Shop"),
            "5": Door("The Gadabout Bakery"),
            "6": Door("The Shifterspender St"),
            "7": Door("The Town Hall"),
            "8": Door("The Assassins Guild"),
            "9": Door("The Old Manor"),
        },
        "info": """

do you want to:
1. Go to the Teleportation Deck.
2. Go to The Dancing Jellyfish Inn.
3. Go to The Slopy Plasmoid Tapphouse.
4. Go to The Centaurbow Weapon Shop.
5. Go to The Gadabout Bakery.
6. Go to The Shifterspender St.
7. Go to The Town Hall.
8. Go to The Assassins Guild.
9. Go to The Old Manor.""",
    },
    "The Old Manor": {
        "room type": "asteroid-1",
        "directions": {
            "1": Door("Teleportation Deck"),
            "2": Door("The Dancing Jellyfish Inn"),
            "3": Door("The Slopy Plasmoid Tapphouse"),
            "4": Door("The Centaurbow Weapon Shop"),
            "5": Door("The Gadabout Bakery"),
            "6": Door("The Shifterspender St"),
            "7": Door("The Town Hall"),
            "8": Door("The Assassins Guild"),
            "9": Door("The Watch Castle"),
        },
        "info": """

do you want to:
1. Go to the Teleportation Deck.
2. Go to The Dancing Jellyfish Inn.
3. Go to The Slopy Plasmoid Tapphouse.
4. Go to The Centaurbow Weapon Shop.
5. Go to The Gadabout Bakery.
6. Go to The Shifterspender St.
7. Go to The Town Hall.
8. Go to The Assassins Guild.
9. Go to The Watch Castle.""",
    },
    "2nd Teleportation Deck": {
        "room type": "asteroid-2",
        "directions": {
            "1": Door("Charter 2nd Ship"),
            "2": Door("The 2nd Dancing Jellyfish Inn"),
            "3": Door("The 2nd Slopy Plasmoid Tapphouse"),
            "4": Door("The 2nd GiffHammer Weapon Shop"),
            "5": Door("The 2nd Gadabout Bakery"),
            "6": Door("The 2nd Githspender St"),
            "7": Door("The 2nd Town Hall"),
            "8": Door("The 2nd Thieves Guild"),
            "9": Door("The 2nd Watch Castle"),
        },
        "10": Door("The 2nd Old Manor"),
        "info": """
You are in a strange cave with many teleportation circles, as well as some ships that are floating above the floor.

Out of the gap in the side of the cave it looks black with a few twinkles of light.
There is a sign on the wall. It is a map of a city on an asteriod.
The main locations are: The Teleportation Deck, The Dancing Jellyfish Inn, The Slopy Plasmoid Tapphouse, The GiffHammer Weapon Shop, The Gadabout Bakery, The Githspender Store,
The Town Hall, The Thieves Guild, The Watch Castle, and The Old Manor.
do you want to:
1. Charter a ship away.
2. Go to The Dancing Jellyfish Inn.
3. Go to The Slopy Plasmoid Tapphouse.
4. Go to The Giffhammer Weapon Shop.
5. Go to The Gadabout Bakery.
6. Go to The Githspender St.
7. Go to The Town Hall.
8. Go to The Thieves Guild.
9. Go to The Watch Castle.
10. Go to The Old Manor.""",
    },
    "Charter 2nd Ship": {
        "room type": "asteroid-2",
        "directions": {
            "1": Door("2nd Teleportation Deck"),
            "2": Door("The 2nd Dancing Jellyfish Inn"),
            "3": Door("The 2nd Slopy Plasmoid Tapphouse"),
            "4": Door("The 2nd GiffHammer Weapon Shop"),
            "5": Door("The 2nd Gadabout Bakery"),
            "6": Door("The 2nd Githspender St"),
            "7": Door("The 2nd Town Hall"),
            "8": Door("The 2nd Thieves Guild"),
            "9": Door("The 2nd Watch Castle"),
            "10": Door("The Old 2nd Manor"),
            "11": Door("Teleportation Deck"),
            "12": Door("3rd Teleportation Deck"),
        },
        "creatures stats": [
            creature(
                "hull leech",
                15,
                2,
                [item("spike", "weapon", 1)],
                "A barnacle-like creature that is attached to the hull of the ship",
                "You see a spike on a tentacle stabed through the hull of the ship",
                creature_type("plant"),
            ),
        ],
        "info": """

You charter a ship, and the Captain says: "You can go anywhere you like before you land back on this here asteriod!"

Do you want to:
1. Go to the Teleportation Deck.
2. Go to The Dancing Jellyfish Inn.
3. Go to The Slopy Plasmoid Tapphouse.
4. Go to The GiffHammer Weapon Shop.
5. Go to The Gadabout Bakery.
6. Go to The Githspender St.
7. Go to The Town Hall.
8. Go to The Thieves Guild.
9. Go to The Watch Castle.
10. Go to The Old Manor.
11. Go to The 1st Asteriod.
12. Go to The 3rd Asteriod.""",
    },
    "The 2nd Dancing Jellyfish Inn": {
        "room type": "asteroid-2",
        "directions": {
            "1": Door("2nd Teleportation Deck"),
            "2": Door("The 2nd Slopy Plasmoid Tapphouse"),
            "3": Door("The 2nd GiffHammer Weapon Shop"),
            "4": Door("The 2nd Gadabout Bakery"),
            "5": Door("The 2nd Githspender St"),
            "6": Door("The 2nd Town Hall"),
            "7": Door("The 2nd Thieves Guild"),
            "8": Door("The 2nd Watch Castle"),
            "9": Door("The 2nd Old Manor"),
        },
        "info": """

do you want to:
1. Go to the Teleportation Deck.
2. Go to The Slopy Plasmoid Tapphouse.
3. Go to The GiffHammer Weapon Shop.
4. Go to The Gadabout Bakery.
5. Go to The Shifterspender St.
6. Go to The Town Hall.
7. Go to The Thieves Guild.
8. Go to The Watch Castle.
9. Go to The Old Manor.""",
    },
    "The 2nd Slopy Plasmoid Tapphouse": {
        "room type": "asteroid-2",
        "directions": {
            "1": Door("2nd Teleportation Deck"),
            "2": Door("The 2nd Dancing Jellyfish Inn"),
            "3": Door("The 2nd GiffHammer Weapon Shop"),
            "4": Door("The 2nd Gadabout Bakery"),
            "5": Door("The 2nd Githspender St"),
            "6": Door("The 2nd Town Hall"),
            "7": Door("The 2nd Thieves Guild"),
            "8": Door("The 2nd Watch Castle"),
            "9": Door("The 2nd Old Manor"),
        },
        "info": """

do you want to:
1. Go to the Teleportation Deck.
2. Go to The Dancing Jellyfish Inn.
3. Go to The GiffHammer Weapon Shop.
4. Go to The Gadabout Bakery.
5. Go to The Githspender St.
6. Go to The Town Hall.
7. Go to The Thieves Guild.
8. Go to The Watch Castle.
9. Go to The Old Manor.""",
    },
    "The 2nd GiffHammer Weapon Shop": {
        "room type": "asteroid-2",
        "directions": {
            "1": Door("2nd Teleportation Deck"),
            "2": Door("The 2nd Dancing Jellyfish Inn"),
            "3": Door("The 2nd Slopy Plasmoid Tapphouse"),
            "4": Door("The 2nd Gadabout Bakery"),
            "5": Door("The 2nd Githspender St"),
            "6": Door("The 2nd Town Hall"),
            "7": Door("The 2nd Thieves Guild"),
            "8": Door("The 2nd Watch Castle"),
            "9": Door("The 2nd Old Manor"),
        },
        "info": """

do you want to:
1. Go to the Teleportation Deck.
2. Go to The Dancing Jellyfish Inn.
3. Go to The Slopy Plasmoid Tapphouse.
4. Go to The Gadabout Bakery.
5. Go to The Githspender St.
6. Go to The Town Hall.
7. Go to The Thieves Guild.
8. Go to The Watch Castle.
9. Go to The Old Manor.""",
    },
    "The 2nd Gadabout Bakery": {
        "room type": "asteroid-2",
        "directions": {
            "1": Door("2nd Teleportation Deck"),
            "2": Door("The 2nd Dancing Jellyfish Inn"),
            "3": Door("The 2nd Slopy Plasmoid Tapphouse"),
            "4": Door("The 2nd GiffHammer Weapon Shop"),
            "5": Door("The 2nd Githspender St"),
            "6": Door("The 2nd Town Hall"),
            "7": Door("The 2nd Thieves Guild"),
            "8": Door("The 2nd Watch Castle"),
            "9": Door("The 2nd Old Manor"),
        },
        "info": """

do you want to:
1. Go to the Teleportation Deck.
2. Go to The Dancing Jellyfish Inn.
3. Go to The Slopy Plasmoid Tapphouse.
4. Go to The GiffHammer Weapon Shop.
5. Go to The Githspender St.
6. Go to The Town Hall.
7. Go to The Thieves Guild.
8. Go to The Watch Castle.
9. Go to The Old Manor.""",
    },
    "The 2nd Githspender St": {
        "room type": "asteroid-2",
        "directions": {
            "1": Door("2nd Teleportation Deck"),
            "2": Door("The 2nd Dancing Jellyfish Inn"),
            "3": Door("The 2nd Slopy Plasmoid Tapphouse"),
            "4": Door("The 2nd GiffHammer Weapon Shop"),
            "5": Door("The 2nd Gadabout Bakery"),
            "6": Door("The 2nd Town Hall"),
            "7": Door("The 2nd Thieves Guild"),
            "8": Door("The 2nd Watch Castle"),
            "9": Door("The 2nd Old Manor"),
        },
        "info": """

do you want to:
1. Go to the Teleportation Deck.
2. Go to The Dancing Jellyfish Inn.
3. Go to The Slopy Plasmoid Tapphouse.
4. Go to The GiffHammer Weapon Shop.
5. Go to The Gadabout Bakery.
6. Go to The Town Hall.
7. Go to The Thieves Guild.
8. Go to The Watch Castle.
9. Go to The Old Manor.""",
    },
    "The 2nd Town Hall": {
        "room type": "asteroid-2",
        "directions": {
            "1": Door("2nd Teleportation Deck"),
            "2": Door("The 2nd Dancing Jellyfish Inn"),
            "3": Door("The 2nd Slopy Plasmoid Tapphouse"),
            "4": Door("The 2nd GiffHammer Weapon Shop"),
            "5": Door("The 2nd Gadabout Bakery"),
            "6": Door("The 2nd Githspender St"),
            "7": Door("The 2nd Thieves Guild"),
            "8": Door("The 2nd Watch Castle"),
            "9": Door("The 2nd Old Manor"),
        },
        "info": """

do you want to:
1. Go to the Teleportation Deck.
2. Go to The Dancing Jellyfish Inn.
3. Go to The Slopy Plasmoid Tapphouse.
4. Go to The GiffHammer Weapon Shop.
5. Go to The Gadabout Bakery.
6. Go to The Githspender St.
7. Go to The Thieves Guild.
8. Go to The Watch Castle.
9. Go to The Old Manor.""",
    },
    "The 2nd Thieves Guild": {
        "room type": "asteroid-2",
        "directions": {
            "1": Door("2nd Teleportation Deck"),
            "2": Door("The 2nd Dancing Jellyfish Inn"),
            "3": Door("The 2nd Slopy Plasmoid Tapphouse"),
            "4": Door("The 2nd GiffHammer Weapon Shop"),
            "5": Door("The 2nd Gadabout Bakery"),
            "6": Door("The 2nd Githspender St"),
            "7": Door("The 2nd Town Hall"),
            "8": Door("The 2nd Watch Castle"),
            "9": Door("The 2nd Old Manor"),
        },
        "creatures stats": [
            creature(
                "thief",
                10,
                4,
                [item("knife", "weapon", 2), item("money-pouch", "valuable", 25)],
                "A hooded 5ft 11 humanoid thief, thief level 3",
                "You see a thief at the door",
                creature_type("humanoid", "cowfolk"),
            ),
        ],
        "info": """

do you want to:
1. Go to the Teleportation Deck.
2. Go to The Dancing Jellyfish Inn.
3. Go to The Slopy Plasmoid Tapphouse.
4. Go to The GiffHammer Weapon Shop.
5. Go to The Gadabout Bakery.
6. Go to The Githspender St.
7. Go to The Town Hall.
8. Go to The Watch Castle.
9. Go to The Old Manor.""",
    },
    "The 2nd Watch Castle": {
        "room type": "asteroid-2",
        "directions": {
            "1": Door("2nd Teleportation Deck"),
            "2": Door("The 2nd Dancing Jellyfish Inn"),
            "3": Door("The 2nd Slopy Plasmoid Tapphouse"),
            "4": Door("The 2nd GiffHammer Weapon Shop"),
            "5": Door("The 2nd Gadabout Bakery"),
            "6": Door("The 2nd Githspender St"),
            "7": Door("The 2nd Town Hall"),
            "8": Door("The 2nd Thieves Guild"),
            "9": Door("The 2nd Old Manor"),
        },
        "info": """

do you want to:
1. Go to the Teleportation Deck.
2. Go to The Dancing Jellyfish Inn.
3. Go to The Slopy Plasmoid Tapphouse.
4. Go to The GiffHammer Weapon Shop.
5. Go to The Gadabout Bakery.
6. Go to The Githspender St.
7. Go to The Town Hall.
8. Go to The Thieves Guild.
9. Go to The Old Manor.""",
    },
    "The 2nd Old Manor": {
        "room type": "asteroid-2",
        "directions": {
            "1": Door("2nd Teleportation Deck"),
            "2": Door("The 2nd Dancing Jellyfish Inn"),
            "3": Door("The 2nd Slopy Plasmoid Tapphouse"),
            "4": Door("The 2nd GiffHammer Weapon Shop"),
            "5": Door("The 2nd Gadabout Bakery"),
            "6": Door("The 2nd Githspender St"),
            "7": Door("The 2nd Town Hall"),
            "8": Door("The 2nd Thieves Guild"),
            "9": Door("The 2nd Watch Castle"),
        },
        "info": """

do you want to:
1. Go to the Teleportation Deck.
2. Go to The Dancing Jellyfish Inn.
3. Go to The Slopy Plasmoid Tapphouse.
4. Go to The GiffHammer Weapon Shop.
5. Go to The Gadabout Bakery.
6. Go to The Githspender St.
7. Go to The Town Hall.
8. Go to The Thieves Guild.
9. Go to The Watch Castle.""",
    },
    "3rd Teleportation Deck": {
        "room type": "asteroid-2",
        "directions": {
            "1": Door("Charter 3rd Ship"),
            "2": Door("The Main Guildhall"),
            "3": Door("The Order of the Arcane Scribes"),
            "4": Door("The Wayfarers' Brotherhood"),
            "5": Door("The Artisans' Collective"),
            "6": Door("The Silent Shadows Syndicate"),
            "7": Door("The Guardians of the Wilds"),
            "8": Door("The Mercantile Consortium"),
            "9": Door("The Sentinels of the Shield"),
        },
        "10": Door("The 3rd Old Manor"),
        "info": """
You are in a strange cave with many teleportation circles, as well as some ships that are floating above the floor.

Out of the gap in the side of the cave it looks black with a few twinkles of light.
There is a sign on the wall. It is a map of a city on an asteriod.
The main locations are: The Teleportation Deck, The Dancing Jellyfish Inn, The Slopy Plasmoid Tapphouse, The GiffHammer Weapon Shop, The Gadabout Bakery, The Githspender Store,
The Town Hall, The Thieves Guild, The Watch Castle, and The Old Manor.
do you want to:
1. Charter a ship away.
2. Go to The Main Guildhall.
3. Go to The Magic Guild.
4. Go to The Explorers' Guild.
5. Go to The Craftsmen's Guild.
6. Go to The Stealth Guild.
7. Go to The Nature Guild.
8. Go to The Trade Guild.
9. Go to The Watch Castle.
10. Go to The Old Manor.""",
    },
    "Charter 3rd Ship": {
        "room type": "asteroid-3",
        "directions": {
            "1": Door("Teleportation Deck"),
            "2": Door("The Main Guildhall"),
            "3": Door("The Order of the Arcane Scribes"),
            "4": Door("The Wayfarers' Brotherhood"),
            "5": Door("The Artisans' Collective"),
            "6": Door("The Silent Shadows Syndicate"),
            "7": Door("The Guardians of the Wilds"),
            "8": Door("The Mercantile Consortium"),
            "9": Door("The Sentinels of the Shield"),
            "10": Door("The 3rd Old Manor"),
            "11": Door("Teleportation Deck"),
            "12": Door("2nd Teleportation Deck"),
        },
        "info": """

You charter a ship, and the Captain says: "You can go anywhere you like before you land back on this here asteriod!"

Do you want to:
1. Go to The Teleportation Deck.
2. Go to The Main Guildhall.
3. Go to The Magic Guild.
4. Go to The Explorers' Guild.
5. Go to The Craftsmen's Guild.
6. Go to The Stealth Guild.
7. Go to The Nature Guild.
8. Go to The Trade Guild.
9. Go to The Guards Guild.
10. Go to The Old Manor.
11. Go to The 1st Asteriod.
12. Go to The 2nd Asteriod.""",
    },
    "The Main Guildhall": {
        "description": """
The Forge of Heroes

Theme: Valor and Heroism
Purpose: The Forge of Heroes is a legendary guildhall dedicated to the training, inspiration, and celebration of heroes. Its towering spires and majestic architecture evoke a sense of awe and 
reverence, inspiring all who enter to aspire to greatness. Within its hallowed halls, aspiring adventurers undergo rigorous training regimes, learning the arts of combat, leadership, and 
selflessness under the guidance of seasoned mentors and legendary champions. In addition to training, the Forge also serves as a repository of heroic deeds, with its walls adorned with 
tapestries, statues, and artifacts commemorating the triumphs of the past. Whether preparing for epic quests, honing their skills in the arena, or seeking guidance from wise sages, heroes 
from across the realm flock to the Forge, drawn by the promise of glory and the chance to make their mark on history.""",
        "room type": "asteroid-3",
        "directions": {
            "1": Door("2nd Teleportation Deck"),
            "2": Door("The Order of the Arcane Scribes"),
            "3": Door("The Wayfarers' Brotherhood"),
            "4": Door("The Artisans' Collective"),
            "5": Door("The Silent Shadows Syndicate"),
            "6": Door("The Guardians of the Wilds"),
            "7": Door("The Mercantile Consortium"),
            "8": Door("The Sentinels of the Shield"),
            "9": Door("The 3rd Old Manor"),
            "10": Door("The Grand Coliseum"),
        },
        "info": """

do you want to:
1. Go to The Teleportation Deck.
2. Go to The Magic Guild.
3. Go to The Explorers' Guild.
4. Go to The Craftsmen's Guild.
5. Go to The Stealth Guild.
6. Go to The Nature Guild.
7. Go to The Trade Guild.
8. Go to The Guards Guild.
9. Go to The Old Manor.
10. Go to The Arena""",
    },
    "The Grand Coliseum": {
        "description": """
The Grand Coliseum

Theme: Gladiatorial Combat and Spectacle
Purpose: The Grand Coliseum is an ancient and revered arena where warriors from across the realm come to test their mettle in epic battles of skill and strength. Its towering walls and 
majestic architecture evoke the grandeur of a bygone era, harkening back to a time when gladiators fought for glory and the adulation of the masses. Within its vast amphitheater, spectators 
from all walks of life gather to witness the spectacle of combat, cheering on their favorite champions and reveling in the excitement of the arena. But the Grand Coliseum is more than just a 
venue for bloodsport—it is a symbol of honor, valor, and the indomitable spirit of competition. Warriors who prove themselves in the crucible of the arena earn not only fame and fortune but 
also the respect of their peers and the adoration of the crowds. Whether battling for supremacy in one-on-one duels, facing off against fearsome beasts in savage contests, or participating in 
elaborate tournaments of skill and strategy, the fighters of the Grand Coliseum embody the virtues of courage, determination, and resilience. As the premier arena of its kind, the Grand 
Coliseum stands as a testament to the enduring appeal of gladiatorial combat and the timeless allure of the warrior's path.""",
        "room type": "asteroid-3",
        "directions": {
            "1": Door("The Main Guildhall"),
        },
        "creatures stats": [
            creature(
                "gladiator",
                15,
                6,
                [item("longsword", "weapon", 4)],
                "A large 6ft 7 humaniod gladiator",
                'As you enter the Arena a hulking gladiator walks up to you and says: "You sould run while you still can or face me!"',
                creature_type("humaniod", "goliath"),
            ),
        ],
        "info": """

do you want to:
1. Go to The The Main Guildhall.""",
    },
    "The Order of the Arcane Scribes": {
        "description": """
Order of the Arcane Scribes

Theme: Magic and Knowledge
Purpose: The Order of the Arcane Scribes is a venerable guild steeped in the mysteries of magic and the pursuit of knowledge. Comprised of wizards, scholars, and scribes, their primary mission
is the preservation, study, and advancement of the arcane arts. Within their ancient guildhall, which stands as a testament to centuries of magical scholarship, members pore over ancient 
tomes, decipher cryptic runes, and experiment with new spells. Their work encompasses a wide range of magical disciplines, from elemental manipulation to divination and healing magic. Beyond 
their scholarly pursuits, the Order also offers magical services to the community, providing everything from enchantments and potion brewing to mystical consultations and magical education. 
Whether delving into the depths of forgotten lore or harnessing the power of the elements, the Arcane Scribes are dedicated to unraveling the secrets of the cosmos and mastering the forces of 
magic.""",
        "room type": "asteroid-3",
        "directions": {
            "1": Door("3rd Teleportation Deck"),
            "2": Door("The Main Guildhall"),
            "3": Door("The Wayfarers' Brotherhood"),
            "4": Door("The Artisans' Collective"),
            "5": Door("The Silent Shadows Syndicate"),
            "6": Door("The Guardians of the Wilds"),
            "7": Door("The Mercantile Consortium"),
            "8": Door("The Sentinels of the Shield"),
            "9": Door("The 3rd Old Manor"),
        },
        "info": """

do you want to:
1. Go to the Teleportation Deck.
2. Go to The Main Guildhall.
3. Go to The Explorers' Guild.
4. Go to The Craftsmen's Guild.
5. Go to The Stealth Guild.
6. Go to The Nature Guild.
7. Go to The Trade Guild.
8. Go to The Guards Guild.
9. Go to The Old Manor.""",
    },
    "The Wayfarers' Brotherhood": {
        "description": """
Wayfarers' Brotherhood

Theme: Exploration and Adventure
Purpose: The Wayfarers' Brotherhood is a renowned guild of intrepid adventurers, explorers, and seekers of the unknown. Theirs is a life dedicated to the thrill of discovery, the pursuit of 
treasure, and the exploration of uncharted realms. From the towering peaks of distant mountains to the depths of forgotten dungeons, members of the Wayfarers' Brotherhood traverse the world in 
search of adventure and fortune. Their guildhall, a bustling hub of activity and excitement, serves as a meeting place for like-minded individuals to share tales of daring exploits, plan 
ambitious expeditions, and seek companions for their journeys. Guided by a spirit of curiosity and a thirst for discovery, the Wayfarers embody the adventurous spirit of exploration, ever 
eager to uncover the mysteries that lie beyond the horizon.""",
        "room type": "asteroid-3",
        "directions": {
            "1": Door("3rd Teleportation Deck"),
            "2": Door("The Main Guildhall"),
            "3": Door("The Order of the Arcane Scribes"),
            "4": Door("The Artisans' Collective"),
            "5": Door("The Silent Shadows Syndicate"),
            "6": Door("The Guardians of the Wilds"),
            "7": Door("The Mercantile Consortium"),
            "8": Door("The Sentinels of the Shield"),
            "9": Door("The 3rd Old Manor"),
        },
        "info": """

do you want to:
1. Go to the Teleportation Deck.
2. Go to The Main Guildhall.
3. Go to The Magic Guild.
4. Go to The Craftsmen's Guild.
5. Go to The Stealth Guild.
6. Go to The Nature Guild.
7. Go to The Trade Guild.
8. Go to The Guards Guild.
9. Go to The Old Manor.""",
    },
    "The Artisans' Collective": {
        "description": """
Artisans' Collective

Theme: Craftsmanship and Creativity
Purpose: The Artisans' Collective is a guild dedicated to the celebration of craftsmanship, creativity, and the pursuit of artistic excellence. Within their bustling guildhall, master 
artisans, craftsmen, and artists of all disciplines gather to hone their skills, showcase their creations, and inspire one another with their passion for their craft. From the ringing of 
anvils in the blacksmith's forge to the delicate brushstrokes of the painter's canvas, members of the Artisans' Collective excel in a diverse array of trades and artistic endeavors. Their 
guildhall doubles as a vibrant workshop and gallery, where members collaborate on projects, share techniques, and exhibit their finest works to the public. Whether forging weapons of legendary 
quality, crafting intricate works of jewelry, or painting breathtaking landscapes, the Artisans' Collective stands as a testament to the enduring power of creativity and the transformative 
potential of skilled craftsmanship.""",
        "room type": "asteroid-3",
        "directions": {
            "1": Door("3rd Teleportation Deck"),
            "2": Door("The Main Guildhall"),
            "3": Door("The Order of the Arcane Scribes"),
            "4": Door("The Wayfarers' Brotherhood"),
            "5": Door("The Silent Shadows Syndicate"),
            "6": Door("The Guardians of the Wilds"),
            "7": Door("The Mercantile Consortium"),
            "8": Door("The Sentinels of the Shield"),
            "9": Door("The 3rd Old Manor"),
        },
        "info": """

do you want to:
1. Go to the Teleportation Deck.
2. Go to The Main Guildhall.
3. Go to The Magic Guild.
4. Go to The Explorers' Guild.
5. Go to The Stealth Guild.
6. Go to The Nature Guild.
7. Go to The Trade Guild.
8. Go to The Guards Guild.
9. Go to The Old Manor.""",
    },
    "The Silent Shadows Syndicate": {
        "description": """
Silent Shadows Syndicate

Theme: Stealth and Subterfuge
Purpose: Operating from the shadows, the Silent Shadows Syndicate is a clandestine guild of spies, thieves, and assassins who specialize in the arts of stealth, subterfuge, and infiltration. 
Their clandestine operations span the realms of espionage, sabotage, and intelligence gathering, making them a formidable force in the world of intrigue. Within their secretive guildhall, 
concealed from prying eyes and hidden from public view, members of the Syndicate plot and scheme, carrying out covert missions on behalf of their clients or furthering their own clandestine 
agendas. Masters of disguise, experts in surveillance, and lethal in combat, the members of the Silent Shadows Syndicate operate with precision and finesse, striking swiftly and decisively 
before melting back into the shadows from whence they came. Though their methods may be controversial, their services are in high demand by those who require the services of skilled operatives 
willing to operate outside the boundaries of conventional morality.""",
        "room type": "asteroid-3",
        "directions": {
            "1": Door("3rd Teleportation Deck"),
            "2": Door("The Main Guildhall"),
            "3": Door("The Order of the Arcane Scribes"),
            "4": Door("The Wayfarers' Brotherhood"),
            "5": Door("The Artisans' Collective"),
            "6": Door("The Guardians of the Wilds"),
            "7": Door("The Mercantile Consortium"),
            "8": Door("The Sentinels of the Shield"),
            "9": Door("The 3rd Old Manor"),
        },
        "info": """

do you want to:
1. Go to the Teleportation Deck.
2. Go to The Main Guildhall.
3. Go to The Magic Guild.
4. Go to The Explorers' Guild.
5. Go to The Craftsmen's Guild.
6. Go to The Nature Guild.
7. Go to The Trade Guild.
8. Go to The Guards Guild.
9. Go to The Old Manor.""",
    },
    "The Guardians of the Wilds": {
        "description": """
Guardians of the Wilds

Theme: Nature and Conservation
Purpose: The Guardians of the Wilds are a dedicated guild of druids, rangers, and nature enthusiasts who have devoted themselves to the protection and preservation of the natural world. Deeply 
connected to the land and its inhabitants, members of the Guardians of the Wilds serve as stewards of the wilderness, safeguarding forests, rivers, and mountains from the depredations of 
civilization and the encroachment of dark forces. Within their secluded guildhall, nestled amidst the ancient trees of a sacred grove, members commune with nature, honing their connection to 
the primal forces that sustain all life. Through their efforts, they seek to promote harmony between civilization and the wild, advocating for sustainable practices and opposing those who 
would exploit nature for profit or power. Whether embarking on quests to thwart the schemes of eco-terrorists, guiding travelers through treacherous terrain, or tending to the needs of injured 
wildlife, the Guardians of the Wilds stand as vigilant protectors of the natural world, sworn to defend it against all who would seek to do it harm.""",
        "room type": "asteroid-3",
        "directions": {
            "1": Door("3rd Teleportation Deck"),
            "2": Door("The Main Guildhall"),
            "3": Door("The Order of the Arcane Scribes"),
            "4": Door("The Wayfarers' Brotherhood"),
            "5": Door("The Artisans' Collective"),
            "6": Door("The Silent Shadows Syndicate"),
            "7": Door("The Mercantile Consortium"),
            "8": Door("The Sentinels of the Shield"),
            "9": Door("The 3rd Old Manor"),
        },
        "info": """

do you want to:
1. Go to the Teleportation Deck.
2. Go to The Main Guildhall.
3. Go to The Magic Guild.
4. Go to The Explorers' Guild.
5. Go to The Craftsmen's Guild.
6. Go to The Stealth Guild.
7. Go to The Trade Guild.
8. Go to The Guards Guild.
9. Go to The Old Manor.""",
    },
    "The Mercantile Consortium": {
        "description": """
Mercantile Consortium

Theme: Trade and Commerce
Purpose: The Mercantile Consortium is a formidable guild of merchants, traders, and entrepreneurs who wield considerable influence in the realm of commerce and finance. Their sprawling network 
of trade routes, marketplaces, and financial institutions spans continents, facilitating the flow of goods, wealth, and information across the known world. Within their opulent guildhall, a 
bustling nexus of commerce and negotiation, members of the Consortium broker lucrative deals, negotiate favorable terms, and vie for dominance in the cutthroat world of business. Masters of 
strategy, experts in logistics, and adept at navigating the complexities of international trade, members of the Mercantile Consortium are driven by a relentless pursuit of profit and power. 
Though their methods may be ruthless and their ambitions vast, their guild stands as a pillar of the global economy, shaping the course of history through the power of commerce and the pursuit 
of wealth.""",
        "room type": "asteroid-3",
        "directions": {
            "1": Door("3rd Teleportation Deck"),
            "2": Door("The Main Guildhall"),
            "3": Door("The Order of the Arcane Scribes"),
            "4": Door("The Wayfarers' Brotherhood"),
            "5": Door("The Artisans' Collective"),
            "6": Door("The Silent Shadows Syndicate"),
            "7": Door("The Guardians of the Wilds"),
            "8": Door("The Sentinels of the Shield"),
            "9": Door("The 3rd Old Manor"),
        },
        "info": """

do you want to:
1. Go to the Teleportation Deck.
2. Go to The Main Guildhall.
3. Go to The Magic Guild.
4. Go to The Explorers' Guild.
5. Go to The Craftsmen's Guild.
6. Go to The Stealth Guild.
7. Go to The Trade Guild.
8. Go to The Guards Guild.
9. Go to The Old Manor.""",
    },
    "The Sentinels of the Shield": {
        "description": """
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
new recruits, fostering a sense of camaraderie and unity among the ranks.""",
        "room type": "asteroid-3",
        "directions": {
            "1": Door("3rd Teleportation Deck"),
            "2": Door("The Main Guildhall"),
            "3": Door("The Order of the Arcane Scribes"),
            "4": Door("The Wayfarers' Brotherhood"),
            "5": Door("The Artisans' Collective"),
            "6": Door("The Silent Shadows Syndicate"),
            "7": Door("The Guardians of the Wilds"),
            "8": Door("The Mercantile Consortium"),
            "9": Door("The 3rd Old Manor"),
        },
        "info": """

do you want to:
1. Go to the Teleportation Deck.
2. Go to The Main Guildhall.
3. Go to The Magic Guild.
4. Go to The Explorers' Guild.
5. Go to The Craftsmen's Guild.
6. Go to The Stealth Guild.
7. Go to The Nature Guild.
8. Go to The Trade Guild.
9. Go to The Old Manor.""",
    },
    "The 3rd Old Manor": {
        "room type": "asteroid-3",
        "directions": {
            "1": Door("3rd Teleportation Deck"),
            "2": Door("The Main Guildhall"),
            "3": Door("The Order of the Arcane Scribes"),
            "4": Door("The Wayfarers' Brotherhood"),
            "5": Door("The Artisans' Collective"),
            "6": Door("The Silent Shadows Syndicate"),
            "7": Door("The Guardians of the Wilds"),
            "8": Door("The Mercantile Consortium"),
            "9": Door("The Sentinels of the Shield"),
        },
        "info": """

do you want to:
1. Go to the Teleportation Deck.
2. Go to The Main Guildhall.
3. Go to The Magic Guild.
4. Go to The Explorers' Guild.
5. Go to The Craftsmen's Guild.
6. Go to The Stealth Guild.
7. Go to The Nature Guild.
8. Go to The Trade Guild.
9. Go to The Guards Guild.""",
    },
}
