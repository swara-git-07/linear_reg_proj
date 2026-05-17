import shutil
import change_basis, linear_transform, load_and_plot_image, pca_numpy

def command_menu():
    choice = ""
    print(f"0: All - default")
    print(f"1: Draw the image  ")
    print(f"2: Example - Change the basis  ")
    print(f"3: Linear Transform by rotation and shearing application on the image ")
    print(f"4: PCA-Application of the image ")
    print(f"5: clean all images and associated folders created")

    choice = input("Enter your choice; any other key to quit -> (0-5):  ")
    return choice


def execute_command(step_choice: int):
    match step_choice:
        case 1:
            step1()
            pass
        case 2:
            step2()
            pass
        case 3:
            step3()
            pass
        case 4:
            step4()
            pass
        case 5:
            step5()
            pass
        case 0:
            step1()
            step2()
            step3()
            step4()
            pass
        case _:
            print("Invalid choice. exiting .....")


def step1():
    print("step 1 executing .....")
    load_and_plot_image.get_data_from_dataframe("mnist_test.csv")
    load_and_plot_image.plot_image()
    print("step 1  done..... exiting ...")


def step2():
    print("step 2 executing .....")
    change_basis.construct_change_analyze_basis()
    print("step 2  done..... exiting ...")
    pass


def step3():
    print("step 3 executing .....")
    linear_transform.linear_transform_example()
    linear_transform.linear_transformation_image()
    print("step 3  done..... exiting ...")
    pass


def step4():
    print("step 4 executing .....")
    pca_numpy.pca_numpy()
    print("step 4  done..... exiting ...")
    pass


def step5():
    print("step 5 executing .....")

    print("deleting original image folder if exists.....")
    shutil.rmtree("./original_image", ignore_errors=True)

    print("deleting pca image folder if exists .....")
    shutil.rmtree("./pca", ignore_errors=True)

    print("deleting transformed image folder if exists .....")
    shutil.rmtree("./transformed", ignore_errors=True)

    print("step 5  done..... exiting ...")


if __name__ == '__main__':
    """
        This is the main function that is executed when the script is run directly.
        It calls the get_data_from_dataframe function to retrieve the MNIST test data,
        and then calls the plot_image function to display a randomly selected image.
    """
    re_run = ""
    while True:
        try:
            option = command_menu()
            if int(option) in range(0, 6):
                execute_command(int(option))
            # elif int(option) not in range(0, 6):
            #     print("Invalid choice. Please enter a number between 0 and 5. ")
            #     print()
        except ValueError:
            print("no or invalid selection, executing all steps ... please wait... ")
            execute_command(0)
        re_run = input("Would like to run other steps ? Press (y/n) :  ")
        if re_run.lower() != "y":
            break
        pass
