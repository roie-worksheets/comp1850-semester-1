L = int(input("Length of sequence: "))

sequence = [0]

for n in range(1, L):
    if (value := sequence[n - 1] - n) > 0:
        sequence.append(value)
    else:
        sequence.append(sequence[n - 1] + n)

print(*sequence)