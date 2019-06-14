lower = 0.1
upper = 1.0
length = 10

# width = [lower + x*(upper-lower)/(length-1) for x in range(length)]

width = []
for x in range(length):
    width.append(lower + x * (upper - lower)/(length-1))

width[-1] = upper
print width




