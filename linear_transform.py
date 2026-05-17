import pathlib

from scipy.ndimage import affine_transform
import numpy as np
import matplotlib.pyplot as plt

from load_and_plot_image import get_data_from_dataframe

def create_rotation_matrix(angle: int = 30):
    angle = np.radians(30)
    c, s = np.cos(angle), np.sin(angle)
    r_mat = np.array(((c, -s), (s, c)))
    return r_mat


def shearing(shear_x=0.2, shear_y=0):
    shear_mat = np.array([1, shear_x, shear_y, 1]).reshape(2, 2)
    return shear_mat


def linear_transform_example():
    r_mat = create_rotation_matrix()
    shear_mat = shearing()
    transform_mat = r_mat.dot(shear_mat)
    print(f"transformed matrix after rotation and shearing is -> \n {transform_mat}")
    transformation = np.linalg.inv(transform_mat)
    print(f"inverse of the transformation matrix is -> \n {transformation}")


def linear_transformation_image():
    data_frame = get_data_from_dataframe("mnist_test.csv")
    ori_image = np.array(data_frame.iloc[100]).reshape(28, 28)
    r_mat = create_rotation_matrix()
    shear_mat = shearing()
    transform_mat = r_mat.dot(shear_mat)
    transformation = np.linalg.inv(transform_mat)
    offset = 28 / 2 - transformation.dot(28 / 2)
    offset = offset[0]
    t_image = affine_transform(ori_image, transformation, offset=offset)

    pathlib.Path('./transformed').mkdir(parents=True, exist_ok=True)

    # original image
    plt.figure(figsize=(2, 2))
    plt.title('original image')
    plt.imshow(ori_image, interpolation='nearest', cmap='gray')
    plt.savefig('./transformed/origional_image_digit_6.png', bbox_inches='tight', dpi=50)
    print("original image saved in folder transformed and file as origional_image_digit_6.png")
    print()

    # transformed image
    plt.figure(figsize=(2, 2))
    plt.title('transformed image')
    plt.imshow(t_image, interpolation='nearest', cmap='gray')
    plt.savefig('./transformed/transformed_image_digit_6.png', bbox_inches='tight', dpi=50)
    print("transformed image saved in folder transformed and file as transformed_image_digit_6.png")
    print()

    pass
