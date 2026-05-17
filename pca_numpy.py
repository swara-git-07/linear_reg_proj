import pathlib

import numpy as np
import matplotlib.pyplot as plt
from load_and_plot_image import get_data_from_dataframe


def pca_numpy():
    image_mat_df = get_data_from_dataframe("mnist_test.csv")

    # get data matrix from loaded image dataframe
    image = np.array(image_mat_df.iloc[100]).reshape(28, 28)

    # Center the data by subtracting the mean
    image_mean = np.mean(image, axis=0)
    image_centered = image - image_mean

    # calculate covariance matrix using numpy cov()
    cov_matrix = np.cov(image_centered, rowvar=False)

    # decomposing the covariance matrix using numpy eigh()
    eigenvals, eigenvecs = np.linalg.eigh(cov_matrix)

    # Sort and select top K reversed components based on eigenvalues
    k = 4
    idx = np.argsort(eigenvals)[::-1]
    top_k_eigenvecs = eigenvecs[:, idx[:k]]

    # Project the image using dot product
    # Reconstruct again by adding to original image
    projected = np.dot(image_centered, top_k_eigenvecs)
    reconstructed = np.dot(projected, top_k_eigenvecs.T) + image_mean

    ## original image
    plt.imshow(image, interpolation='nearest', cmap='gray')
    plt.title('Chosen 100th Image From DataSet ->  Digit: 6 ')

    ## saving file
    pathlib.Path('./pca').mkdir(parents=True, exist_ok=True)
    plt.savefig('./pca/original_digit_6.png', bbox_inches='tight', dpi=50)
    print("original image saved in folder pca and file as original_digit_6.png")
    print()
    # draw the reconstructed image
    plt.figure(figsize=(2, 2))
    plt.imshow(reconstructed, cmap='gray')
    plt.title(f'Reconstructed with {k} Components')
    plt.savefig('./pca/pca_digit_6.png', bbox_inches='tight', dpi=50)
    print("PCA transformed image saved in folder pca and file as pca_digit_6.png")
    print()
