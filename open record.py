import numpy as np
import matplotlib.pyplot as plt

record = np.load("record.npy")
plt.ion()
fig, ax = plt.subplots(nrows=4, ncols=4)
plt.draw()

for c in range(len(record)):
    plot_num = 0
    for row in ax:
        for col in row:

            sensor_num = 0
            # print(type(self.sensors))
            for x in range(record.shape[0]):
                for y in range(record.shape[1]):
                    if x == plot_num:
                        col.cla()
                        col.plot(record[x, y])
                        print(record[x, y])
        plot_num += 1
    plt.draw()
    plt.pause(0.01)

plt.show()