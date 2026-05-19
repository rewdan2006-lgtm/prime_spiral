#determines if number is a prime
def is_prime (n):
    if n<2:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
        
    return True

#generates spiral co-ordinates
def generate_spiral(n):
    x,y = 0,0
    dx, dy = 1, 0 #start moving right
    coords = []
    steps_taken = 0
    step_limit = 1
    step_count = 0

    for i in range (1 , n + 1):
        coords.append((x, y))

        x += dx
        y += dy
        steps_taken += 1
        if steps_taken == step_limit:
            steps_taken = 0
            #rotate direction clockwise
            dx , dy = -dy , dx
            step_count += 1

            #every 2 turns increase step length
            if step_count % 2 == 0:
                step_limit += 1
    return coords

#coords = generate_spiral(10)
#for i, c in enumerate(coords):
    print(i + 1, c)

# output
"""1 (0, 0)
2 (1, 0)
3 (1, 1)
4 (0, 1)
5 (-1, 1)
6 (-1, 0)
7 (-1, -1)
8 (0, -1)
9 (1, -1)
10 (2, -1)"""

# Plot the spiral with prime numbers
import matplotlib.pyplot as plt

coords = generate_spiral(1200)

x_vals = []
y_vals = []

for i, (x, y) in enumerate(coords):
    if is_prime(i + 1):
        x_vals.append(x)
        y_vals.append(y)

plt.style.use("dark_background")

plt.figure(figsize=(7, 7))
plt.scatter(x_vals, y_vals, s=0.5, c='white')

plt.axis("off")
plt.title("Ulam Spiral (Prime Number Distribution)")
plt.show()

