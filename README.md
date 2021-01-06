# Keras Image Augmentation Generator

Data augmentation techniques are used a lot to increase the size of the dataset by performing rotations, transformations, zooming, flipping, etc.

## How to use

python <path_to_your_file> -i <input_folder> -o <output_folder> -t <number>

Required arguments:

| Parameter    | Default | Description                                           |
|--------------|---------|-------------------------------------------------------|
| -i  --image  |         | Path to the folder with the input images              |
| -o  --output |         | Path to output directory to store augmentation images |

Optional arguments:

| Parameter    | Default | Description                                           |
|--------------|---------|-------------------------------------------------------|
| -t  --total  | 100     | Number of training samples to generate                |

**Output format**

The output format is:

<output_folder>/image<number>.jpg

# Example

- After install Tensorflow Library:

## Using 1 image to generate 10

`python data_augmentation.py -i /home/gabrieloliveira/images -o /home/gabrieloliveira/images_output -t 10`

### Result 

![Lena-10](https://github.com/gabrieloliveira95/Keras_Image_Augmentation/blob/main/example/output-10.jpg?raw=true)

## Using 1 image to generate 100

`python data_augmentation.py -i /home/gabrieloliveira/images -o /home/gabrieloliveira/images_output -t 100`

### Result 

![Lena-10](https://github.com/gabrieloliveira95/Keras_Image_Augmentation/blob/main/example/output-100.jpg?raw=true)



# Required tools

[python 3.8](https://www.python.org/download/releases/3.8/)

[tensorflow 2.4.0](https://pypi.org/project/tensorflow/2.4.0/)

[numpy](https://pypi.python.org/pypi/numpy)

[pillow 8.1.0](https://pypi.org/project/Pillow/8.1.0/)

