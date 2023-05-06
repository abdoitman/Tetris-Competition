import random

bag = ['S', 'L', 'Z', 'O', 'T', 'I', 'J']
first=True

def get_next_shape(seed):
    random.seed(seed)
    global bag, first
    if first:
        random.shuffle(bag)
        first = False
    while True:
        if bag == []:
            bag = ['S', 'L', 'Z', 'O', 'T', 'I', 'J']
            random.shuffle(bag)
            yield bag.pop()
        else:
            yield bag.pop()
