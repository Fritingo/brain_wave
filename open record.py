import numpy as np
import matplotlib.pyplot as plt

record = np.load("record.npy")
plt.ion()
plt.show()
fig, ax = plt.subplots(nrows=4, ncols=4)


for y in range(record.shape[1]):
    for x in range(record.shape[0]):
        plot_num = 0
        for row in ax:
            for col in row:
                if x == plot_num:
                    col.cla()
                    col.plot(record[x, y:(y+6)])
                    # print(record[x, y:y+49])
                plot_num += 1
                print(plot_num)

    plt.pause(0.03)
    plt.draw()

