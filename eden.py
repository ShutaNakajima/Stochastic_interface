import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

n = 200  # Number of steps

# Create the initial lists using list comprehensions
List = [[[1 if random.random() < 3/4 else 0 for _ in range(2)] for _ in range(2*n+2)] for _ in range(2*n+2)]
FPP = [[n]* (2*n+2) for _ in range(2*n+2)]

FPP[n][n] = 0

# Update FPP
for _ in range(1, 2*n+1):
    A = np.copy(FPP)
    for i in range(2*n+1):
        for j in range(2*n+1):
            A[i][j] = min(FPP[i][j], 
                          FPP[(i+1) % (2*n+1)][j] + List[i][j][0],
                          FPP[(i-1) % (2*n+1)][j] + List[i-1][j][0],
                          FPP[i][(j+1) % (2*n+1)] + List[i][j][1],
                          FPP[i][(j-1) % (2*n+1)] + List[i][j-1][1])            
    FPP = A

# Prepare for animation
fig = plt.figure()
ims = []

xlist, ylist = [], []

for k in range(1, n//4):
    for i in range(1, 2*n+1):
        for j in range(1, 2*n+1):
            if FPP[i][j] + 1 == k:
                xlist.append(i - n)
                ylist.append(j - n)

    im = plt.scatter(xlist, ylist, color='red')
    ims.append([im])

ani = animation.ArtistAnimation(fig, ims, interval=1000)
ani.save('test.gif', writer='imagemagick')
plt.show()
