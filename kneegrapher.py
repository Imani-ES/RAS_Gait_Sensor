import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import bluetooth_comms.desktop as btd
import multiprocessing
import time

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
xs = []
ys = []

def animate(i, xs, ys):
    #Obtain knee sensor reading if calibrated
    print(btd.fullyCalibrate)
    if btd.fullyCalibrate:
        angle = btd.normLen1

        #Add knee data over realtime
        xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
        ys.append(angle)

        #Limit it to 20 items
        xs = xs[-20:]
        ys = ys[-20:]

        #Draw x and y lists
        ax.clear()
        ax.plot(xs, ys)

        #Format plot
        plt.xticks(rotation=45, ha='right')
        plt.subplots_adjust(bottom=0.3)
        plt.title('Knee Angle Over Time')
        plt.ylabel('Knee Angle (degrees)')


def runAnimation():
    global fig, ax, xs, ys
    print('Working')
    ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
    plt.show()

if __name__ == "__main__":
    manager = multiprocessing.Manager()
    job_for_core2 = multiprocessing.Process(target=runAnimation, args=())
    job_for_core2.start()
    job_for_core1 = multiprocessing.Process(target=btd.main, args=())
    job_for_core1.start()

