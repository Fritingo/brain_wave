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
            for y in range(record.shape[1]):
                for x in range(record.shape[0]):
                    if x == plot_num:
                        col.cla()
                        col.plot(record[x, y])
                        print(record[x, y])
            plot_num += 1
            print(plot_num)
    plt.pause(0.03)
    plt.draw()


# plt.show()