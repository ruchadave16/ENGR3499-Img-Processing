import numpy as np
import cv2 as cv
import matplotlib.image as mpimg
import matplotlib.pyplot as plt


def plot_histogram(data, colorscale):
    # img.ravel() -> flatten array into 1d
    # hist() -> 1536 bins (1 per row??)
    plt.hist(data, colorscale, [0, colorscale])
    plt.show()


def convert_binary(input_data, threshold):
    i = 0
    data = []
    while i < len(input_data):
        if input_data[i] < threshold:
            data.append(0)
        else:
            data.append(255)
        i += 1
    return data


# Read all 4 images
img1 = cv.imread("high_res_2048_1546.jpg", cv.IMREAD_GRAYSCALE).ravel()
img2 = cv.imread("low_res_2.jpg", cv.IMREAD_GRAYSCALE).ravel()
img3 = cv.imread("pink_filter.jpg", cv.IMREAD_GRAYSCALE).ravel()
img4 = cv.imread("yellow_filter.jpg", cv.IMREAD_GRAYSCALE).ravel()

# cv.imshow("image", img) # Plot the image
plot_histogram(img1, 256)
plot_histogram(img2, 256)
plot_histogram(img3, 256)
plot_histogram(img4, 256)

new_img1 = convert_binary(img1, 100)
plt.imshow(new_img1.reshape(1536, 2048), cmap="gray")
plt.show()

new_img2 = convert_binary(img2, 100)
plt.imshow(new_img2.reshape(1536, 2048), cmap="gray")
plt.show()

new_img3 = convert_binary(img3, 100)
plt.imshow(new_img3.reshape(1536, 2048), cmap="gray")
plt.show()

new_img4 = convert_binary(img4, 100)
plt.imshow(new_img4.reshape(1536, 2048), cmap="gray")
plt.show()
# plot_histogram(img1, 2)
