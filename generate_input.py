from random import randint

#MAX_SIZE = 2600  # ~ 1 sec
MAX_SIZE = 3750  # ~2 sec

print('Generating input file...')
with open('input.txt', 'w') as integers:
    for i in range(1, MAX_SIZE + 1):
        integers.write(str(randint(1, MAX_SIZE)) + '\n')
