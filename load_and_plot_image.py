import shutil

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pathlib

import time

global image_data


def get_data_from_dataframe(filename: str):
    """
    Retrieves data from a CSV file containing MNIST test data, extracts relevant features,
    and returns the data as a pandasDataFrame. The function globally assigns the extracted
    data to the `image_data` variable for further use.

    :param: None
    :return: is A pandasDataFrame containing the MNIST test data without the 'label' column
    """
    global image_data
    df = pd.read_csv(filename, header=0, encoding='ISO-8859-1', sep=',')
    df_data = df.drop(['label'], axis=1)
    image_data = df_data
    return df_data


def pick_image(n: int = 100):
    """
    Picks an image from the MNIST test data based on the provided index.

    :param n: The index of the image to pick (default is 100)
    :return: A pandas Series representing the selected image
    """
    global image_data
    return image_data.iloc[n, :]


def plot_image():
    """
    Plot an image represented as a 28x28 grayscale array with nearest-neighbor interpolation.

    This function retrieves an image, processes it into a numpy array, reshapes it into a
    28x28 matrix that represents a grayscale image, and displays it using Matplotlib.

    :raises ValueError: If the image cannot be properly reshaped into a 28x28 matrix.

    :return: None
    """

    image = pick_image()
    arr = np.array(image, dtype=np.uint8)
    arr = arr.reshape(28, 28)
    plt.figure(figsize=(2, 2))
    plt.imshow(arr, interpolation='nearest', cmap='gray')
    plt.title('Chosen 100th Image From DataSet ->  Digit: 6 ')

    ## remove earlier image if exists
    shutil.rmtree(path='./original_image', ignore_errors=True)
    time.sleep(1)

    ## saving file
    pathlib.Path('./original_image').mkdir(parents=True, exist_ok=True)
    plt.savefig('./original_image/original_digit_6.png', bbox_inches='tight', dpi=50)

    print("image saved in folder original_image and file as original_digit_6.png")
    print()