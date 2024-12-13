import matplotlib.pyplot as plt
import numpy as np
import cv2

# Initialize the plot
fig, ax = plt.subplots()
image_data = np.zeros((32, 32, 3), dtype=np.uint8)  # Create a blank canvas
plot = ax.imshow(image_data)


def image_creator(img):
    # import image and get info?
    # img = cv2.imread('/home/marius/Downloads/smiley.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # img will be a numpy array of the img
    #print(img)
    #print(img.shape)
    count = 0
    img_vals = np.zeros((32, 32, 3), dtype=np.uint8)
    for i in range(32):
        for j in range(32):

            # start x and y pixel
            x = i * int(img.shape[0]/32)
            y = j * int(img.shape[1]/32)

            # go through all pixels in the grid
            red_avg = 0
            green_avg = 0
            blue_avg = 0

            # print(int(img.shape[0]/32))
            # print(int(img.shape[1]/32))
            startx = x
            starty = y
            while x < startx + int(img.shape[0]/32):
                while y < starty + int(img.shape[1]/32):

                    red_avg += int(img[x, y, 0])
                    green_avg += int(img[x, y, 1])
                    blue_avg += int(img[x, y, 2])
                    y += 1

                x += 1


            img_vals[i][j] = [int(red_avg/int(img.shape[0]/32)), int(green_avg / int(img.shape[0]/32)), int(blue_avg / int(img.shape[0]/32))]
            count += 1

    return img_vals

def matrix_creator(img_vals):
    # Ok, so I'm thinking that I do something where I have a list of arrays that are (32, 32, 3) and then I iterate through them
    image_array = []

    #for i in range(255):
    image_data[:] = [0, 0, 0]
    for x in range(32):
        for y in range(32):
            val = img_vals[x,y]
            #if val[0] != 255 and val[1] != 255 and val[2] != 255:
            #val += 10
            image_data[x, y] = val

    image_array.append(np.copy(image_data))
    return image_array


def show_matrix(image_array):
    # print(image_array)
    #while True:
    for i in range(len(image_array)):
        plot.set_data(image_array[i])
        plt.pause(0.05)
