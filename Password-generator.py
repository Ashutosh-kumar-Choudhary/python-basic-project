import random


# Function to generate passwords based on desired lengths
def create_passwords(lengths):
    """Generates a list of passwords with the specified lengths."""
    chars = "abcdefghijklmnopqrstuvwxyz"  # Alphabet set for password generation
    generated_passwords = []  # List to store generated passwords

    for length in lengths:
        temp_password = ""  # Initialize an empty string for each password
        for _ in range(length):
            random_index = random.randrange(len(chars))  # Randomly select an index from the alphabet
            temp_password += chars[random_index]  # Add the selected character to the password

        temp_password = add_number(temp_password)  # Replace some characters with numbers
        temp_password = add_uppercase(temp_password)  # Replace some characters with uppercase letters

        generated_passwords.append(temp_password)  # Add the modified password to the list

    return generated_passwords


# Function to replace some characters with numbers
def add_number(password):
    """Randomly replaces some characters with numbers."""
    for _ in range(random.randrange(1, 3)):
        index_to_replace = random.randrange(len(password) // 2)
        password = password[:index_to_replace] + str(random.randrange(10)) + password[index_to_replace + 1:]
    return password


# Function to replace some characters with uppercase letters
def add_uppercase(password):
    """Randomly replaces some characters with uppercase letters."""
    for _ in range(random.randrange(1, 3)):
        index_to_replace = random.randrange(len(password) // 2, len(password))
        password = password[:index_to_replace] + password[index_to_replace].upper() + password[index_to_replace + 1:]
    return password


# Main function to interact with the user and generate passwords
def main():
    total_passwords = int(input("How many passwords would you like to generate? "))
    print(f"Generating {total_passwords} passwords...")

    length_list = []

    print("Minimum password length is 3.")

    for i in range(total_passwords):
        pw_length = int(input(f"Enter the length of Password #{i + 1}: "))
        if pw_length < 3:
            pw_length = 3
        length_list.append(pw_length)

    generated_pwds = create_passwords(length_list)

    for i in range(total_passwords):
        print(f"Password #{i + 1} = {generated_pwds[i]}")


# Execute the main function
main()