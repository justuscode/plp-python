def process_file():
    try:
        # Ask the user for the input file name
        input_file_name = input("Enter the name of the file to read: ")

        # Open the input file for reading
        with open(input_file_name, "r") as input_file:
            content = input_file.read()

        # Modify the content
        modified_content = content.upper()

        # Ask for the output file name
        output_file_name = input("Enter the name of the new file to write to: ")

        # Open the output file for writing
        with open(output_file_name, "w") as output_file:
            output_file.write(modified_content)

        print(f"Content successfully modified and saved to '{output_file_name}'!")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("Error: You don't have permission to access this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
process_file()
