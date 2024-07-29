def categorize_names(file_path):
    """Reads a file and categorizes names into positive and negative lists."""
    positive_names = []
    negative_names = []

    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Remove whitespace and split the line into name and label
                line = line.strip()
                if line:  # Ensure the line is not empty
                    name, label = line.split(':')

                    # Add the name to the appropriate list based on the label
                    if label.strip().lower() == 'positive':
                        positive_names.append(name.strip())
                    elif label.strip().lower() == 'negative':
                        negative_names.append(name.strip())
                    else:
                        print(f"Unrecognized label '{label}' for name '{name}'.")

    except FileNotFoundError:
        print(f"The file at '{file_path}' was not found.")
    except IOError:
        print(f"An error occurred while reading the file at '{file_path}'.")
    except ValueError:
        print("Each line should contain a name and a label separated by a colon.")

    return positive_names, negative_names

def main():
    # Specify the path to the text file
    file_path = 'sentiment.txt'  # Change this to the path of your file
    
    # Categorize names from the file
    positive_names, negative_names = categorize_names(file_path)
    
    # write in matching txt file
    with open("matching.txt", "a") as file:
    
        file.write(f"Andy - " + "\n")
        file.write(positive_names[0]+ "\n")
        file.write(positive_names[1]+ "\n")
        file.write(positive_names[2]+ "\n\n")
        file.write(f"Angela - "+ "\n")
        file.write(positive_names[3]+ "\n")
        file.write(positive_names[4]+ "\n")
        file.write(positive_names[5]+ "\n\n")
        file.write(f"Jim - "+ "\n" )
        file.write(negative_names[0]+ "\n")
        file.write(negative_names[1]+ "\n")
        file.write(negative_names[2]+ "\n\n")
        file.write(f"Stanely - "+ "\n" )
        file.write(negative_names[3]+ "\n")
        file.write(negative_names[4]+ "\n")
        file.write(negative_names[5]+ "\n")
  


if __name__ == "__main__":
    main()