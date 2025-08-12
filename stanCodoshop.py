"""
File: stanCodoshop.py
Name: 
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    r = pixel.red 
    g = pixel.green
    b = pixel.blue 
    color_distance = ((r - red)**2 + (g - green)**2 + (b - blue)**2) ** 0.5

    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    list_red = []
    list_green = []
    list_blue = []
    for i in pixels:
        r = i.red
        list_red.append(r)

    for i in pixels:
        g = i.green
        list_green.append(g)

    for i in pixels:
        b = i.blue
        list_blue.append(b)
    
    avg_red = int(sum(list_red) / len(list_red))
    avg_green = int(sum(list_green) / len(list_green))
    avg_blue  = int(sum(list_blue) / len(list_blue))

    rgb = [avg_red, avg_green, avg_blue]
           
    return rgb


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    current_dist = 100000000000
    current_pixel = 'abc'
    avg = get_average(pixels)
    for pixel in pixels:
        dist = get_pixel_dist(pixel, avg[0], avg[1], avg[2])
        if dist < current_dist:
            current_dist, current_pixel = dist, pixel
    
    return current_pixel
        
def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    
    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect
    
    for x in range(width):
        for y in range(height):
            pixels = []
            for img in images:
                pixel = img.get_pixel(x, y)
                pixels.append(pixel)
            
            best_pixel = get_best_pixel(pixels)
            # 5. 將這個 pixel 的顏色指定給 result 圖片對應位置
            result.set_pixel(x, y, best_pixel)
    

    # ----- YOUR CODE ENDS HERE ----- #

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
