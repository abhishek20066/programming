import math

def gst_amount(amount, rate=18):
    return amount * rate / 100


def boxes_needed(quantity, box_size):
    return math.ceil(quantity / box_size)


def round_down_to_five(amount):
    return math.floor(amount / 5) * 5