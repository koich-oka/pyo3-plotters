import asyncio
import logging

LOG = logging.getLogger(__name__)
LOG.addHandler(logging.StreamHandler())
LOG.addHandler(logging.FileHandler("log.log", mode="a"))
LOG.setLevel(logging.INFO)

async def wait():
    for i in range(100):
        LOG.info("sleep")
        await asyncio.sleep(0.001)

def wait_sync(x):
    import time
    n = int(len(x) / 200)
    for i in range(n):
        LOG.info("sleep")
        time.sleep(0.001)

def plot(x, y):
    import matplotlib
    matplotlib.use("agg")
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10.24, 7.68))
    fig.suptitle("Image Title")
    axes[0].plot(x, y, label="Sine")
    LOG.info("plot")
    axes[0].legend()
    axes[1].plot(x, y, label="Sine")
    axes[1].legend()
    plt.savefig("b.png")
    LOG.info("save")
    plt.clf()
    plt.close(fig)

async def main():
    import math
    num = 10000
    x = [p/1000 for p in range(-num, num)]
    y = [math.sin(p/1000) for p in range(-num, num)]
    loop = asyncio.get_running_loop()
    await asyncio.gather(
        loop.run_in_executor(None, wait_sync, x),
        loop.run_in_executor(None, plot, x, y))

if __name__ == '__main__':
    asyncio.run(main())
    LOG.info("end")
