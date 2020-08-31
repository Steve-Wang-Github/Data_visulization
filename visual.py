import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()

    plt.style.use("classic")
    fig,ax = plt.subplots()
    ax.scatter(rw.x_values,rw.y_values,s=15)
    plt.show()

    kept_run = input("Make another walk? (y/n): ")
    if kept_run == "n":
        break
 