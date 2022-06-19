import os
import random
import string


def get_random_string(length):
    # Random string with the combination of lower and upper case
    letters = string.ascii_letters
    result_str = "".join(random.choice(letters) for i in range(length))
    return result_str


def delete_file(path):
    if os.path.isfile(path):
        os.remove(path)
