def read_file(file_path):
    """
    Reads the content of a file and prints it line by line.
    Handles the case where the file does not exist.
    
    :param file_path: Path to the file to be read.
    """
    try:
        with open(file_path, 'r') as file:
            print(f"Reading file: {file_path}\n")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except IOError as e:
        print(f"Error: An I/O error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Specify the file path
    file_path = input("Enter the path of the file to read: ")
    
    # Attempt to read the file
    read_file(file_path)
