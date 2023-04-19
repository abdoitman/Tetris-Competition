import random

bag = ['S', 'L', 'Z', 'O', 'T', 'I', 'J']
random.shuffle(bag)

def get_next_shape():
    global bag
    while True:
        if bag == []:
            bag = ['S', 'L', 'Z', 'O', 'T', 'I', 'J']
            random.shuffle(bag)
            yield bag.pop()
        else:
            yield bag.pop()
