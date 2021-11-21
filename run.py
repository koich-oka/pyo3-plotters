NUM = 18200

def plot_rust():
    from pyo3_plotters import plot_with_plotters

    plot_with_plotters("a.png", [p/1000 for p in range(-NUM, NUM)])

def plot_matplotlib():
    import math
    import matplotlib
    matplotlib.use("agg")
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10.24, 7.68))
    fig.suptitle("Image Title")
    x = [p/1000 for p in range(-NUM, NUM)]
    y = [math.sin(p/1000) for p in range(-NUM, NUM)]
    axes[0].plot(x, y, label="Sine")
    axes[0].legend()
    axes[1].plot(x, y, label="Sine")
    axes[1].legend()
    plt.savefig("b.png")
    plt.clf()
    plt.close(fig)

def plot_plotly():
    import math
    import plotly.express as px
    from kaleido.scopes.plotly import PlotlyScope
    scope = PlotlyScope(
        plotlyjs="https://cdn.plot.ly/plotly-latest.min.js",
        # plotlyjs="/path/to/local/plotly.js",
    )
    x = [p/1000 for p in range(-NUM, NUM)]
    y = [math.sin(p/1000) for p in range(-NUM, NUM)]
    fig = px.line({'x': x, 'y': y})
    with open("c.png", "wb") as f:
        f.write(scope.transform(fig, format="png"))

def main():
    plot_rust()
    plot_matplotlib()
    # plot_plotly()

if __name__ == '__main__':
    from line_profiler import LineProfiler
    prof = LineProfiler()
    prof.add_function(plot_rust)
    prof.add_function(plot_matplotlib)
    prof.add_function(plot_plotly)
    prof.runcall(main)
    prof.print_stats(output_unit=1e-3)
