import math
import os.path


def get_number(given_min=-math.inf, given_max=math.inf, prompt="Please enter a number:", force_no_prompt=False):
    adj_prompt = prompt
    real_min = given_min
    real_max = given_max
    if given_min > given_max:
        real_min = given_max
        real_max = given_min
    if -math.inf < real_min and real_max < math.inf:
        adj_prompt += " ( " + str(real_min) + " - " + str(real_max) + " )"
    elif real_min != -math.inf:
        adj_prompt += "( min: " + str(real_min) + " )"
    elif real_max != math.inf:
        adj_prompt += "( max: " + str(real_min) + " )"
    if "\n" not in adj_prompt:
        adj_prompt += "\n"
    if force_no_prompt:
        adj_prompt = ""
    while True:
        keyboard_input = input(adj_prompt)
        if not keyboard_input.isnumeric():
            print("ERROR - You must enter a number.")
        else:
            convert_input = int(keyboard_input)
            if convert_input < real_min or convert_input > real_max:
                print("ERROR - Number not inside the required range.")
                print(f"Number must be between {real_min} and {real_max}")
            else:
                return convert_input


def menu_selector(menu_list, prompt="Please select an option:"):
    if not hasattr(menu_list, "__iter__"):
        print("ERROR - Given menu not a list")
        exit(-1)
    if len(menu_list) < 1:
        print("ERROR - Given menu is empty")
        exit(-1)
    for menu_item in menu_list:
        if not isinstance(menu_item, str):
            print("ERROR - Menu contains non-string items")
            exit(-1)
    print(prompt)
    for item_index in range(len(menu_list)):
        print(str(item_index+1) + " - " + menu_list[item_index])
    return get_number(1, len(menu_list), "", True)


def file_overwrite(file_name=""):
    if file_name != "":
        print("File name: " + str(file_name) + " already exists, overwrite?")
    else:
        print("File already exists, overwrite?")
    return yes_no()


def safe_file_write(file_path):
    outcome = True
    if os.path.exists(file_path):
        outcome = file_overwrite(file_path)
    if outcome:
        return open(file_path, "w")
    else:
        return None


def yes_no(prompt="Yes / No", default_yes=False, invert=False):
    adj_prompt = prompt
    if "\n" not in adj_prompt:
        adj_prompt += "\n"
    keyboard_input = input(adj_prompt)
    keyboard_input = keyboard_input.lower()
    if keyboard_input == "yes" or keyboard_input == "y":
        answer = True
    elif keyboard_input == "no" or keyboard_input == "n":
        answer = False
    else:
        answer = default_yes
    if invert:
        return not answer
    else:
        return answer
