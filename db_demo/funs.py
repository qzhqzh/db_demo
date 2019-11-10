import random
import string


def generate_random_strings():
    return ''.join(random.sample(string.ascii_letters + string.digits, 16))