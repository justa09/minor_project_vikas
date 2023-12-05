import random
import string

def generate():
    all_char =string.digits

    s = ''
    for _ in range(5):
        s += random.choice(all_char)

    return s
