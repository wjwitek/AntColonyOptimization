import matplotlib.pyplot as plt
import cv2

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

def browse_images(iters):
    root_wind = "Motion detector"
    cv2.namedWindow(root_wind)
    cv2.createTrackbar("Stage", root_wind, 0, iters-1, lambda x: x)
    cv2.setTrackbarPos("Stage", root_wind, 0)
    while True:
        cur_image = cv2.getTrackbarPos("Stage", root_wind)
        img = cv2.imread(f"img_{cur_image}.jpg",0)
        cv2.imshow(root_wind, img)
        if cv2.waitKey(10) == ord('q'):
            break
