import os
import glob

all_files = []


def display_menu():
    print(
        "---------------------------------------------------------------------------------"
    )
    print(
        "This program will delete all files with a given similarity (or copies) in the name given from a valid folder path. It will also check sub directories."
    )
    print(
        "---------------------------------------------------------------------------------"
    )


def get_input():
    potential_path = input("Please enter the path you'd like me to search through: ")

    similar_keyword = input(
        "Please enter a similarity between the files you'd like me to delete. Examples: '- Copy' or '-video-paired': "
    )
    file_extension = input(
        "Please enter the file extension? such as 'txt', 'mov', etc: "
    )
    yes_or_no = input("Whould you like me to check sub folders? Y or N?: ")
    should_check_subdirs = yes_or_no.lower() == "y"

    # is_checking_subdirectories = True if yes_or_no == "y" else False
    # string, string, string
    return (potential_path, similar_keyword, file_extension, should_check_subdirs)


def search_for_files(path_name, file_extension, should_check_inner_folders):

    files = glob.glob(
        path_name + f"/**/*.{file_extension}", recursive=should_check_inner_folders
    )
    return files


if __name__ == "__main__":

    while True:
        found_files = []
        display_menu()
        (path, keyword, file_extension, should_check_subdirs) = get_input()
        all_files = search_for_files(path, file_extension, should_check_subdirs)
        for file in all_files:
            if keyword in file:
                found_files.append(file)

        print(f"Found {len(found_files)} files(s) containing {keyword}. ")
        should_delete = input(
            "Would you like me to delete them? Y for yes or N for no: "
        )
        yes_or_no = should_delete.lower()
        should_delete = yes_or_no == "y"
        if should_delete:
            for file in found_files:
                print(f"Deleting {file}...check trash")
                os.remove(file)
        user_choice = input("Should I run this again? Y for yes or N for no: ")
        if user_choice.lower() == "y":
            continue
        else:
            break
