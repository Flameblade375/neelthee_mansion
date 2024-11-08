from .Rooms import * 
from .creatures import *
from .items import *
from .Quests import *
from .all_game_utils import *


GameState = {
    'Enemies killed': 0,
    'collected items': [],
}


'''
Neel-thee's Mansion of Amnesia
'''

global player, evil_mage, commands, NOTE_NUM, credits, color_coding, quest_manager, revealer, CHARACTERSLIST, BACKGROUNDS

BACKGROUNDS = {
    'Adventurer': ['survival', 'climbing'],
    'Artist': ['painting', 'sculpting'],
    'Scholar': ['reading', 'research'],
}

revealer = KeyRevealer()

quest_manager = QuestManager()

color_coding = False

credits = '''
Made by: Alexander.E.F
AI assisted the creation'''


name = ''
age = 0
height = Height()
weight = 0


CHARACTERSLIST = [
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
    {'name': 'Grace', 'age': 29, 'height': Height('5ft 7'), 'weight(LBs)': 140},
    {'name': 'Josh', 'age': 26, 'height': Height('5ft 6'), 'weight(LBs)': 135},
    {'name': 'Luka', 'age': 29, 'height': Height('5ft 7'), 'weight(LBs)': 140},
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
    global player
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
    global player
    # Display the game instructions
    type_text('''
===========================
Commands:
go [%*GREEN*%direction%*RESET*%/%*GREEN*%teleport%*RESET*%/%*GREEN*%number%*RESET*%] - Move to another location
get [%*BLUE*%item%*RESET*%] - Pick up an item from your current location
search [%*RED*%container%*RESET*%] - Search a container in your current location
use [%*BLUE*%item%*RESET*%] - Use an item from your inventory
put [%*BLUE*%item%*RESET*%] [in] [%*RED*%container%*RESET*%] - Put an item from your inventory into a container in your current location
examine [%*GREEN*%direction%*RESET*%/%*RED*%container%*RESET*%/%*BLUE*%item%*RESET*%] - Find out some info about the object
sleep - Rest for a bit and regain some health
look - Look around your current location
quit - Quit the game
help - Show these instructions
hint - Get a random hint for your current location
map - Display the map of places you have been to
''', colorTrue=color_coding)


def showHint():
    global player
    if 'Hints' in ROOMS[player.CURRENTROOM]:
        type_text("You think:", colorTrue=color_coding)
        hint = choice(ROOMS[player.CURRENTROOM]['Hints'])
        type_text(hint, colorTrue=color_coding)
    else:
        type_text("You can't think of anything", colorTrue=color_coding)

def check_direction(var: str, directions: list):
    global player
    for direction in directions:
        if var == direction:
            return True
    return False


def End(text: str, win: bool = True):
    global player
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
    global player, NOTE_NUM
    player.NOTES.append(note)
    NOTE_NUM += 1
    inv_note = 'note ' + str(NOTE_NUM)
    try:
        del player.inventory[parchment_index]
    except IndexError:
        pass
    player.inventory_add([item(inv_note)])


def Use_grappling_hook():
    global player

    def swing_into_forest():
        global player
        type_text("You throw your grappling-hook, it catches a branch of a nearby tree and hooks back onto itself. \nYou can swing into the forest!", colorTrue=color_coding)
        if ask_for_consent("Do you want to swing into the forest"):
            type_text("You swing into the forest", colorTrue=color_coding)
            Move('Forest Clearing')
        else:
            type_text("You flick the rope and it unhooks. You continue exploring the house.", colorTrue=color_coding)

    def climb_into_house():
        global player
        type_text("You throw your grappling-hook, it catches the railing of the nearby house and hooks back onto itself. \nYou can climb into the house!", colorTrue=color_coding)
        if ask_for_consent("Do you want to climb into the house"):
            type_text("You climb into the house", colorTrue=color_coding)
            Move('Balcony')
        else:
            type_text("You flick the rope and it unhooks. You continue exploring the forest", colorTrue=color_coding)

    if player.CURRENTROOM == 'Balcony' and 'grappling-hook' in player.inventory:
        swing_into_forest()
    elif player.CURRENTROOM == 'Forest Clearing' and 'grappling-hook' in player.inventory:
        climb_into_house()


def Use_quill():
    global player

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
    global player
    """Reads a specified note from the player's inventory."""
    note_key = f'note {note_number}'
    if note_key in player.inventory:
        note_index = int(note_number) - 1
        type_text(f'You read:', colorTrue=color_coding)
        type_text(player.NOTES[note_index], colorTrue=color_coding)
    else:
        type_text('You do not have that note', colorTrue=color_coding)


def Use(*Args):
    global player
    Item = " ".join(Args)
    """Uses an item from the player's inventory."""
    if Item in player.inventory:
        item_obj = player.inventory[player.inventory.index(Item)]
        if isinstance(item_obj, item):
            if item_obj.sell(player):
                type_text(f"You sell the %*BLUE*%{Item}%*RESET*%", colorTrue=color_coding)
                player.inventory.remove(item_obj.name)
            elif Item == 'quill':
                Use_quill()
            elif Item == 'grappling-hook':
                Use_grappling_hook()
    elif Item[0] == 'note' and Item[1]:
        Use_note(Item[1])
    elif Item == '0':
        type_text("You can't use nothing", colorTrue=color_coding)
    else:
        type_text("You can't use that", colorTrue=color_coding)


def PickKey(locked_obj):
    keys = player.inventory.keys()
    if not isinstance(keys, list):
        keys = [keys]
    
    if keys:
        while True:
            type_text(f"Please pick which key you want to use in the lock. This is what you know about the lock: {locked_obj}. These are your keys:")

            # Enumerate keys and display them
            for idx, key in enumerate(keys, 1):  # Starts numbering at 1
                type_text(f"{idx}. {key.name} - {key.CurentRevealStr}")
            
            # Use loop_til_valid_input to get a valid integer within the correct range
            choice = loop_til_valid_input(
                input_text="Enter the number of the key you'd like to use: ", 
                bad_text="That's not a valid choice, please try again.", 
                Class=int  # Ensuring input is an integer
            )

            # Since loop_til_valid_input ensures valid input, just return the selected key
            if 1 <= choice <= len(keys):
                return keys[choice - 1]  # Fetch the key using 0-based index
    
    return Key(KeyCode=None)


def Move(move):
    global player


    def attempt_charter():
        global player
        if player.money >= 10:
            player.money -= 10
            if 'descovered' in ROOMS[newRoom] and not ROOMS[newRoom]['descovered']:
                ROOMS[newRoom]['descovered'] = True
            return ROOMS[player.CURRENTROOM]['directions'][move]
        else:
            type_text("You don't have enough money to charter a ship.", colorTrue=color_coding)
            return player.CURRENTROOM

    def attempt_move_to_garden():
        global player
        key = PickKey(Lock("629.IdnXwnt"))
        if key.GetKeyCode() == "629.IdnXwnt":
            End('You unlock the gate to the garden with the key!')
            return newRoom
        type_text('The gate is locked.', colorTrue=color_coding)
        return newRoom

    def move_to_room():
        global player
        player.LASTROOM = player.CURRENTROOM
        if 'descovered' in ROOMS[newRoom] and not ROOMS[newRoom]['descovered']:
            ROOMS[newRoom]['descovered'] = True
        if move == '0':
            return attempt_charter()
        elif newRoom == 'Garden':
            return attempt_move_to_garden()
        else:
            return newRoom

    if move in ROOMS[player.CURRENTROOM]['directions']:
        newRoom = "Hall"
        if isinstance(ROOMS[player.CURRENTROOM]['directions'][move], Door):
            if isinstance(ROOMS[player.CURRENTROOM]['directions'][move].lock, Lock):
                key = PickKey(ROOMS[player.CURRENTROOM]['directions'][move].lock)
                ROOMS[player.CURRENTROOM]['directions'][move].Unlock(key, player)
            newRoom = ROOMS[player.CURRENTROOM]['directions'][move].GetRoom(player.CURRENTROOM)
        else:
            newRoom = ROOMS[player.CURRENTROOM]['directions'][move]
        newRoom = move_to_room()
        player.CURRENTROOM = newRoom
        return
    elif move in ROOMS:
        newRoom = move
        if newRoom == 'Garden':
            newRoom = attempt_move_to_garden()
        player.LASTROOM = player.CURRENTROOM
        player.CURRENTROOM = newRoom
        if 'random_events' in ROOMS[player.CURRENTROOM]:
            for randomEvent in ROOMS[player.CURRENTROOM]['random_events']:
                if isinstance(randomEvent, RandomEvent):
                    randomEvent.check_and_trigger(player)
        return
    type_text(f"There is no exit {move}", colorTrue=color_coding)


def start():
    global player
    # shows the main menu
    type_text(f'\nHello %*MAGENTA*%{player.name}%*RESET*% and welcome to my Role Playing Game. \nI hope you have fun!', colorTrue=color_coding)
    showInstructions()


def showStatus():
    global player

    # Display player's current status
    text = f'\n---------------------------'
    
    # Display the current inventory
    the_inventory = [itemnum.name for itemnum in player.inventory if isinstance(itemnum, item)]
    text += f'\nInventory: %*BLUE*%{", ".join(the_inventory)}%*RESET*%; Money: {player.money}; XP: {player.xp}; Level: {player.Level}'
    
    # Display possible directions of travel
    text = display_directions(text)

    # Display the map if available
    if 'map' in ROOMS[player.CURRENTROOM]:
        text += f'\n\nKey: {"; ".join(KEY)}\n'
        text += f'\n{ROOMS[player.CURRENTROOM]["map"]}\n'

    # Display the description of the current room
    text += ('\n' + str(ROOMS[player.CURRENTROOM]['info']))

    text += f"\n---------------------------"
    
    type_text(text, colorTrue=color_coding)
    
    # Optionally display additional room description
    if 'description' in ROOMS[player.CURRENTROOM] and ask_for_consent("Do you want to observe the area"):
        type_text("The area:", colorTrue=color_coding)
        type_text(ROOMS[player.CURRENTROOM]['description'], colorTrue=color_coding)


def display_directions(text):
    global player
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
            'down': "There is a hole in the ground leading"
        },
        'cavern': {
            'north': "There is a tunel to the",
            'east': "There is a tunel to the",
            'south': "There is a tunel to the",
            'west': "There is a tunel to the",
            'up': "There is a shoot with handhold going",
            'down': "There is a shoot in the ground going"
        },
    }

    room_type = ROOMS[player.CURRENTROOM]['room type']
    if room_type in direction_descriptions:
        for direction in directions:
            if direction in ROOMS[player.CURRENTROOM]['directions']:
                if direction != 'teleport':
                    text += f'\n{direction_descriptions[room_type][direction]} %*GREEN*%{direction}%*RESET*%.'

    if 'teleport' in ROOMS[player.CURRENTROOM]['directions']:
        text += "\nThere is a %*GREEN*%teleport%*RESET*%ation circle on the ground."

    return text

def Examine(*Args):
    Name = ' '.join(Args)
    item_index = player.inventory.index(Name)  # Store the result of index in a variable

    if item_index is not None:  # Check explicitly if item_index is valid
        _ = player.inventory[item_index]
        if isinstance(_, item):
            type_text("You look at your item and you figure out this about it:")
            if not revealer.reveal_key_code(_):
                if _.type == 'weapon':
                    type_text(f"This item is a weapon that adds {_.value} damage.")
                elif _.type == 'readable':
                    if 'reading' in player.Skills:
                        type_text(f"You read {_.name} and it contains:")
                        if isinstance(_, Book):
                            type_text(_.GetContense())
                        else:
                            type_text(_.value)
    elif Name in ROOMS[player.CURRENTROOM]['directions']:  # Check exits in the room
        door = ROOMS[player.CURRENTROOM]['directions'][Name]
        if isinstance(door, Door):
            if isinstance(door.lock, Lock):
                type_text("The door is locked," if door.lock.is_locked else "The door is not locked,", "you know this about its key code:")
                revealer.reveal_key_code(door)
            else:
                type_text(f"The exit {Name} has no lock.")
        else:
            type_text(f"There is nothing special about the exit {Name}.")
    elif Name in ROOMS[player.CURRENTROOM]['containers']:  # Check containers in the room
        containerins = ROOMS[player.CURRENTROOM]['containers'][Name]
        if isinstance(containerins, container):
            if isinstance(containerins.lock, Lock):
                type_text("The container is locked," if containerins.lock.is_locked else "The container is not locked,", "you know this about its key code:")
                revealer.reveal_key_code(containerins)
            else:
                type_text(f"The container {Name} has no lock.")
        else:
            type_text(f"There is no container named {Name} in this room.")
    else:
        type_text(f"There is nothing special about the {Name}.")

def battle(player: PC, good_guys: list, bad_guys: list, last_room):
    """
    Simulate a battle between the player (and allies) and monsters.

    Args:
        player (PC): The player character.
        good_guys (list): The list of allies to help the player.
        bad_guys (list): The list of monsters to battle the player.
        last_room: The previous room before the battle.

    Returns:
        None if all bad guys are defeated, else the remaining bad guys.
    """
    while player.hp > 0:
        if all(monster.hp <= 0 for monster in bad_guys):
            handle_victory(player, bad_guys)
            return good_guys, None

        if ask_for_consent("Do you want to run away"):
            Move(last_room)
            return good_guys, bad_guys

        # Player and good guys' turn
        for ally in [player] + good_guys:
            if all(monster.hp <= 0 for monster in bad_guys):
                handle_victory(player, bad_guys)
                return good_guys, None

            target = select_target(ally, bad_guys)
            player_turn(ally, target)

        # Bad guys' turn
        for monster in bad_guys:
            if monster.hp > 0:
                target = select_target(monster, [player] + good_guys)
                monster_turn(target, monster)

        if player.hp <= 0:
            End(f'The monsters defeat you!', win=False)
            return good_guys, bad_guys

    return good_guys, bad_guys


def player_turn(player: PC, monster: creature):
    """
    Handle a character's turn during the battle.

    Args:
        player (PC): The player or ally.
        monster (creature): The monster being fought.
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
    Handle a monster's turn during the battle.

    Args:
        player (PC): The player or ally.
        monster (creature): The monster attacking.
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


def handle_victory(player: PC, monsters: list):
    """
    Handle the logic when the player and allies defeat all monsters.

    Args:
        player (PC): The player character.
        monsters (list): The list of defeated monsters.
    """
    type_text("You have defeated all the enemies!", colorTrue=color_coding)
    for monster in monsters:
        if monster.hp <= 0:
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
        tuple[int, int]: Minimum and maximum damage range.
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


def select_target(chooser, targets: list):
    """
    Select a target from a list of characters.

    Args:
        chooser: The entity (e.g., player or AI) selecting the target.
        targets (list): List of characters to select from.

    Returns:
        The selected target.
    """
    if chooser == player:
        valid_targets = []
        type_text("Who do you want to attack? The options:")
        # Enumerate through the targets to get both the index and the enemy.
        for index, enemy in enumerate(targets):
            if enemy.hp > 0:
                type_text(f"{index + 1}: {enemy.name} ({enemy.hp} HP)")
                valid_targets.append(index)
        
        # Prompt the player to select a target
        while True:
            try:
                choice = int(input("Enter the number of the target: ")) - 1
                if choice in valid_targets:
                    return targets[choice]
                else:
                    type_text("Invalid choice. Please select a valid target.")
            except ValueError:
                type_text("Invalid input. Please enter a number.")
    else:
        # AI or other logic for non-player chooser
        for target in targets:
            if target.hp > 0:
                return target



def command():
    global player
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
    player.heal(3)  # Example: heal 3 health points during sleep

    # Optional: Print a message or effect that happens during sleep
    type_text("You feel refreshed after a good rest.", colorTrue=color_coding)

def get_player_input(split = True):
    global player
    move = ''
    while move == '':
        move = str(input('>')).strip().lower()
    if split:
        return move.split()
    return move

def handle_go_command(direction):
    global player
    Move(direction)

def handle_get_command(player: PC, *Args):
    item_name = " ".join(Args)
    for ItemName in ROOMS[player.CURRENTROOM]['items'].keys():
        if item_name == ItemName:
            player.inventory_add([ROOMS[player.CURRENTROOM]['items'][ItemName]])
            del ROOMS[player.CURRENTROOM]['items'][ItemName]
            type_text(f'%*BLUE*%{item_name}%*RESET*% got!', colorTrue=color_coding)
            return
    type_text(f"Can't get {item_name}!", colorTrue=color_coding)

def handle_look_command():
    global player
    should_return = False
    if 'items' in ROOMS[player.CURRENTROOM]:
        type_text(f'The items in the room: %*BLUE*%{", ".join(ROOMS[player.CURRENTROOM]["items"].keys())}%*RESET*%.', colorTrue=color_coding)
        should_return = True
    if 'containers' in ROOMS[player.CURRENTROOM]:
        type_text(f"The containers here are: %*RED*%{', '.join(ROOMS[player.CURRENTROOM]['containers'].keys())}%*RESET*%", colorTrue=color_coding)
        should_return = True
    if should_return:
        return
    type_text('There is nothing of interest.', colorTrue=color_coding)

def handle_use_command(item = None, sub_item = None):
    global player
    Use(item, sub_item)

def handle_search_command(player, *Args):
    Container = " ".join(Args)
    if 'containers' in ROOMS[player.CURRENTROOM]:
        if Container in ROOMS[player.CURRENTROOM]['containers'] and not all_same_value(ROOMS[player.CURRENTROOM]['containers'][Container].contents, None):
            search_container(player, Container)
        else:
            type_text(f"You cannot search the {Container}", colorTrue=color_coding)

def search_container(player: PC, Container):
    ContainerName = Container
    Container = ROOMS[player.CURRENTROOM]['containers'][Container]
    if isinstance(Container, container):
        if isinstance(Container.lock, Lock):
            key = PickKey(Container.lock)
            Container.Unlock(key, player)
        type_text(f"You search the{' secret' if Container.secret else ''} %*RED*%{ContainerName}%*RESET*% and find a ", newline=False, colorTrue=color_coding)
        for searchitem in Container.contents:
            if searchitem:
                if isinstance(searchitem, item):
                    end_str = ' and a ' if Container.contents.index(searchitem) < last_index(Container.contents) else '\n'
                    type_text(f"%*BLUE*%{searchitem.name}%*RESET*%{end_str}", newline=False, colorTrue=color_coding)
        Container.take_contents(player)


def handle_put_command(player: PC, *Args):
    arguments = " ".join(Args)
    Arguments = arguments.split(" in ")
    
    # Ensure we have exactly two parts
    if len(Arguments) < 2:
        type_text("You need to specify an item and where to put it (e.g., 'put book in drawer').", colorTrue=color_coding)
        return
    
    # Strip whitespace
    Arguments = [arg.strip() for arg in Arguments]
    item_name = Arguments[0]
    container_name = Arguments[1]

    # Check if item is in inventory
    if item_name not in [item.name for item in player.inventory]:
        type_text(f"You don't have {item_name} in your inventory.", colorTrue=color_coding)
        return

    # Retrieve item and container
    PutItem = player.inventory[[item.name for item in player.inventory].index(item_name)]
    if 'containers' in ROOMS[player.CURRENTROOM]:
        put_in_container(player, PutItem, container_name)
    else:
        type_text(f"You cannot put the {PutItem.name} in the {container_name}", colorTrue=color_coding)


def put_in_container(player: PC, PutItem = None, container = None):
    player.inventory.remove(PutItem.name)
    if not ROOMS[player.CURRENTROOM]['containers'][container].contents:
        ROOMS[player.CURRENTROOM]['containers'][container].contents = []
    if not isinstance(ROOMS[player.CURRENTROOM]['containers'][container].contents, list):
        ROOMS[player.CURRENTROOM]['containers'][container].contents = [ROOMS[player.CURRENTROOM]['containers'][container].contents]
    ROOMS[player.CURRENTROOM]['containers'][container].contents += [PutItem]
    type_text(f"You put you're %*BLUE*%{PutItem.name}%*RESET*% into the %*RED*%{container}%*RESET*%", colorTrue=color_coding)



def handle_get_quest_command(questnum):
    global player
    if 'quests' in ROOMS[player.CURRENTROOM]:
        if questnum in ROOMS[player.CURRENTROOM]['quests']:
            quest_manager.add_quest(ROOMS[player.CURRENTROOM]['quests'][questnum])
            quest_manager.start_quest(ROOMS[player.CURRENTROOM]['quests'][questnum])
            del ROOMS[player.CURRENTROOM]['quests'][questnum]


def PrintMap():
    global player
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
        return [enemy, enemy_reacting]

def handle_grumpy_pig(player: PC, enemy: creature):
    enemy_reacting = True
    if 'saddle' in player.inventory and 'pig-rod' in player.inventory:
        if ask_for_consent("Do you want to use your saddle and pig-rod on the pig"):
            enemy_reacting = False
            type_text(f'You throw a saddle onto the pig and leap on steering it about with a pig fishing rod!', colorTrue=color_coding)
            del ROOMS[player.CURRENTROOM]['creatures stats']
            del player.inventory[player.inventory.index('saddle')]
            del player.inventory[player.inventory.index('pig-rod')]
            player.inventory_add(item['pig-steed'])
            player.xp += 20
    if 'torch' in player.inventory:
        if ask_for_consent("Do you want to use your torch to scare the pig away"):
            enemy_reacting = False
            type_text(f'You wave your torch at the pig and it runs away through a tiny open window.', colorTrue=color_coding)
            del ROOMS[player.CURRENTROOM]['creatures stats'][ROOMS[player.CURRENTROOM]['creatures stats'].index(enemy)]
            player.xp += 5
    if 'rations' in player.inventory:
        if ask_for_consent("Do you want to throw your ration at the pig"):
            enemy_reacting = False
            type_text(f"You quickly throw rations at the pig. It still doesn't look happy though.", colorTrue=color_coding)
            del player.inventory[player.inventory.index('rations')]
            player.xp += 15

    if enemy_reacting:
        return [enemy, enemy_reacting]

def handle_greedy_goblin(player: PC, enemy: creature):
    enemy_reacting = True
    if player.money >= 15:
        if ask_for_consent("Do you want to pay the goblin to not attack you"):
            enemy_reacting = False
            type_text(f"You pay the {enemy.name} to not attack you for now, but he says you should run.", colorTrue=color_coding)
            player.money -= 15
            enemy.dropped_items[1].value += 15
    if enemy_reacting:
        return [enemy, enemy_reacting]

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
    'examine': Examine,
}


def quit():
    exit()

guards = [
    Guard(
        name="Guard",
        hp=10,
        atpw=4,
        description="A 5'8\" human guard who looks like he doesn't belong here.",
        flavor_text="A human guard spots you and says: 'You shouldn't be here.'",
        type=creature_type('humanoid', 'human'),
        current_room="Bedroom",
        patrol_route=["Bedroom", "Office", "Tower Bottom", "Landing", "Bedroom"],
        patrol_type='normal'
    ),
    Guard(
        name="Wolf",
        hp=10,
        atpw=4,
        description="A large wolf with blood covering its face.",
        flavor_text="A wolf spots you and growls.",
        type=creature_type('beast', 'wolf'),
        current_room="Balcony",
        patrol_type='random',
        frendly_text="The wolf nuzzles you"
    ),
]

def handle_wolf(player: PC, wolf: Guard):
    enemy_reacting = True
    if 'rations' in player.inventory:
        if ask_for_consent("Do you want to give your ration to the wolf"):
            enemy_reacting = False
            type_text(
                "You quickly give your rations to the wolf. It looks happy, walks up to you, and nuzzles you.", 
                colorTrue=color_coding
            )
            player.inventory.remove('rations')
            wolf.patrol_type = "follow"
            wolf.frendly = True
            return wolf
    if enemy_reacting:
        return [wolf, enemy_reacting]

def handle_guard_action(guard):
    # Dynamically build the function name
    function_name = f"handle_{guard.name.lower()}"
    
    # Use globals() to retrieve the function by name
    function_to_call = globals().get(function_name)
    
    if function_to_call:
        # Call the found function
        guard = function_to_call(player, guard)
        return [True, guard]  # Function was found and called
    else:
        return [False, [guard, True]]  # Function was not found

def initializer():
    global color_coding, player, CHARACTERSLIST
    df = pd.DataFrame(CHARACTERSLIST)
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
            lstIndex = last_index(CHARACTERSLIST)
            if selected_character <= lstIndex:
                character_info = CHARACTERSLIST[selected_character]
                name = character_info['name']
                age = character_info['age']
                height = character_info['height']
                weight = character_info['weight(LBs)']
                break
            else:
                type_text(colorTrue=False)

    else:
        type_text("You will now have to enter a name, age, height, and weight. Please enter the height in this format: _ft _. These will be used throughout the game.", colorTrue=False)

        name = loop_til_valid_input("What is your name?", "You didn't enter a string. Please enter a string.", str)
        age = loop_til_valid_input("What is your age (in whole years)?", "You didn't enter an integer. Please enter an integer.", int)
        height = loop_til_valid_input("What is your height?", "You didn't enter your height in the correct format. Please enter your height in the correct format.", Height)
        weight = loop_til_valid_input("What is your weight (in lbs)?", "You didn't enter an integer. Please enter an integer.", int)

    color_coding = loop_til_valid_input("Do you want color coding (Y/N)?", "you didn't answer Y or N.", Y_N).value


    background_name = []
    background_skills = []

    while True: 
        type_text("")  # Prints an empty line
        type_text("0. Random")

        # Display each background with its skills formatted correctly.
        for idx, (background_name, background_skills) in enumerate(BACKGROUNDS.items()):
            formatted_skills = ", ".join(background_skills)
            type_text(f"{idx + 1}. {background_name} - {formatted_skills}")

        # Prompt the user to pick a background by number.
        background = loop_til_valid_input("What background do you want? (please select the number to the left of them)", "You didn't pick one", int)
        
        length = len(BACKGROUNDS)
        if 1 <= background <= length:
            # Get the background name and skills based on user choice.
            background_name = list(BACKGROUNDS.keys())[background - 1]
            background_skills = BACKGROUNDS[background_name]
            break
        elif background == 0:
            # Randomly select a background and get its associated skills.
            background_name = choice(list(BACKGROUNDS.keys()))
            background_skills = BACKGROUNDS[background_name]
            break
        else:
            type_text("You didn't pick one")


    # start the player in the Hall and sets up everything else
    player = PC(
        name,
        age,
        background,
        1,
        'Soldier',
        height,
        weight,
        CURRENTROOM='Hall',
        Skills=background_skills,
    )

def main():
    global player, color_coding


    # this is the initializer
    initializer()

    # shows the instructions
    start()

    # loop forever while the player wants to play
    while True:
        command()

        if 'random_events' in ROOMS[player.CURRENTROOM]:
            for event in ROOMS[player.CURRENTROOM]['random_events']:
                if isinstance(event, RandomEvent):
                    event.check_and_trigger(player)

        # Move guards
        for guard in guards:
            if isinstance(guard, Guard):
                guard.move(ROOMS, player)

        good_guys = []
        bad_guys = []

        # Check for detection
        for guard in guards:
            if isinstance(guard, Guard):
                if guard.hp > 0:
                    if guard.check_detection(player.CURRENTROOM):
                        guard_handled = handle_guard_action(guard)
                        if not isinstance(guard_handled, list):
                            guard_handled = [guard_handled]

                        # Get is_reacting from guard_handled
                        is_reacting = guard_handled[1][1] if isinstance(guard_handled[1], list) else True

                        # Only update guard if the guard is reacting
                        if is_reacting:
                            if guard.frendly:
                                good_guys.append(guard)
                            else:
                                bad_guys.append(guard)

                        if guard_handled[0]:
                            guards[guards.index(guard)] = guard_handled[1][0] if isinstance(guard_handled[1], list) else guard_handled[1]

        # Handle creatures in the current room
        if 'creatures stats' in ROOMS[player.CURRENTROOM]:
            is_reactings = []
            enemies = ROOMS[player.CURRENTROOM]['creatures stats']
            if not isinstance(enemies, list):
                enemies = [enemies]  # Ensure enemies is a list even if there's only one creature

            for enemy in enemies:
                if isinstance(enemy, creature):
                    if enemy.hp > 0:
                        enemy.type_text_flavor_text()
                        if ask_for_consent(f"Do you want to examine the {enemy.name}"):
                            enemy.type_text_description()

                        # Handle specific creatures
                        if enemy.name == 'hungry bear':
                            enemy_REF = handle_hungry_bear(player, enemy)
                        elif enemy.name == 'grumpy pig':
                            enemy_REF = handle_grumpy_pig(player, enemy)
                        elif enemy.name == 'greedy goblin':
                            enemy_REF = handle_greedy_goblin(player, enemy)
                        else:
                            enemy_REF = enemy

                        if isinstance(enemy_REF, list):
                            is_reacting = enemy_REF[1]
                            enemy_REF = enemy_REF[0]
                            is_reactings.append(is_reacting)

                        enemies[enemies.index(enemy)] = enemy_REF

                        # Add to good or bad lists if reacting
                        if is_reacting:
                            if enemy_REF.frendly:
                                good_guys.append(enemy_REF)
                            else:
                                bad_guys.append(enemy_REF)

            if all_same_value(enemies, False):
                del ROOMS[player.CURRENTROOM]['creatures stats']
            else:
                ROOMS[player.CURRENTROOM]['creatures stats'] = enemies

        # Execute battle with separated good and bad guys
        if bad_guys:
            good_guys, bad_guys = battle(player, good_guys, bad_guys, player.LASTROOM)

        # Handle NPC interactions
        if 'NPCs' in ROOMS[player.CURRENTROOM]:
            for npcname, npcstats in ROOMS[player.CURRENTROOM]['NPCs'].items():
                if ask_for_consent("Do you want to interact with this NPC") or npcstats.aggressive:
                    npcstats.interact()
                    if npcstats.aggressive:
                        ROOMS[player.CURRENTROOM]['NPCs'][npcname] = battle(player, [], [npcstats], player.LASTROOM)[1]

        player.special_ability.Tick()
        quest_manager.update_objective(f"Kill {GameState['Enemies killed']} creatures")
        for Item in GameState['collected items']:
            if isinstance(Item, item):
                quest_manager.update_objective(f"Collect {Item.name}")





if __name__ == "__main__":
    main()
