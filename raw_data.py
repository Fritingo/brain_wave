import time

from emokit.emotiv import Emotiv

if __name__ == "__main__":
    with Emotiv(display_output=True, verbose=True) as headset:
        while True:
            t2 = time.time()
            packet = headset.dequeue()
            if packet is not None:
                # print(packet.sensors)
                # print str(time.time() - t2) + "s"
                pass
            time.sleep(0.001)
