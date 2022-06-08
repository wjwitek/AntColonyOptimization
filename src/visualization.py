import matplotlib.pyplot as plt

def create_plot(points, path, iter):
    first = True
    for x, y in points:
        if first: 
            plt.plot(x, y, marker="o", markersize=10, markerfacecolor="red", markeredgecolor="red")
            first = False
        else: plt.plot(x, y, marker="o", markersize=10, markerfacecolor="blue", markeredgecolor="blue")

    for i in range(1, len(path)):
        x1, y1 = points[path[i-1]][0], points[path[i-1]][1]
        x2, y2 = points[path[i]][0], points[path[i]][1]

        plt.plot([x1,x2], [y1,y2], "ko-")

    plt.savefig(f"img_{iter}.jpg")
    plt.clf()
