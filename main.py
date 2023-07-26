import csv
import random


def read_csv_file(file_name):
    # Create an empty dictionary to store the dictionary entries.
    dictionary_entries = []

    # Open the CSV file in read mode.
    with open(file_name, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=":")
        # Iterate over the lines in the CSV file.
        for line in csv_reader:
            # The first item in the line is the word and the second item is the meaning.
            word = line[0]
            meaning = line[1]

            # Add the dictionary entry to the dictionary.
            dictionary_entries.append([word, meaning])

    return dictionary_entries


def random_word(dictionary_entries):
    # Get a random number between 0 and the length of the dictionary entries array.
    random_index = random.randint(0, len(dictionary_entries) - 1)

    # Return the dictionary entry at the random index.
    return dictionary_entries[random_index], random_index


def show_definition(word):
    # Print the definition to the console.
    print("The definition is: " + word[1])


def ask_user_for_guess():
    # Prompt the user to enter a word.
    guess = input("What is the word? ")

    # Return the user input.
    return guess


def main():
    # Read the CSV file and store the dictionary entries in a dictionary.
    dictionary_entries = read_csv_file("./ets2019/test1/RC/part7.txt")
    # Get a random word from the dictionary entries array.
    # max_itr = len(dictionary_entries)
    max_itr = 40
    score = 0
    for itr in range(1, max_itr + 1):
        print("===============================")
        print("Turn ", itr)
        word, idx = random_word(dictionary_entries)

        # Show the definition of the random word to the console.
        show_definition(word)

        # Ask the user to enter the word.
        guess = ask_user_for_guess()

        # Check if the user input is correct.
        if guess == word[0]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct word is ==> " + word[0])
        dictionary_entries.pop(idx)
        itr -= 1
    print(f"Your score: {score} / {max_itr}")


if __name__ == "__main__":
    main()
