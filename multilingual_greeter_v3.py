from typing import Dict
import random

# Populate this dictionary with at least two languages.
# Use integers for keys and strings for values.
# Example: Key = 1. Value = 'English'.
lang_dict = { 1 : 'English', 2 : "Spanish"
}

# Populate this dictionary with appropriate prompts that correspond with the ids from lang_dict.
# Example: Key = 1. Value = 'What is your name?'.
name_prompt_dict = { 1 : 'What is your name?', 2 : '¿Cuál es su nombre?'
}

# Populate this dictionary with appropriate prompts that correspond with the ids from lang_dict.
# Example: Key = 1. Value = 'Hello'.
greetings_dict = { 1 : ['Hello', 'Whats up', "How's it going"], 2 : ['Hola', 'Qué pasa', 'Cómo te va']
}


def print_language_options(lang_options: Dict[int, str]) -> None:
    """
    Given a dictionary, this functions iterates through the values and prints them out.

    :param lang_options: A dictionary
    Keys are integers representing a language id
    Values are strings representing the name of a language
    :return: None
    """
    print('Please choose a language: ')
    for key, value in lang_options.items():
        print(f"{key}: {value}")


def language_input() -> int:
    """
    This function prompts the user for a language choice.

    :return: An integer representing the language choice made by the user
    """
    choice = int(input("pick language: "))
    return choice


def language_choice_is_valid(lang_options: Dict[int, str], lang_choice: int) -> bool:
    """
    This method determines if the choice the user made is valid.

    :param lang_options: A dictionary
    Keys are integers representing a language id
    Values are strings representing the name of a language

    :param lang_choice: An integer representing the value the user selected
    :return: A boolean representing the validity of the lang_choice
    """
    return lang_choice in lang_options


def get_name_input(name_prompt_options: Dict[int, str], lang_choice: int) -> str:
    """
    This method takes in a dictionary and a key. It returns the value in the dictionary that has a key corresponding to
    the lang_choice parameter.

    :param name_prompt_options: A dictionary where the key is an integer representing an id and the value is a prompt
    in the users chosen language
    :param lang_choice: The language the user has chosen
    :return:
    """
    return name_prompt_options[lang_choice]


def name_input(name_prompt: str) -> str:
    """
    This function takes in a string and uses it to prompt the user for their name.

    :param name_prompt: A string in the user's chosen language that asks them for their name
    :return: The user's response when asked for their name
    """
    return input(name_prompt)


def greet(name: str, greetings_options: Dict[int, str], lang_choice: int) -> None:
    """
    Using the parameters provided, this function greets the user.

    :param name: The name the user provided
    :param greetings_options: A dictionary where the key is an integer representing a greeting and the value is a string
    with a greeting in the user's chosen language
    :param lang_choice: The language the user has chosen.
    :return:
    """
    random_greeting_index = random.randint(0,len(greetings_dict)-1)
    ran_greet = greetings_options

    print(greetings_options[lang_choice][random_greeting_index],name)

def select_mode():
    global lang_dict
    global name_prompt_dict
    global greetings_dict
    while True:
        choice = (input('please select mode:\n1: Admin Mode\n2: User Mode\n: '))
        if choice == '1':
            choice_2 = input('1: Add langague support\n2: Update Greeting\n: ')
            if choice_2 == '1':
                add_langauge = input('Add langue to support\n: ')
                lang_dict[len(lang_dict)+1] = add_langauge
                print("Add name prompt for ",add_langauge)
                add_name_promt = input(':')
                name_prompt_dict[len(name_prompt_dict)+1] = add_name_promt
                print('Add a greeting for ',add_langauge)
                add_greet = input(": ")
                greetings_dict[len(greetings_dict)+1] = add_greet
            elif choice_2 == '2':
                print_language_options(lang_dict)
                lang_select = int(input(': '))
                greet_change = input('What is the new greeting: ')
                greetings_dict[lang_select] = greet_change
                print(greetings_dict)
            else:
                print('Invalid input.')
        elif choice == '2':
            break
        else:
            print('Invalid input.')


if __name__ == '__main__':
    select_mode()
    print_language_options(lang_dict)
    chosen_lang = language_input()
    while language_choice_is_valid(lang_dict, chosen_lang) is False:
        print("Invalid selection. Try again.")
        chosen_lang = language_input()

    selected_prompt = f"{get_name_input(name_prompt_dict, chosen_lang)} \n"
    chosen_name = name_input(selected_prompt)
    greet(chosen_name, greetings_dict, chosen_lang)
