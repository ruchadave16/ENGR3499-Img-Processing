import numpy as np
import cv2 as cv
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

    # img.ravel() -> flatten array into 1d
    # hist() -> 1536 bins (1 per row??)

def plot_histogram(data, colorscale):
    '''
    Plots a histogram of an image given an array of integers representing the pixel
    color, and the max value of the colorgrade scale.

    Args:   
        data: An array of integers representing each pixel's color value in the photo.
        colorscale: An integer representing the max value of the color scale.
    '''
    plt.hist(data, colorscale, [0, colorscale])
    plt.show()


def convert_binary(input_data, threshold):
    '''
    Converts each pixel value to 0 (white) if below a given threshold and 1 (black)
    if above a given threshold.
    Args:
        input_data: An array of integers representing each pixel's color value.
        threshold: An integer representing the color value to compare each pixel with.
    '''
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
img1 = cv.imread("high_res_2048_1536.jpg", cv.IMREAD_GRAYSCALE).ravel()
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
