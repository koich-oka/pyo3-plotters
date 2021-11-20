NUM = 5000

def plot_rust():
    from pyo3_plotters import plot_with_plotters

    plot_with_plotters("a.png", [p/1000 for p in range(-NUM, NUM)])

def plot_matplotlib():
    import math
    import matplotlib
    matplotlib.use("agg")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(10.24, 7.68))
    fig.suptitle("Image Title")
    x = [p/1000 for p in range(-NUM, NUM)]
    y = [math.sin(p/1000) for p in range(-NUM, NUM)]
    ax.set_title("Sine and Cosine")
    ax.plot(x, y, label="Sine")
    ax.legend()
    ax.set_xticklabels(x)
    plt.savefig("b.png")
    plt.clf()
    plt.close(fig)

def main():
    plot_matplotlib()
    plot_rust()

if __name__ == '__main__':
    from line_profiler import LineProfiler
    prof = LineProfiler()
    prof.add_function(plot_rust)
    prof.add_function(plot_matplotlib)
    prof.runcall(main)
    prof.print_stats(output_unit=1e-3)
