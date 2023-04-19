import random

bag = ['S', 'L', 'Z', 'O', 'T', 'I', 'J']

def get_next_shape():
    global bag
    while True:
        if bag == []:
            bag = ['S', 'L', 'Z', 'O', 'T', 'I', 'J']
            random.shuffle(bag)
            yield bag.pop()
        else:
            random.shuffle(bag)
            yield bag.pop()