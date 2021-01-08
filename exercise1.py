import random

def get_number_input(prompt_text, input_type=int):
    user_input = input(prompt_text)
    try:
        number_input = input_type(user_input)
    except ValueError:
        print("Not a number! Try again!")
        number_input = get_number_input(prompt_text, input_type)
    return number_input


if __name__ == "__main__":
    random_number = random.randint(1,100)
    while (user_guess:= get_number_input("Enter a number: ", int)) != random_number:
        if user_guess < random_number:
            print('Too small! Try again!')
        else:
            print('Too large! Try again!')
    else:
        print(f'Right! The answer is {user_guess}')
