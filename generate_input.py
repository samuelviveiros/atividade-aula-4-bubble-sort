from random import randint

MAX_SIZE = 100_000

# Generate a text file with 1 billion of random integers
print('Generating input file...')
with open('input.txt', 'w') as integers:
    for i in range(1, MAX_SIZE + 1):
        integers.write(str(randint(1, MAX_SIZE)) + '\n')
