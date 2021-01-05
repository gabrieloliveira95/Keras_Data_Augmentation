from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import load_img
import numpy as np
import argparse
import glob
import os


def imageGenerator(index, image, args, totalImages):
    # Load the input image and convert it to a NumPy array
    # Reshape it to have an extra dimension

    print(f"{index}/{totalImages}: {image}")
    image = load_img(image)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)

    # Image generator for data augmentation
    # Initialize the total number of images generated thus far
    aug = ImageDataGenerator(
        rotation_range=30,
        zoom_range=0.15,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.15,
        horizontal_flip=True,
        fill_mode="nearest")
    total = 0

    # Generator
    imageGen = aug.flow(image, batch_size=1, save_to_dir=args["output"],
                        save_prefix="image", save_format="jpg")

    imageGen
    for i, image in enumerate(imageGen):
        if i == args["total"]:
            break


if __name__ == "__main__":

    # Arguments parser
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True,
                    help="Path to the folder with the input images")
    ap.add_argument("-o", "--output", required=True,
                    help="Path to output directory to store augmentation images")
    ap.add_argument("-t", "--total", type=int, default=100,
                    help="#Number of training samples to generate")
    args = vars(ap.parse_args())

    if args["total"] < 0:
        # Invalid Argument
        print('Invalid Argument ', args["total"])
        exit(22)

    # Read Images and store in a list
    imagesPath = []
    try:
        for file in glob.glob(f'{args["image"]}*.jpg'):
            imagesPath.append(file)

        if len(imagesPath) == 0:
            raise Exception('No JPG Images in Intput Folder')
    except Exception as e:
        print(e)
        # No such file or directory 2
        exit(2)

    # Create Output Path
    if not os.path.exists(args["output"]):
        os.makedirs(args["output"])
        print(f'Created Output Folder in --> {args["output"]}')

    for i, images in enumerate(imagesPath):
        imageGenerator(index=i+1, image=images, args=args,
                       totalImages=len(imagesPath))
