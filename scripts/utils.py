from matplotlib import pyplot as plt
import cv2 as cv
import numpy as np


def imshow(image: np.array, title: str):
    plt.imshow(image)
    plt.title(title)
    plt.axis("off")


def plot_world_point(
    image: np.array, x: float, y: float, z: float, M: float
) -> tuple[int, int]:
    x = np.array([x, y, z, 1])
    pixel_coordinates = M @ x
    pixel_coordinates /= pixel_coordinates[-1]
    point = tuple(map(int, pixel_coordinates[:2]))
    cv.circle(image, center=point, radius=2, color=(179, 66, 245), thickness=-1)
    plt.imshow(image)
    return point


def plot_plane_point_2D(x: float, y: float, h: np.array) -> tuple[int, int]:
    maracana2 = cv.imread("maracana2.jpg")
    x = np.array([x, y, 1])
    pixel_coordinates = h @ x
    pixel_coordinates /= pixel_coordinates[2]
    point = tuple(map(int, pixel_coordinates[:2]))
    cv.circle(maracana2, center=point, radius=2, color=(250, 0, 245), thickness=-1)
    plt.imshow(maracana2)
    return point
