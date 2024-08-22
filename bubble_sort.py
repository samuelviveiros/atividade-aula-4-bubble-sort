import time


print('Loading integers into memory...')
L = []
with open('input.txt', 'r') as integers:
    for integer in integers:
        L.append(int(integer))


print('Executing `Bubble Sort` algorithm...')

start_time = time.time()

n = len(L)
j = 1
while j <= n:
    i = 0
    while i <= n - 2:
        if L[i] > L[i + 1]:
            t = L[i]
            L[i] = L[i + 1]
            L[i + 1] = t
        i += 1
    j += 1

end_time = time.time()

print(f'Execution time: {end_time - start_time:.2f} seconds')

print('Saving changes to file...')
with open('output.txt', 'w') as integers:
    for integer in L:
        integers.write(str(integer) + '\n')

print('Done!')
