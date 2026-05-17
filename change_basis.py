import numpy as np

def construct_change_analyze_basis():
    """
    Calculate and verify change of basis matrix between two linearly independent bases.
    """
    # define a square of standard basis, which is linearly independent (identity Matrix)
    # in mumpy identity matrix constructed using "eye" function where diagonal elements are 1
    std_vector = np.eye(3, 3)

    print(f"The Standard Matrix is \n {std_vector}")

    # define a new basis vector of your choice of 3x3 dimension
    new_basis_vector = np.array([[2, 4, 3], [5, 6, 8], [9, 10, 11]])

    # check if bases are linearly independent
    if np.linalg.det(new_basis_vector) == 0 or np.linalg.det(std_vector) == 0:
        raise ValueError("Bases must be linearly independent.")
    else:

        # calculate change of basis matrix
        change_of_basis_mat = np.linalg.inv(new_basis_vector) @ std_vector
        print(f"The change of Basis Matrix is \n {change_of_basis_mat}")

        # revert back and check
        org_new_basis_mat = np.linalg.inv(std_vector) @ new_basis_vector
        print(f"The reverted Origional Matrix is -> \n {org_new_basis_mat}")
