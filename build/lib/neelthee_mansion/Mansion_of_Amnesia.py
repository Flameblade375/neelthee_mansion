from .Rooms import *
from .creatures import *
from .items import *
from .Quests import *
from .all_game_utils import *


GameState = {
    'Enemys killed': 0,
    'collected items': [],
}


'''
Neel-thee's Mansion of Amnesia
'''

global player, evil_mage, commands, NOTE_NUM, LAST_ROOM, CURRENTROOM, credits, characters, color_coding, quest_manager

quest_manager = QuestManager()

color_coding = False

credits = '''
Made by: Alexander.E.F'''

# start the player in the Hall
CURRENTROOM = 'Hall'

LAST_ROOM = CURRENTROOM

name = ''
age = 0
height = Height()
weight = 0


charactersList = [
    {'name': 'Jack', 'age': 19, 'height': Height('6ft 3'), 'weight(LBs)': 213}, 
    {'name': 'Darcie-Mae', 'age': 19, 'height': Height('5ft 5'), 'weight(LBs)': 150}, 
    {'name': 'John', 'age': 25, 'height': Height('5ft 10'), 'weight(LBs)': 180}, 
    {'name': 'Emily', 'age': 22, 'height': Height('5ft 6'), 'weight(LBs)': 135}, 
    {'name': 'William', 'age': 30, 'height': Height('6ft 1'), 'weight(LBs)': 200}, 
    {'name': 'Samantha', 'age': 28, 'height': Height('5ft 8'), 'weight(LBs)': 155}, 
    {'name': 'Mark', 'age': 23, 'height': Height('5ft 11'), 'weight(LBs)': 185}, 
    {'name': 'Alex', 'age': 27, 'height': Height('6ft 0'), 'weight(LBs)': 190}, 
    {'name': 'Sarah', 'age': 20, 'height': Height('5ft 4'), 'weight(LBs)': 125}, 
    {'name': 'Natalie', 'age': 24, 'height': Height('5ft 7'), 'weight(LBs)': 140}, 
    {'name': 'Michael', 'age': 32, 'height': Height('6ft 2'), 'weight(LBs)': 200}, 
    {'name': 'Liam', 'age': 29, 'height': Height('5ft 10'), 'weight(LBs)': 180}, 
    {'name': 'James', 'age': 25, 'height': Height('6ft 1'), 'weight(LBs)': 195}, 
    {'name': 'Emma', 'age': 22, 'height': Height('5ft 6'), 'weight(LBs)': 130}, 
    {'name': 'Olivia', 'age': 26, 'height': Height('5ft 8'), 'weight(LBs)': 135}, 
    {'name': 'Sophia', 'age': 28, 'height': Height('5ft 5'), 'weight(LBs)': 145}, 
    {'name': 'Daniel', 'age': 28, 'height': Height('6ft 0'), 'weight(LBs)': 180}, 
    {'name': 'Matthew', 'age': 31, 'height': Height('5ft 11'), 'weight(LBs)': 175}, 
    {'name': 'Jennifer', 'age': 25, 'height': Height('5ft 6'), 'weight(LBs)': 140}, 
    {'name': 'Hannah', 'age': 23, 'height': Height('5ft 4'), 'weight(LBs)': 130}, 
    {'name': 'Isabella', 'age': 24, 'height': Height('5ft 4'), 'weight(LBs)': 132}, 
    {'name': 'Jake', 'age': 29, 'height': Height('5ft 6'), 'weight(LBs)': 140}, 
    {'name': 'Zack', 'age': 21, 'height': Height('5ft 5'), 'weight(LBs)': 125}, 
    {'name': 'Lucy', 'age': 27, 'height': Height('5ft 7'), 'weight(LBs)': 135}, 
    {'name': 'Mia', 'age': 25, 'height': Height('5ft 3'), 'weight(LBs)': 128}, 
    {'name': 'Brandon', 'age': 30, 'height': Height('6ft 1'), 'weight(LBs)': 180}, 
    {'name': 'Ethan', 'age': 28, 'height': Height('6ft 0'), 'weight(LBs)': 175}, 
    {'name': 'Andrew', 'age': 28, 'height': Height('6ft 0'), 'weight(LBs)': 175}, 
    {'name': 'Nathan', 'age': 26, 'height': Height('5ft 10'), 'weight(LBs)': 165}, 
    {'name': 'David', 'age': 22, 'height': Height('6ft 2'), 'weight(LBs)': 185},
    {'name': 'Noah', 'age': 25, 'height': Height('5ft 11'), 'weight(LBs)': 175},
    {'name': 'Aiden', 'age': 30, 'height': Height('6ft 0'), 'weight(LBs)': 180},
    {'name': 'Lucas', 'age': 28, 'height': Height('5ft 10'), 'weight(LBs)': 170},
    {'name': 'Ava', 'age': 22, 'height': Height('5ft 5'), 'weight(LBs)': 130},
    {'name': 'Lily', 'age': 26, 'height': Height('5ft 6'), 'weight(LBs)': 135},
    {'name': 'Grace', 'age': 29, 'height': Height('5ft 7'), 'weight(LBs)': 140}
]
    
    
evil_mage = PC(
    'Neel-thee Contozt', 
    19836, 
    'Mage', 
    29, 
    'Evil prince', 
    Height('5ft 7.375'), 
    222, 
    xp=99180, 
)


# Function to parse command
def parse_command(command_str: str, commands: dict):
    # Split the command string into parts
    parts = command_str.split()
    
    # Check for multi-word commands
    for cmd in commands.keys():
        cmd_parts = cmd.split()
        if len(cmd_parts) > 1 and parts[:len(cmd_parts)] == cmd_parts:
            action = ' '.join(cmd_parts)
            targets = parts[len(cmd_parts):]
            return action, targets
    
    # Default single word command
    action = parts[0]
    targets = parts[1:] if len(parts) > 1 else []
    return action, targets



def showInstructions():
    # Display the game instructions
    type_text('''
===========================
Commands:
go [%*GREEN*%direction%*RESET*%/%*GREEN*%teleport%*RESET*%/%*GREEN*%number%*RESET*%] - Move to another location
get [%*BLUE*%item%*RESET*%] - Pick up an item from your current location
search [the/] [%*RED*%container%*RESET*%] - Search a container in your current location
use [%*BLUE*%item%*RESET*%] - Use an item from your inventory
put [%*BLUE*%item%*RESET*%] [the/] [%*RED*%container%*RESET*%] - Put an item from your inventory into a container in your current location
sleep - Rest for a bit and regain some health
look - Look around your current location
quit - Quit the game
help - Show these instructions
hint - Get a random hint for your current location
map - Display the map of places you have been to
''', colorTrue=color_coding)


def showHint():
    if 'Hints' in ROOMS[CURRENTROOM]:
        type_text("You think:", colorTrue=color_coding)
        hint = choice(ROOMS[CURRENTROOM]['Hints'])
        type_text(hint, colorTrue=color_coding)
    else:
        type_text("You can't think of anything", colorTrue=color_coding)

def check_direction(var: str, directions: list):
    for direction in directions:
        if var == direction:
            return True
    return False


def End(text: str, win: bool = True):
    type_text(text, colorTrue=color_coding)
    if win:
        type_text('Do you want to leave the game? Y/N', colorTrue=color_coding)
        while True:
            leave = input('>').lower()
            if leave == 'n':
                type_text('You decide to continue exploring.', colorTrue=color_coding)
                break
            elif leave == 'y':
                type_text('You escaped the house... %*BOLD*%GAME OVER, YOU WIN!', colorTrue=color_coding)
                commands["quit"]()
            else:
                type_text("Sorry, that wasn't 'y' or 'n'. Please enter 'y' or 'n'.", colorTrue=color_coding)
    else:
        type_text('%*BOLD*%GAME OVER, YOU LOSE!', colorTrue=color_coding)
        commands["quit"]()


NOTE_NUM = 0


def add_note(note, parchment_index=None):
    player.NOTES.append(note)
    NOTE_NUM += 1
    inv_note = 'note ' + str(NOTE_NUM)
    try:
        del player.inventory[parchment_index]
    except IndexError:
        pass
    player.inventory_add([item(inv_note)])


def Use_grappling_hook():

    def swing_into_forest():
        type_text("You throw your grappling-hook, it catches a branch of a nearby tree and hooks back onto itself. \nYou can swing into the forest!", colorTrue=color_coding)
        if ask_for_consent("Do you want to swing into the forest"):
            type_text("You swing into the forest", colorTrue=color_coding)
            Move('Forest Clearing')
        else:
            type_text("You flick the rope and it unhooks. You continue exploring the house.", colorTrue=color_coding)

    def climb_into_house():
        type_text("You throw your grappling-hook, it catches the railing of the nearby house and hooks back onto itself. \nYou can climb into the house!", colorTrue=color_coding)
        if ask_for_consent("Do you want to climb into the house"):
            type_text("You climb into the house", colorTrue=color_coding)
            Move('Balcony')
        else:
            type_text("You flick the rope and it unhooks. You continue exploring the forest", colorTrue=color_coding)

    if CURRENTROOM == 'Balcony' and 'grappling-hook' in player.inventory:
        swing_into_forest()
    elif CURRENTROOM == 'Forest Clearing' and 'grappling-hook' in player.inventory:
        climb_into_house()


def Use_quill():

    if all(item in player.inventory for item in ['ink-pot', 'parchment', 'quill']):
        parchment_index = player.inventory.index('parchment')
        type_text('What do you want to write', colorTrue=color_coding)
        write = str(input('>')).strip()

        if write:
            add_note(write, parchment_index)
        else:
            type_text("You can't write nothing", colorTrue=color_coding)
    else:
        type_text("You need an ink pot, parchment, and a quill to write.", colorTrue=color_coding)


def Use_note(note_number):
    """Reads a specified note from the player's inventory."""
    note_key = f'note {note_number}'
    if note_key in player.inventory:
        note_index = int(note_number) - 1
        type_text(f'You read:', colorTrue=color_coding)
        type_text(player.NOTES[note_index], colorTrue=color_coding)
    else:
        type_text('You do not have that note', colorTrue=color_coding)


def Use(moveone, movetwo=None):
    """Uses an item from the player's inventory."""
    if moveone in player.inventory:
        item_obj = player.inventory[player.inventory.index(moveone)]
        if isinstance(item_obj, item):
            if item_obj.sell(player):
                type_text(f"You sell the %*BLUE*%{moveone}%*RESET*%", colorTrue=color_coding)
                player.inventory.remove(item_obj.name)
            elif moveone == 'quill':
                Use_quill()
            elif moveone == 'grappling-hook':
                Use_grappling_hook()
    elif moveone == 'note' and movetwo:
        Use_note(movetwo)
    elif moveone == '0':
        type_text("You can't use nothing", colorTrue=color_coding)
    else:
        type_text("You can't use that", colorTrue=color_coding)


def Move(move):
    global CURRENTROOM, LAST_ROOM


    def attempt_charter():
        if player.money >= 10:
            player.money -= 10
            if 'descovered' in ROOMS[newRoom] and not ROOMS[newRoom]['descovered']:
                ROOMS[newRoom]['descovered'] = True
            return ROOMS[CURRENTROOM]['directions'][move]
        else:
            type_text("You don't have enough money to charter a ship.", colorTrue=color_coding)
            return CURRENTROOM

    def attempt_move_to_garden():
        if 'key' in player.inventory:
            End('You unlock the gate to the garden with the key!')
            return newRoom
        else:
            type_text('The gate is locked.', colorTrue=color_coding)
            return newRoom

    def move_to_room():
        global LAST_ROOM
        LAST_ROOM = CURRENTROOM
        if move == '0':
            return attempt_charter()
        elif newRoom == 'Garden':
            if 'descovered' in ROOMS[newRoom] and not ROOMS[newRoom]['descovered']:
                ROOMS[newRoom]['descovered'] = True
            return attempt_move_to_garden()
        else:
            if 'descovered' in ROOMS[newRoom] and not ROOMS[newRoom]['descovered']:
                ROOMS[newRoom]['descovered'] = True
            return newRoom

    if move in ROOMS[CURRENTROOM]['directions']:
        newRoom = ROOMS[CURRENTROOM]['directions'][move]
        CURRENTROOM = move_to_room()
        return
    elif move in ROOMS:
        newRoom = move
        if newRoom == 'Garden':
            CURRENTROOM = attempt_move_to_garden()
        else:
            CURRENTROOM = newRoom
        LAST_ROOM = CURRENTROOM
        return
    type_text("You can't go that way!", colorTrue=color_coding)


def start():
    # type_text a main men, colorTrue=color_codingu
    type_text(f'\nHello %*MAGENTA*%{player.name}%*RESET*% and welcome to my Role Playing Game. \nI hope you have fun!', colorTrue=color_coding)
    showInstructions()


def showStatus():

    # Display player's current status
    text = f'\n---------------------------'
    
    # Display the current inventory
    the_inventory = [itemnum.name for itemnum in player.inventory if isinstance(itemnum, item)]
    text += f'\nInventory: %*BLUE*%{", ".join(the_inventory)}%*RESET*%; Money: {player.money}; XP: {player.xp}; Level: {player.Level}'
    
    # Display possible directions of travel
    text = display_directions(text)

    # Display the map if available
    if 'map' in ROOMS[CURRENTROOM]:
        text += f'\n\nKey: {"; ".join(KEY)}\n'
        text += f'\n{ROOMS[CURRENTROOM]["map"]}\n'

    # Display the description of the current room
    text += ('\n' + str(ROOMS[CURRENTROOM]['info']))

    text += f"\n---------------------------"
    
    type_text(text, colorTrue=color_coding)
    
    # Optionally display additional room description
    if 'description' in ROOMS[CURRENTROOM] and ask_for_consent("Do you want to observe the area"):
        type_text("The area:", colorTrue=color_coding)
        type_text(ROOMS[CURRENTROOM]['description'], colorTrue=color_coding)


def display_directions(text):
    directions = ['north', 'east', 'south', 'west', 'up', 'down', 'teleport']
    direction_descriptions = {
        'house': {
            'north': "There is a door to the",
            'east': "There is a door to the",
            'south': "There is a door to the",
            'west': "There is a door to the",
            'up': "There is a staircase leading",
            'down': "There is a staircase leading"
        },
        'forest': {
            'north': "There is a path to the",
            'east': "There is a path to the",
            'south': "There is a path to the",
            'west': "There is a path to the",
            'up': "There is a ladder going",
            'down': "There is a holl in the ground leading"
        }
    }

    room_type = ROOMS[CURRENTROOM]['room type']
    if room_type in direction_descriptions:
        for direction in directions:
            if direction in ROOMS[CURRENTROOM]['directions']:
                if direction != 'teleport':
                    text += f'\n{direction_descriptions[room_type][direction]} %*GREEN*%{direction}%*RESET*%.'

    if 'teleport' in ROOMS[CURRENTROOM]['directions']:
        text += "\nThere is a %*GREEN*%teleport%*RESET*%ation circle on the ground"

    return text

def battle(player: PC, monster: creature, last_room):
    """
    Simulate a battle between the player and a monster.

    Args:
        player (PC): The player character.
        monster (creature): The monster to battle.
        last_room: The previous room before the battle.

    Returns:
        The monster if it is still alive, None otherwise.
    """
    while player.hp > 0 and monster.hp > 0:
        if ask_for_consent("Do you want to run away"):
            Move(last_room)
            return monster

        player_turn(player, monster)
        
        if monster.hp <= 0:
            handle_victory(player, monster)
            return None

        monster_turn(player, monster)
        
        if player.hp <= 0:
            End(f'The %*CYAN*%{monster.name}%*RESET*% defeats you!', win=False)
            return monster

    return monster

def player_turn(player: PC, monster: creature):
    """
    Handle the player's turn during the battle.

    Args:
        player (PC): The player character.
        monster (creature): The monster to battle.
    """
    player_action = loop_til_valid_input(
        "Choose your action: (attack/defend/special): ", 
        "Invalid action. Please enter a valid action.", 
        PC_action
    ).value.lower()
    
    if player_action == "attack":
        perform_attack(player, monster)
    elif player_action == "defend":
        player.defending = True
        type_text("You brace yourself for the next attack.", colorTrue=color_coding)
    elif player_action == "special":
        use_special_ability(player, monster)

def monster_turn(player: PC, monster: creature):
    """
    Handle the monster's turn during the battle.

    Args:
        player (PC): The player character.
        monster (creature): The monster to battle.
    """
    type_text(f"The %*CYAN*%{monster.name}%*RESET*% attacks!", colorTrue=color_coding)
    damage = calculate_damage(monster, player)
    
    player.take_damage(damage)

def perform_attack(attacker: PC, defender: creature):
    """
    Perform an attack action.

    Args:
        attacker (PC): The attacking character.
        defender (creature): The defending monster.
    """
    damage = calculate_damage(attacker, defender)
    defender.take_damage(damage)

def handle_victory(player: PC, monster: creature):
    """
    Handle the logic when the player defeats the monster.

    Args:
        player (PC): The player character.
        monster (creature): The defeated monster.
    """
    type_text(f"You defeat the %*CYAN*%{monster.name}%*RESET*%!", colorTrue=color_coding)
    player.inventory_add(monster.dropped_items)

def calculate_damage(attacker, defender) -> int:
    """
    Calculate the damage inflicted by the attacker on the defender.

    Args:
        attacker: The attacking character.
        defender: The defending character.

    Returns:
        int: The calculated damage.
    """
    damage_min, damage_max = calculate_damage_range(attacker.atpw)
    damage = randint(damage_min, damage_max)
    
    if random() < attacker.crit_chance:
        damage *= 2
        type_text("Critical hit!", colorTrue=color_coding)
    
    if hasattr(defender, 'defending') and defender.defending:
        damage //= 2
        type_text("The attack is defended, reducing damage.", colorTrue=color_coding)
        defender.defending = False
    
    return damage

def calculate_damage_range(atpw: int) -> tuple[int, int]:
    """
    Calculate the damage range based on attack power.

    Args:
        atpw (int): Attack power of the combatant.

    Returns:
        Tuple[int, int]: Minimum and maximum damage range.
    """
    damage_max_range = randint(1, 3)
    damage_min_range = randint(1, 3)
    damage_min = max(1, atpw - damage_min_range)  # Ensure minimum damage is at least 1
    damage_max = atpw + damage_max_range
    return damage_min, damage_max

def use_special_ability(player: PC, monster: creature):
    """
    Allow the player to use a special ability during combat.

    Args:
        player (PC): The player character.
        monster (creature): The monster being fought.
    """
    if player.special_ability.ready:
        player.special_ability.activate(monster)
        type_text(f"You use your special ability: {player.special_ability.name}.", colorTrue=color_coding)
        player.special_ability.ready = False
    else:
        type_text("Your special ability is not ready yet.", colorTrue=color_coding)


def command():
    try:
        ShouldBreak = False

        while True:
            showStatus()
            user_input = get_player_input(False)

            if user_input:
                commands_list = user_input.split(',')
                for command_str in commands_list:
                    action, targets = parse_command(command_str.strip(), commands)

                    if action in commands:
                        if has_named_arg(commands[action], 'player'):
                            if targets:
                                commands[action](player, *targets)
                            else:
                                commands[action](player)
                        elif targets:
                            commands[action](*targets)
                        else:
                            commands[action]()
                    else:
                        type_text(f"Unknown command '{action}'. Type 'help' for a list of commands.", colorTrue=color_coding)
                    if action in commands:
                        ShouldBreak = True
            if ShouldBreak:
                return
    except KeyError as e:
        type_text(f"KeyError: {e} - This might be due to an undefined command or incorrect arguments.", colorTrue=color_coding)
    except ValueError as e:
        type_text(f"ValueError: {e} - This might be due to incorrect arguments provided.", colorTrue=color_coding)
    except Exception as e:
        type_text(f"Unexpected Error: {e}", colorTrue=color_coding)

def handle_sleep_command(player: PC):
    type_text("You decide to rest for a while.", colorTrue=color_coding)

    # Simulate some time passing
    sleep(2)  # Example: sleep for 2 seconds

    # Restore player's health or apply any other effects
    player.heal(3)  # Example: heal 5 health points during sleep

    # Optional: Print a message or effect that happens during sleep
    type_text("You feel refreshed after a good rest.", colorTrue=color_coding)

def get_player_input(split = True):
    move = ''
    while move == '':
        move = str(input('>')).strip().lower()
    if split:
        return move.split()
    return move

def handle_go_command(direction):
    Move(direction)

def handle_get_command(player: PC, item_name):
    if "item" in ROOMS[CURRENTROOM] and item_name == ROOMS[CURRENTROOM]['item'].name:
        player.inventory_add([ROOMS[CURRENTROOM]['item']])
        del ROOMS[CURRENTROOM]['item']
        type_text(f'%*BLUE*%{item_name}%*RESET*% got!', colorTrue=color_coding)
    else:
        type_text(f"Can't get {item_name}!", colorTrue=color_coding)

def handle_look_command():
    return_ = False
    if 'item' in ROOMS[CURRENTROOM]:
        type_text(f'The item in the room: %*BLUE*%{ROOMS[CURRENTROOM]["item"].name}%*RESET*%.', colorTrue=color_coding)
        return_ = True
    if 'containers' in ROOMS[CURRENTROOM]:
        type_text(f"The containers here are: %*RED*%{', '.join(ROOMS[CURRENTROOM]['containers'].keys())}%*RESET*%", colorTrue=color_coding)
        return_ = True
    if return_:
        return
    type_text('There is nothing of interest.', colorTrue=color_coding)

def handle_use_command(item = None, sub_item = None):
    Use(item, sub_item)

def handle_search_command(player, container = None, sub_container = None):
    if 'containers' in ROOMS[CURRENTROOM]:
        if container == 'the' and sub_container in ROOMS[CURRENTROOM]['containers'] and not all_same_value(ROOMS[CURRENTROOM]['containers'][sub_container].contents, None):
            search_container(player, sub_container)
        elif container in ROOMS[CURRENTROOM]['containers'] and not all_same_value(ROOMS[CURRENTROOM]['containers'][container].contents, None):
            search_container(player, container)
        else:
            type_text(f"You cannot search the {container}", colorTrue=color_coding)

def search_container(player: PC, container):
    player.inventory_add(ROOMS[CURRENTROOM]['containers'][container].contents)
    type_text(f"You search the{' secret' if ROOMS[CURRENTROOM]['containers'][container].secret else ''} %*RED*%{container}%*RESET*% and find a ", newline=False, colorTrue=color_coding)
    for searchitem in ROOMS[CURRENTROOM]['containers'][container].contents:
        if searchitem:
            if isinstance(searchitem, item):
                end_str = ' and a ' if ROOMS[CURRENTROOM]['containers'][container].contents.index(searchitem) < last_index(ROOMS[CURRENTROOM]['containers'][container].contents) else '\n'
                type_text(f"%*BLUE*%{searchitem.name}%*RESET*%{end_str}", newline=False, colorTrue=color_coding)
    ROOMS[CURRENTROOM]['containers'][container].contents = []


def handle_put_command(player: PC, PutItem: item = None, container = None, sub_container = None):
    if PutItem in player.inventory:
        if 'containers' in ROOMS[CURRENTROOM]:
            if container == 'the' and sub_container in ROOMS[CURRENTROOM]['containers']:
                put_in_container(player, player.inventory[player.inventory.index(PutItem)], sub_container)
                return
            elif container in ROOMS[CURRENTROOM]['containers']:
                put_in_container(player, player.inventory[player.inventory.index(PutItem)], container)
                return
    type_text(f"You cannot put the {PutItem.name} in the {container}", colorTrue=color_coding)


def put_in_container(player: PC, PutItem = None, container = None):
    player.inventory.remove(PutItem.name)
    if not ROOMS[CURRENTROOM]['containers'][container].contents:
        ROOMS[CURRENTROOM][container].contents = []
    if not isinstance(ROOMS[CURRENTROOM][container].contents, list):
        ROOMS[CURRENTROOM]['containers'][container].contents = [ROOMS[CURRENTROOM]['containers'][container].contents]
    ROOMS[CURRENTROOM]['containers'][container].contents += [PutItem]
    type_text(f"You put you're %*BLUE*%{PutItem.name}%*RESET*% into the %*RED*%{container}%*RESET*%", colorTrue=color_coding)



def handle_get_quest_command(questnum):
    if 'quests' in ROOMS[CURRENTROOM]:
        if questnum in ROOMS[CURRENTROOM]['quests']:
            quest_manager.add_quest(ROOMS[CURRENTROOM]['quests'][questnum])
            quest_manager.start_quest(ROOMS[CURRENTROOM]['quests'][questnum])
            del ROOMS[CURRENTROOM]['quests'][questnum]


def PrintMap():
    type_text(ShowMap())


# Define handling functions for different types of enemies
def handle_hungry_bear(player: PC, enemy: creature):
    enemy_reacting = True
    if 'potion' in player.inventory:
        if ask_for_consent("Do you want to throw your potion at the bear"):
            enemy_reacting = False
            del player.inventory[player.inventory.index('potion')]
            type_text(f'You throw the potion at the bear and it explodes into a puff of magic smoke that stuns the bear!', colorTrue=color_coding)
    if enemy_reacting:
        return battle(player, enemy, LAST_ROOM)

def handle_grumpy_pig(player: PC, enemy: creature):
    enemy_reacting = True
    if 'saddle' in player.inventory and 'pig-rod' in player.inventory:
        if ask_for_consent("Do you want to use your saddle and pig-rod on the pig"):
            enemy_reacting = False
            type_text(f'You throw a saddle onto the pig and leap on steering it about with a pig fishing rod!', colorTrue=color_coding)
            del ROOMS[CURRENTROOM]['creatures stats']
            del player.inventory[player.inventory.index('saddle')]
            del player.inventory[player.inventory.index('pig-rod')]
            player.inventory_add(item['pig-steed'])
            player.xp += 20
    if 'torch' in player.inventory:
        if ask_for_consent("Do you want to use your torch to scare the pig away"):
            enemy_reacting = False
            type_text(f'You wave your torch at the pig and it runs away through a tiny open window.', colorTrue=color_coding)
            del ROOMS[CURRENTROOM]['creatures stats']
            player.xp += 5
    if 'ration' in player.inventory:
        if ask_for_consent("Do you want to throw your ration at the pig"):
            enemy_reacting = False
            type_text(f"You quickly throw rations at the pig. It still doesn't look happy though.", colorTrue=color_coding)
            del player.inventory[player.inventory.index('ration')]
            player.xp += 15

    if enemy_reacting:
        return battle(player, enemy, LAST_ROOM)

def handle_greedy_goblin(player: PC, enemy: creature):
    enemy_reacting = True
    if player.money >= 15:
        if ask_for_consent("Do you want to pay the goblin to not attack you"):
            enemy_reacting = False
            type_text(f"You pay the {enemy.name} to not attack you for now, but he says you should run.", colorTrue=color_coding)
            player.money -= 15
            enemy.dropped_items[1].value += 15
    if enemy_reacting:
        return battle(player, enemy, LAST_ROOM)

commands = {
    'go': handle_go_command,
    'get quest': handle_get_quest_command,
    'get': handle_get_command,
    'look': handle_look_command,
    'use': handle_use_command,
    'search': handle_search_command,
    'quit': quit,
    'help': showInstructions,
    'hint': showHint,
    'sleep': handle_sleep_command,
    'put': handle_put_command,
    'map': PrintMap,
}


def quit():
    exit()

guards = [
    Guard(
        name="Guard",
        hp=10,
        atpw=4,
        description="A 5ft 8 human guard who looks like he doesn't belong here",
        flavor_text="A human guard spots you and says: 'You shouldn't be here'",
        type = creature_type('humanoid', 'human'),
        current_room="Bedroom",
        patrol_route=["Bedroom", "Office", "Tower Bottom", "Landing", "Bedroom"],
        patrol_type='random'
        ),
]

def main():
    global charactersList


    df = pd.DataFrame(charactersList)


    # this is the initializer
    Standord_Player = loop_til_valid_input("Do you want to use a premade character?", "you didn't answer Y or N.", Y_N).value

    if Standord_Player:
        while True:
            type_text("Who do you want to play as?", colorTrue=False)
            print(df)
            selected_character = loop_til_valid_input(
                "Who do you want to play as? (please select the number to the left of there stats)", 
                "That wasn't one of the characters. Please choose one.", 
                int
            )
            lstIndex = last_index(charactersList)
            if selected_character <= lstIndex:
                character_info = charactersList[selected_character]
                name = character_info['name']
                age = character_info['age']
                height = character_info['height']
                weight = character_info['weight(LBs)']
                break
            else:
                type_text(colorTrue=False)

        type_text("Please enter a codename for your achievements to save under \n>", False, colorTrue=False)
        codename = input()

    else:
        type_text("You will now have to enter a name, age, height, and weight. Please enter the height in this format: _ft _. These will be used throughout the game.", colorTrue=False)

        name = loop_til_valid_input("What is your name?", "You didn't enter a string. Please enter a string.", str)
        age = loop_til_valid_input("What is your age (in whole years)?", "You didn't enter an integer. Please enter an integer.", int)
        height = loop_til_valid_input("What is your height?", "You didn't enter your height in the correct format. Please enter your height in the correct format.", Height)
        weight = loop_til_valid_input("What is your weight (in lbs)?", "You didn't enter an integer. Please enter an integer.", int)
        codename = False

    color_coding = loop_til_valid_input("Do you want color coding (Y/N)?", "you didn't answer Y or N.", Y_N).value

    player = PC(
        name,
        age,
        'Warrior',
        1,
        'Soldier',
        height,
        weight,
        [
            f"You joined the army at {14 if age >= 14 else age}", 
            f"You joined the army to end the war and because you wanted glory", 
            f"You spent your first year of service training and the rest on the front lines, surprisingly you didn't die", 
            f"In your service, you made 3 friends, one of them died", 
            f"You fought your enemies from the tops of the mountains to the vast oceans", 
            f"Your father was never home; he was always off on great adventures until he died when you were {7 if age >= 7 else age}", 
            f"You have no friends back home; you were always very lonely", 
            f"You are an only child. You ran away from home to join the army; your mother misses you terribly", 
            f"She was a baker, and you spent a lot of time helping her bake bread. You never went to school", 
            f"The people you admire the most are Sam and Aragorn from Lord of the Rings, which you read as a child. You have also read the Hunger Games when you were {13 if age >= 13 else age}", 
            f"Your favorite weapon is a bow; however, the scimitar is a close second.", 
        ],
        Backstory=f"""
    You were born into a life of solitude as an only child. Your father was always away on grand adventures and passed away when you were just {7 if age >= 7 else age}. Your mother, a dedicated 
    baker, raised you alone. Although she did her best, you spent most of your time helping her in the bakery rather than attending school, which left you feeling quite isolated.

    At the age of {14 if age >= 14 else age}, driven by a desire for glory and a wish to end the war, you left home to join the army. You spent your first year in rigorous training, followed by a 
    harsh life on the front lines. Against all odds, you survived, forging bonds with three close friends—though one of them tragically died in battle. Your journey took you from the heights of 
    mountains to the vast expanses of the ocean, each experience shaping who you are.

    You were deeply influenced by the heroes of your childhood—Sam and Aragorn from %*ITALIC*%Lord of the Rings%*RESET*%, which you read as a child, and the characters from %*ITALIC*%The Hunger 
    Games%*RESET*%, which you read when you were {13 if age >= 13 else age}. These stories inspired you and fueled your dream of heroism. Though your favorite weapon is a bow, you also have a 
    fondness for the scimitar.

    Now, you find yourself in the Mansion of Amnesia, a place that seems to have erased your memories. The details of your past are fragmented, but the echoes of your history drive you forward. You 
    must navigate the mansion and uncover the truth behind your captivity, all while drawing strength from the remnants of your past.
    """
    )

    # shows the instructions
    start()

    # loop forever while the player wants to play
    while True:
        command()

        # Move guards
        for guard in guards:
            if isinstance(guard, Guard):
                guard.move(ROOMS)

        # Check for detection
        for guard in guards:
            if isinstance(guard, Guard):
                if guard.check_detection(CURRENTROOM):
                    guard.type_text_flavor_text()
                    guards[guards.index(guard)] = battle(player, guard, LAST_ROOM)
        
        # player loses if they enter a room with a monster, unless they can fight it.
        if 'creatures stats' in ROOMS[CURRENTROOM]:
            enemies = ROOMS[CURRENTROOM]['creatures stats']
            if not isinstance(enemies, list):
                enemies = [enemies]  # Ensure enemies is a list even if there's only one creature


            for enemy in enemies:
                if isinstance(enemy, creature):
                    enemy.type_text_flavor_text()

                    if enemy.name == 'hungry bear':
                        enemy_REF = handle_hungry_bear(player, enemy)
                        enemies[enemies.index(enemy)] = enemy_REF
                    elif enemy.name == 'grumpy pig':
                        enemy_REF = handle_grumpy_pig(player, enemy)
                        enemies[enemies.index(enemy)] = enemy_REF
                    elif enemy.name == 'greedy goblin':
                        enemy_REF = handle_greedy_goblin(player, enemy)
                        enemies[enemies.index(enemy)] = enemy_REF
                    else:
                        enemy_REF = battle(player, enemy, LAST_ROOM)
                        enemies[enemies.index(enemy)] = enemy_REF

            if all_same_value(enemies, False):
                del ROOMS[CURRENTROOM]['creatures stats']
            else:
                ROOMS[CURRENTROOM]['creatures stats'] = enemies
        
        if 'NPCs' in ROOMS[CURRENTROOM]:
            for npcname, npcstats in ROOMS[CURRENTROOM]['NPCs'].items():
                if ask_for_consent("Do you want to interact with this NPC") or npcstats.aggressive:
                    npcstats.interact
                    if npcstats.aggressive:
                        ROOMS[CURRENTROOM]['NPCs'][npcname] = battle(player, npcstats)
        
        player.special_ability.Tick()
        quest_manager.update_objective(f"Kill {GameState['Enemys killed']} creatures")
        for ___ in GameState['collected items']:
            if isinstance(___, item):
                quest_manager.update_objective(f"Colect {___.name}")





if __name__ == "__main__":
    main()
