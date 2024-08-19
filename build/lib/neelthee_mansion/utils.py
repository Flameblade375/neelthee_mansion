try:
    # Importing everything with wildcards
    from random import *
    from sys import *
    from time import *
    from datetime import *
    from pickle import *
    from string import *
    from socket import *
    from re import *
    from platform import *
    from psutil import *
    from playsound import *


    # Importing the whole module
    import pickle as pk
    import inspect
    import threading
    import json
    import requests
    import keyboard
    import pandas as pd
except ImportError as e:
    print(f"ImportError: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")

"""
This module, named 'utils', provides a collection of utility functions and classes to streamline common programming tasks and enhance code readability. It includes functionalities for system 
interaction, text formatting, file operations, internet connectivity checks, logging, and more.

The module imports various standard and third-party libraries to access diverse functionalities, such as keyboard interactions, random number generation, date and time manipulation, HTTP 
requests, and audio playback.

Key components include:
- Utility functions for tasks like executing Python code from strings, playing sound files, truncating text, downloading files from URLs, checking internet connectivity, generating unique 
identifiers, and formatting dates.
- Utility classes for managing text formatting, converting input strings to boolean values, and logging messages with timestamps.
- A message log class for handling and persisting log data to files.
- A decorator to log function calls with timestamps.

These utilities aim to simplify development processes, promote code reuse, and improve the efficiency of Python applications.
"""

def perform_action_on_matches(input_list, target, action):
    """
    Perform an action on all items in the list that are the same as the target.

    :param input_list: List of items
    :param target: The target item to match
    :param action: A function that defines the action to perform on matched items
    :return: The updated list
    """
    matches = get_all_matches(input_list, target)
    for i in range(len(input_list)):
        if input_list[i] in matches:
            input_list[i] = action(input_list[i])
    return input_list

def get_all_matches(input_list, target):
    """
    Return a list of all items in the list that are the same as the target.

    :param input_list: List of items
    :param target: The target item to match
    :return: List of matched items
    """
    return [item for item in input_list if item == target]

def last_index(lst):
    if isinstance(lst, list):
        if lst:
            return len(lst) - 1
    return None

def has_named_arg(func, arg_name):
    """
    Check if the function 'func' has an argument named 'arg_name'.
    
    :param func: Function to inspect
    :param arg_name: Name of the argument to check
    :return: True if the argument exists, False otherwise
    """
    signature = inspect.signature(func)
    return arg_name in signature.parameters

def get_random_string(length=10):
    return ''.join(choice(ascii_letters + digits) for _ in range(length))

def retry_on_exception(func, retries=3):
    for _ in range(retries):
        try:
            return func()
        except Exception as e:
            print(f"Retry due to: {e}")
    print("Max retries exceeded")

def measure_execution_time(func):
    start_time = time()
    result = func()
    end_time = time()
    print(f"Execution time: {end_time - start_time} seconds")
    return result

def int_to_binary(n):
    return bin(n)[2:]

def binary_to_int(b):
    return int(b, 2)

def str_to_base64(s):
    import base64
    return base64.b64encode(s.encode()).decode()

def base64_to_str(b64):
    import base64
    return base64.b64decode(b64.encode()).decode()

def get_memory_usage():
    memory_info = virtual_memory()
    return memory_info.percent

def get_os_info():
    return system(), release()

def get_process_list():
    return [(p.pid, p.info['name']) for p in process_iter(['name'])]

def get_ip_address():
    return gethostbyname(gethostname())

def download_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        return None

def get_host_name():
    return gethostname()

def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == reverse_string(cleaned)

def add_days(date, days):
    return date + timedelta(days=days)

def get_days_between_dates(date1, date2):
    delta = date2 - date1
    return delta.days

def get_weekday(date):
    return date.strftime("%A")

def word_count(s):
    from collections import Counter
    words = s.split()
    return Counter(words)

def get_cpu_usage():
    return cpu_percent(interval=1)

def get_disk_space():
    usage = disk_usage('/')
    return usage.free / (1024 ** 3)  # Free space in GB

def get_system_uptime():
    return time() - boot_time()

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return match(pattern, email) is not None

def is_valid_url(url):
    import validators
    return validators.url(url)

def is_valid_ip(ip):
    import ipaddress
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def celsius_fahrenheit_conversion(Temp, IsCelsius = True):
    if IsCelsius:
        return (Temp * 9/5) + 32
    else:
        return 5 / 9*(Temp - 32)

def json_to_xml(json_data):
    import json
    import dicttoxml
    return dicttoxml.dicttoxml(json.loads(json_data))

def flatten_list(nested_list):
    import itertools
    return list(itertools.chain(*nested_list))

def merge_dicts(*dicts):
    result = {}
    for d in dicts:
        result.update(d)
    return result

def shuffle_list(lst):
    import random
    shuffle(lst)
    return lst

def date_difference(date1, date2):
    delta = date2 - date1
    return delta.days

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_current_time_in_timezone(timezone_str):
    import pytz
    tz = pytz.timezone(timezone_str)
    return datetime.now(tz)

def clamp(value, min = 0, max = 0):
    if value < min:
        value = min
    if value > max:
        value = max
    return value

def is_executable(code_str):
    try:
        compile(code_str, '<string>', 'exec')
        return True
    except SyntaxError:
        return False

def play_sound(sound_file):
    playsound(sound_file)

def truncate_text(text: str, max_length: int = 234):
    return text[:max_length] + '...' if len(text) > max_length else text

def download_file(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)

def check_internet_connection():
    try:
        create_connection(("www.google.com", 80))
        return True
    except OSError:
        return False

def get_current_timestamp():
    return datetime.now().timestamp()

def format_date(date: datetime):
    return date.strftime("%Y-%m-%d %H:%M:%S")

def delay(seconds):
    sleep(seconds)

# All classes:
class TextEdits:
    # Text colors
    BLACK = '\033[30m'      # Black
    RED = '\033[31m'        # Red
    GREEN = '\033[32m'      # Green
    YELLOW = '\033[33m'     # Yellow
    BLUE = '\033[34m'       # Blue
    MAGENTA = '\033[35m'    # Magenta
    CYAN = '\033[36m'       # Cyan
    WHITE = '\033[37m'      # White
    
    # Custom colors (adjusted for more contrast)
    PINK = '\033[38;5;205m'  # Brighter Pink (ANSI 256-color code)
    PURPLE = '\033[38;5;53m' # Darker Purple (ANSI 256-color code)
    ORANGE = '\033[38;5;208m' # Orange (ANSI 256-color code)
    BROWN = '\033[38;5;94m'  # Brown (ANSI 256-color code)

    # Background colors
    BLACK_BG = '\033[40m'   # Black background
    RED_BG = '\033[41m'     # Red background
    GREEN_BG = '\033[42m'   # Green background
    YELLOW_BG = '\033[43m'  # Yellow background
    BLUE_BG = '\033[44m'    # Blue background
    MAGENTA_BG = '\033[45m' # Magenta background
    CYAN_BG = '\033[46m'    # Cyan background
    WHITE_BG = '\033[47m'   # White background

    # Text styles
    BOLD = '\033[1m'        # Bold text
    UNDERLINE = '\033[4m'   # Underlined text
    BLINK = '\033[5m'       # Blinking text, nonworking
    REVERSE = '\033[7m'     # Reversed (invert the foreground and background colors)
    HIDDEN = '\033[8m'      # Hidden (invisible) text
    LINETHROUGH = '\033[9m' # Strikethrough (linethrough) text
    ITALIC = '\033[3m'

    # Reset all formatting
    RESET = '\033[0m'

class Y_N:
    def __init__(self, Value: str) -> None:
        Value = Value.lower()
        if Value == 'y':
            Value = True
        elif Value == 'n':
            Value = False
        else:
            raise ValueError("That wasn't Y or N")
        self.value = Value

def all_same_value(lst, value):
    return all(x == value for x in lst)

def generate_id(start_str: str = "ObjectName_ObjectDetals", length: int = 32):
    characters = ascii_letters + digits
    random_part = ''.join(choice(characters) for _ in range(length - len(start_str)))
    return start_str + "_" + random_part

def type_text(text: str, newline: bool = True, delay: float = 0.075, colorTrue: bool = True):
    """
    Function to type text with optional color formatting.

    Arguments:
    text -- the text to be typed out
    newline -- whether to print a newline at the end (default: True)
    delay -- delay between each character in seconds (default: 0.075)
    """
    color_start = '%*'
    color_end = '*%'

    key_pressed = False

    def on_key_event(e):
        nonlocal key_pressed
        key_pressed = True

    keyboard.hook(on_key_event)
    
    i = 0
    while i < len(text):
        if key_pressed:
            delay = 0

        if text[i:i+len(color_start)] == color_start:
            color_end_index = text.find(color_end, i)
            if color_end_index != -1:
                color_code = text[i+len(color_start):color_end_index]
                color = getattr(TextEdits, color_code, TextEdits.RESET)
                if colorTrue:
                    stdout.write(color)
                i = color_end_index + len(color_end)
                continue  # Skip to the next iteration

        stdout.write(text[i])
        i += 1
        stdout.flush()
        sleep(delay)
        
    stdout.write(TextEdits.RESET)  # Reset color
    stdout.flush()
    if newline:
        print()
    
    keyboard.unhook(on_key_event)

def rounding(x: int, base: int = 5):
    return int(base * round(x/base))

def loop_til_valid_input(input_text: str, bad_text: str, Class: classmethod, delay: int = 0.075, input_method: str = '>'):
    while True:
        try:
            type_text(input_text, delay=delay)
            value = Class(input(input_method))
            break
        except ValueError:
            type_text(bad_text)
    return value
