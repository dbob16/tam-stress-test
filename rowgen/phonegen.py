import random

def d(start_number:int, end_number:int):
    return random.randint(start_number, end_number)

def gen_pn():
    pn_str = f"{d(0,1)}{d(0,9)}{d(0,9)}-{d(0,9)}{d(0,9)}{d(0,9)}-{d(0,9)}{d(0,9)}{d(0,9)}{d(0,9)}"
    return pn_str
