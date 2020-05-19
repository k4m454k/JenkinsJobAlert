from PyInquirer import style_from_dict, Token, prompt, Separator


def make_choice_selector(caption: str,message: str, choices: list):
    prepared_choice_data = {
        'type': 'list',
        'name': caption,
        'message': message,
        'choices': choices
    }
    answer = prompt([prepared_choice_data])
    return answer
