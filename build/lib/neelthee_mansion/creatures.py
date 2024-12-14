from .items import *
from .utils import *

global ValidActions

ValidActions = [
    "attack",
    "defend",
    "special",
]


class Height:
    def __init__(self, height_str="0ft 0"):
        feet, inches = map(float, height_str.split("ft "))
        if inches >= 12:
            raise ValueError("Inches must be less than 12.")
        try:
            feet = int(feet)
        except ValueError:
            pass
        try:
            inches = int(inches)
        except ValueError:
            pass
        self.feet = feet
        self.inches = inches

    def __str__(self):
        return f"{self.feet}ft {self.inches}"


class base_character:
    """
    Represents a base character in the game, including both players and creatures.
    """

    def take_damage(self, damage_taken: int = 5):
        """
        Reduces the character's hit points by the specified amount of damage.

        Args:
            damage_taken (int): The amount of damage to be subtracted from the character's hit points. Default is 5.

        Returns:
            None
        """
        string_beginning = "%*MAGENTA*%"
        if type(self) == creature:
            string_beginning = "The %*CYAN*%"
        self.hp = self.hp - damage_taken
        if self.hp < 0:
            self.hp = 0
        type_text(
            f"{string_beginning}{self.name}%*RESET*% takes {damage_taken} damage and has {self.hp} HP left!"
        )


class creature_type:
    """
    Represents the type of a creature in the game.
    """

    def __init__(self, type: str, subtype: str = None) -> None:
        """
        Initializes a creature type with the specified type and optional subtype.

        Args:
            type (str): The primary type of the creature.
            subtype (str, optional): The subtype of the creature. Defaults to None.
        """
        self.type = type
        self.subtype = subtype

    def check_type(self):
        """
        Returns the type and subtype of the creature.

        Returns:
            tuple: A tuple containing the type and subtype of the creature, or just the type if no subtype is specified.
        """
        if self.subtype:
            return self.type, self.subtype
        return self.type

    def __str__(self) -> str:
        """
        Returns a string representation of the creature type.

        Returns:
            str: A string representation of the creature type.
        """
        if self.subtype:
            return f"{self.type}, {self.subtype}"
        return f"{self.type}"


class creature(base_character):
    """
    A class representing a creature in the game.

    Attributes:
        name (str): The name of the creature.
        hp (int): The hit points of the creature.
        atpw (int): The attack power of the creature.
        dropped_items (list[str]): A list of items dropped by the creature when defeated.
        description (str): The description of the creature.
        flavor_text (str): The flavor text associated with encountering the creature.
        type (creature_type): The type of the creature.
        crit_chance (float): The chance of the creature landing a critical hit.
    """

    def __init__(
        self,
        name: str,
        hp: int,
        atpw: int,
        dropped_items: list[str] = [],
        description: str = None,
        flavor_text: str = None,
        type: creature_type = creature_type("beast"),
        crit_chance: float = 0.05,
        frendly_text: str = "",
    ):
        """
        Initializes a new creature instance.

        Args:
            name (str): The name of the creature.
            hp (int): The hit points of the creature.
            atpw (int): The attack power of the creature.
            dropped_items (list[str], optional): A list of items dropped by the creature when defeated. Defaults to [].
            description (str, optional): The description of the creature. Defaults to None.
            flavor_text (str, optional): The flavor text associated with encountering the creature. Defaults to None.
            type (creature_type, optional): The type of the creature. Defaults to creature_type('beast').
            crit_chance (float, optional): The chance of the creature landing a critical hit. Defaults to 0.05.
        """
        self.name = name
        self.hp = hp
        self.atpw = atpw
        self.difficulty = self.hp / 10 + self.atpw
        self.dropped_items = dropped_items
        self.xp = rounding(self.difficulty * 2 + len(self.dropped_items))
        self.description = (
            description if description else f"A %*CYAN*%{self.name}%*RESET."
        )
        self.flavor_text = (
            flavor_text if flavor_text else f"You see a %*CYAN*%{self.name}%*RESET*%!"
        )
        self.type = type
        self.crit_chance = crit_chance
        self.frendly = False
        self.frendly_text = frendly_text

    def type_text_flavor_text(self):
        """
        Prints the flavor text associated with encountering the creature.
        """
        type_text(self.flavor_text)

    def type_text_description(self):
        """
        Prints the description of the creature.
        """
        type_text(self.description)
        curent_holiday = get_holiday()
        if curent_holiday == "christmas":
            type_text(f"The {self.name} also has a santa hat.")
        elif curent_holiday == "easter":
            type_text(f"The {self.name} also has bunny ears.")
        elif curent_holiday == "halloween":
            if random < 0.2:
                type_text(f"The {self.name} also has a pumkin on it's head.")


class Guard(creature):
    """
    A class representing a guard that patrols in the game.

    Attributes:
        current_room (str): The current room where the guard is located.
        patrol_route (list[str]): The list of rooms the guard patrols through.
    """

    def __init__(
        self,
        name: str,
        hp: int,
        atpw: int,
        dropped_items: list[str] = [],
        description: str = None,
        flavor_text: str = None,
        type: creature_type = creature_type("humanoid"),
        crit_chance: float = 0.05,
        current_room: str = None,
        patrol_route: list[str] = None,
        patrol_type: str = "normal",
        frendly_text: str = "",
    ):
        """
        Initializes a new guard instance.

        Args:
            name (str): The name of the guard.
            hp (int): The hit points of the guard.
            atpw (int): The attack power of the guard.
            dropped_items (list[str], optional): A list of items dropped by the guard when defeated. Defaults to [].
            description (str, optional): The description of the guard. Defaults to None.
            flavor_text (str, optional): The flavor text associated with encountering the guard. Defaults to None.
            type (creature_type, optional): The type of the guard. Defaults to creature_type('humanoid').
            crit_chance (float, optional): The chance of the guard landing a critical hit. Defaults to 0.05.
            current_room (str, optional): The current room where the guard is located. Defaults to None.
            patrol_route (list[str], optional): The list of rooms the guard patrols through. Defaults to None.
            patrol_type (str): The type of patrol the guard is doing. Defaults to normal.
        """
        super().__init__(
            name,
            hp,
            atpw,
            dropped_items,
            description,
            flavor_text,
            type,
            crit_chance,
            frendly_text,
        )
        self.current_room = current_room
        self.patrol_route = patrol_route or []
        self.patrol_type = patrol_type

    def move(self, ROOMS, player):
        """
        Moves the guard depending on his patrol type.
        """

        if self.patrol_type == "normal":
            if self.patrol_route:
                current_index = self.patrol_route.index(self.current_room)
                next_index = (current_index + 1) % len(self.patrol_route)
                self.current_room = self.patrol_route[next_index]
        elif self.patrol_type == "random":
            rooms = []
            for direction, room in ROOMS[self.current_room]["directions"].items():
                rooms.append(room)
            if hasattr(room, "GetRoom"):
                self.current_room = choice(rooms).GetRoom(self.current_room)
                return
            self.current_room = choice(rooms)
        elif self.patrol_type == "follow":
            for direction, room in ROOMS[self.current_room]["directions"].items():
                if room.GetRoom(self.current_room) == player.CURRENTROOM:
                    self.current_room = room.GetRoom(self.current_room)
                    return

    def check_detection(self, player_room):
        """
        Checks if the guard has detected the player.

        Args:
            player_room (str): The current room where the player is located.

        Returns:
            bool: True if the player is detected, False otherwise.
        """
        if self.current_room == player_room and not self.frendly:
            type_text(
                f"You have been caught by {self.name} in the {self.current_room}!"
            )
            return True
        elif self.current_room == player_room and self.frendly:
            if random() <= 0.015:
                type_text(self.frendly_text)
        return False


class base_ability:
    def __init__(self, name, cooldown_time) -> None:
        self.ready = True
        self.name = name
        self.cooldown_time = cooldown_time
        self.current_cooldown = 0

    def activate(self, target: creature, damage: int = 5):
        self.ready = False
        self.current_cooldown = 0
        print(f"Ability {self.name} will be ready after {self.cooldown_time} commands.")

    def Tick(self):
        self.current_cooldown += 1
        self.check_cooldown()

    def check_cooldown(self):
        if self.current_cooldown >= self.cooldown_time and not self.ready:
            type_text(f"\nAbility {self.name} is ready to use again. ")
            self.ready = True


class supercrit_ability(base_ability):
    def __init__(self) -> None:
        super().__init__("Super Crit", 5)

    def activate(self, target: base_character, damage: int = 5):
        target.take_damage(damage * 5)
        super().activate(target, damage)


class PC(base_character):

    def __init__(
        self,
        Name: str,
        Age: int,
        Class: str,
        Level: int,
        Background: str,
        Height: Height,
        Weight: int,
        Notes: list = [],
        special_ability: base_ability = supercrit_ability(),
        NOTES: list = [],
        xp: int = None,
        inventory: inv = None,
        money: int = 0,
        weapons_atpws: list = [],
        backstory: str = "",
        CURRENTROOM: str = "",
        LASTROOM: str = None,
        Skills: list[str] = None,
    ):
        if not xp:
            if Level == 1:
                xp = 0
            else:
                xp = Level * 25
        if not LASTROOM:
            LASTROOM = CURRENTROOM
        self.name = Name
        self.Age = Age
        self.Class = Class
        self.Level = Level
        self.Background = Background
        self.Height = Height
        self.Weight = Weight
        self.BackstoryNotes = Notes
        self.NOTES = NOTES
        self.maxhp = self.Level * 10
        self.hp = self.maxhp
        self.atpw = rounding(self.Level * 1.5 + 3, 1)
        self.xp = xp
        self.inventory = (
            inventory if inventory is not None else inv()
        )  # Initialize an inv if inventory is None
        self.money = money
        self.weapons_atpws = weapons_atpws
        self.crit_chance = 0.075
        self.defending = False
        self.special_ability = special_ability
        self.backstory = backstory
        self.CURRENTROOM = CURRENTROOM
        self.LASTROOM = LASTROOM
        self.Skills = Skills

    def get_change_weapon(self, weapon_atpw: int = 0, weapon_index: int = -1):
        if weapon_atpw > 0:
            self.weapons_atpws.append(weapon_atpw)
        if weapon_index <= 0 or weapon_index > (len(self.weapons_atpws) - 1):
            self.atpw = self.Level * 2 + 3 + max(self.weapons_atpws)
        else:
            self.atpw = self.Level * 2 + 3 + self.weapons_atpws[weapon_index]

    def check_xp(self):
        self.level = rounding(self.xp / 25, 1)

    def add_xp(self, xp_added: int = 5):
        self.xp += xp_added
        self.check_xp()

    def inventory_add(self, added: list[item]):
        try:
            if not isinstance(added, list):
                added = [added]
            for item_to_add in added:
                if isinstance(item_to_add, item):
                    # Add the item to the player's inventory
                    self.inventory.append(item_to_add)

                    # Check if the added item is a weapon and update player's weapon if needed
                    if item_to_add.type == "weapon":
                        self.get_change_weapon(item_to_add.value)
                else:
                    # Print an error message if the item is not an instance of Item class
                    type_text(f"Error: {item_to_add} is not an instance of Item class")
        except Exception as e:
            # Print the full traceback if an exception occurs
            type_text(f"Error: {e}")

    def heal(self, value):
        self.hp = clamp(value, 0, self.maxhp)


class NPC(PC):
    def __init__(
        self,
        Name: str,
        Age: int,
        Class: str,
        Level: int,
        Background: str,
        Height: Height,
        Weight: int,
        Notes: list = [],
        special_ability: base_ability = supercrit_ability(),
        NOTES: list = [],
        xp: int = None,
        inventory: inv = None,
        money: int = 0,
        weapons_atpws: list = [],
        npc_role: str = "generic",  # New attribute for NPC role (e.g., merchant, enemy, etc.)
        aggressive: bool = False,  # New attribute to determine if NPC is aggressive
    ):
        super().__init__(
            Name=Name,
            Age=Age,
            Class=Class,
            Level=Level,
            Background=Background,
            Height=Height,
            Weight=Weight,
            Notes=Notes,
            special_ability=special_ability,
            NOTES=NOTES,
            xp=xp,
            inventory=inventory,
            money=money,
            weapons_atpws=weapons_atpws,
        )
        self.npc_role = npc_role
        self.aggressive = aggressive

    def interact(self):
        if self.aggressive:
            return f"{self.name} looks hostile and prepares for a fight!"
        else:
            return f"{self.name} has nothing to say to you."

    def npc_info(self):
        return f"Name: {self.name}, Age: {self.Age}, Class: {self.Class}, Level: {self.Level}, Role: {self.npc_role}, Aggressive: {self.aggressive}"


class PC_action:
    def __init__(self, value) -> None:
        if not value in ValidActions:
            raise ValueError
        self.value = value

    def __eq__(self, value: object) -> bool:
        if isinstance(value, PC_action):
            return self.value == value.value
        return self.value == value


class NPC(Guard):

    def __init__(
        self,
        name,
        hp,
        atpw,
        dropped_items=[],
        description=None,
        flavor_text=None,
        type=creature_type("humanoid"),
        crit_chance=0.05,
        current_room=None,
        patrol_route=None,
        patrol_type="normal",
        frendly_text="",
        responses={
            "introduction": "Oh, hello. I didn't see you there.",
        },
        keyword_variations={
            "introduction": ["hello", "hi", "greetings", "hey"],
        },
        generic_response="The person looks like they don't see you.",
    ):
        super().__init__(
            name,
            hp,
            atpw,
            dropped_items,
            description,
            flavor_text,
            type,
            crit_chance,
            current_room,
            patrol_route,
            patrol_type,
            frendly_text,
        )
        self.frendly = True
        # Define the responses for each topic
        self.responses = responses

        # Define keyword variations that map to the same topic
        self.keyword_variations = keyword_variations

        # To keep track of which topics the player has asked about
        self.asked_about = set()
        self.generic_response = generic_response

    def talk(self):
        while True:
            player_input = loop_til_valid_input(
                f"What do you want to say to %*BROWN*%{self.name}%*RESET*%?",
                "",
                str,
            )

            # Normalize the input to lowercase
            player_input = player_input.lower()

            # Exit the loop if the player says "goodbye"
            if player_input == "goodbye":
                type_text(f"Goodbye then. Don't get lost!")
                break

            # Check for keywords and map to corresponding response
            for topic, variations in self.keyword_variations.items():
                if any(variation in player_input for variation in variations):
                    self.asked_about.add(topic)
                    type_text(self._get_response(topic))
                    break  # Stop further keyword checks and wait for the next input
            else:
                # If no keywords found, return a generic response
                type_text(self._generic_response())

    def _get_response(self, topic):
        """Return a response from the NPC based on the topic asked."""
        return f"{self.responses[topic]}"

    def _generic_response(self):
        """Default response if no known keyword is found in the player's input."""
        return self.generic_response


class Geraldo(NPC):

    def __init__(self):
        super().__init__(
            "geraldo times",
            9999999999,
            999,
            type=creature_type("beast", "cat"),
            flavor_text="You see a cat sitting on a bookshelf.",
            description="The cat looks at you with a bored look on its face.",
            responses={
                "introduction": "Oh, you're here. Didn't think you'd make it. But I suppose I'm not the one making the decisions around here, am I?",
                "mansion": "The mansion? Well, it's not as grand as it may seem. Inside, it's as much a prison as it is a home. Everyone you find here has been trapped by Neel-thee. You’ll find that out soon enough.",
                "neel-thee": "Neel-thee? Oh, you've heard of him, have you? He’s not one to be trifled with, but then again, neither am I. But you don't actually need to escape; you could just join Neel-thee.",
                "escape": "Escape? Ha. If only it were that simple. If you're planning to leave, you'd better have a better idea than just running out the door.",
                "danger": "Danger? Well, it’s always lurking, isn’t it? You might not see it, but I feel it in the air. Something's coming, something... wrong.",
                "join": "Thinking about joining Neel-thee? Good idea, If you try and apose him, you're most likely going to die. If you want to join him, you have to go to his study. That is all I can say about this.",
            },
            keyword_variations={
                "mansion": ["mansion", "this place", "the mansion", "home", "house"],
                "neel-thee": [
                    "neel-thee",
                    "who is neel-thee",
                    "tell me about neel-thee",
                    "who is this neel-thee",
                ],
                "escape": ["escape", "leave", "get out", "break free"],
                "danger": ["danger", "something wrong", "something’s off", "dangerous"],
                "join": ["join", "joining"],
                "introduction": ["hello", "hi", "greetings", "hey"],
            },
            generic_response="The cat looks at you with those mysterious eyes, as if deciding whether or not to speak.",
        )
