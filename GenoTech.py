# ============================================== Case Study 03 =========================================================
# ========================================= A DNA Sequence Analyser ====================================================
# *********************************************** E. Thompson **********************************************************

def dna_check(sequence=""):
    # Function to check a sequence contains only the letters A, T, C, G and is not blank.
    sequence_check = sequence.replace("A", "").replace("T", "").replace("C", "").replace("G", "")
    if len(sequence_check) > 0 or len(sequence) == 0:
        print("Error: Invalid sequence. DNA sequences must only consist of the letters 'A', 'T', 'C' and 'G'.")
        return False
    else:
        return True


def split_sequence(sequence):
    # Function to split the user's sequence
    while True:
        user_split = input("Please enter the marker used to split the sequence : ").upper()
        if dna_check(user_split):
            break
    new_sequence = sequence.split(user_split)
    print(new_sequence)


def find_marker(sequence):
    # Function to find a marker in a sequence:
    while True:
        user_marker = input("Please enter the marker you wish to look for : ").upper()
        if dna_check(user_marker):
            break
    if user_marker in sequence:
        print("Marker found")
    else:
        print("Marker not found")


def find_traits(sequence):
    # Function to find known markers for traits in a sequence:
    traits = {
        "ATTG": "blue eyes",
        "GAGC": "large feet",
        "CGGG": "black hair",
        "TAGC": "webbed fingers"
    }
    for marker, trait in traits.items():
        if marker in sequence:
            print(f"The marker {marker} for the trait of {trait} was found.")


def replace_dna(sequence):
    # Function to replace a set of nucleotides in the sequence with another:
    while True:
        user_replace = input("Please enter the nucleotide sequence you wish to replace : ").upper()
        if not dna_check(user_replace):
            continue
        user_replace_with = input(f"Please enter the replacement sequence: ").upper()
        if dna_check(user_replace_with):
            break
    new_sequence = sequence.replace(user_replace, user_replace_with)
    return new_sequence


# Ask the user for their DNA sequence string and check it is valid
while True:
    user_sequence = input("Please enter a DNA sequence : ")
    DNA_sequence = user_sequence.upper()
    if dna_check(DNA_sequence):
        break

# Asks the user which operation they would like to perform:
while True:
    print("""Please select from the following options:
1.  Split the sequence
2.  Look for a marker
3.  Predict traits
4.  Replace a nucleotide pattern
5.  Exit
          """)

    user_choice = input("Please enter your choice (1-5):")

    if user_choice == "5":
        break

    elif user_choice == "1":
        split_sequence(DNA_sequence)

    elif user_choice == "2":
        find_marker(DNA_sequence)

    elif user_choice == "3":
        find_traits(DNA_sequence)

    elif user_choice == "4":
        DNA_sequence = replace_dna(DNA_sequence)
        print(DNA_sequence)

    else:
        print("Error: Please enter a number between 1 and 5.")
