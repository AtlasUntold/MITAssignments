count = 7919
n = 2
x = []

# create a list of all possible values up to 7920
l = list(range(n, (count + 1), 1))

# remove all even numbers beyond prime number 2, as they cannot be prime
for i in range(4, (count + 2), 2):
    x.append(i)
for i in range(x[0], x[-1], 2):
    l.remove(i)
x = []

# remove all multiples of prime number 3, as they cannot be prime
for i in range(6, count, 3):
    x.append(i)
for i in range(x[0], x[-1], 3):
    l.remove(i)
x = []

# remove all multiples of prime number 5, as they cannot be prime
for i in range(10, count, 5):
    x.append(i)
for i in range(x[0], x[-1], 5):
    l.remove(i)
x = []

# remove all multiples of prime number 7, as they cannot be prime
for i in range(14, count, 7):
    x.append(i)
for i in range(x[0], x[-1], 7):
    l.remove(i)
x = []

print(l)