# with open("books/frankenstein.txt", "r") as file:
#     contents = file.read()
#     print(contents)

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #count_words = get_word_count(path)
    count_words = get_word_count(text)
    #count_characters = get_character_count(text)
    chars_dict = get_chars_dict(text)
    print(text)
    print(count_words)
    #print(count_characters)
    print(chars_dict)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict) 
    # This line calls the function chars_dict_to_sorted_list, passing chars_dict as an argument. 
    # It takes a dictionary of characters and their counts, converts it to a list of dictionaries,
    # sorts it, and assigns the sorted list to chars_sorted_list.
    print(f"--- Begin report of {book_path} ---")
    print(f"{count_words} words found in the document")
    print()
# These lines print a formatted report header.

# book_path is the path of the book (or file) that was processed.
# num_words is the number of words in the document.
# The print() function outputs the string to the console. 
# The f before the string allows embedding variables inside {} within the string.



    for item in chars_sorted_list: 
    # for item in chars_sorted_list:: Loops through each item (a dictionary) in the sorted list.
    # Each item looks like {"char": some_character, "num": number_of_occurrences}.
        if not item["char"].isalpha():
        # if not item["char"].isalpha():: This checks if the character (item["char"]) is not alphabetic.
        # isalpha() returns True if the character is a letter, and False otherwise (for example, spaces, punctuation).
            continue
            # continue: If the character is not alphabetic, skip this iteration of the loop and go to the next one.
        print(f"The '{item['char']}' character was found {item['num']} times")
        # print(...): If the character is alphabetic, it prints a report line indicating how many times the character appeared in the text.
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

# def get_word_count(path):
#     try:
#         with open(path, 'r', encoding="utf-8") as f:
#             text = f.read()
#             words = text.split()
#             return len(words)
#     except IOError:
#         return "File not found."
#     except Exception as e:
#         return f"An error occured: {e}"

def get_word_count(text):
    words = text.split()
    return len(words)

#Add a new function to your script that takes the text from the book as a string, 
#and returns the number of times each character appears in the string. 
#Convert any character to lowercase, we don't want duplicates.

# def get_character_count(text):
#     text = text.lower() # Convert all characters to lowercase
#     character_count ={}
#     for char in text: # Count occurrences of each character
#         if char in character_count:
#             character_count[char] += 1 # add 1 for each time the character shows up.
#         else:
#             character_count[char] = 1 # keep the count at 1 if the character shows up once.
        
#     return character_count

# # Function to count character occurrences in a string
# def count_characters_in_text(text):
#     text = text.lower()  # Convert all characters to lowercase
#     character_count = Counter(text)  # Count occurrences of each character
#     return dict(character_count)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

# Convert your dictionary of characters into a list of dictionaries and then use the 
# .sort() method to sort by the number of occurrences. Here's an example:
# You can use a string's .isalpha() method to check if a string only contains characters from the alphabet.


# # A function that takes a dictionary and returns the value of the "num" key
# # This is how the `.sort()` method knows how to sort the list of dictionaries
# def sort_on(dict):
#     return dict["num"]

# vehicles = [
#     {"name": "car", "num": 7},
#     {"name": "plane", "num": 10},
#     {"name": "boat", "num": 2}
# ]
# vehicles.sort(reverse=True, key=sort_on)
# print(vehicles)
# # [{'name': 'plane', 'num': 10}, {'name': 'car', 'num': 7}, {'name': 'boat', 'num': 2}]


def sort_on(dict):
    return dict['num']
# This is a helper function used to define the sorting criteria for sorting dictionaries. It takes a
# dictionary dict as input and returns the value associated with the key "num". This function is used as
# the key in the sorting function to sort based on the number of occurrences of each character.


def chars_dict_to_sorted_list(num_chars_dict): # This function converts the num_chars_dict (a dictionary with characters as keys and their counts as values) into a sorted list of dictionaries.
    sorted_list = [] # Initializes an empty list to store the dictionaries.
    for ch in num_chars_dict:  # Loops through each character ch in the dictionary.
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
        # Creates a dictionary with the character and its count, and appends it to sorted_list. 
        # For example, if the dictionary entry is {'a': 10}, this will append {"char": 'a', "num": 10} to the list.
    sorted_list.sort(reverse=True, key=sort_on)
    # Sorts the list in descending order based on the value of "num" (i.e., the count of occurrences) using the helper function sort_on. 
    #  The reverse=True flag ensures that characters with the highest count come first.
    return sorted_list

# Summary of Process
# The script counts the number of words in a text.
# It then counts how often each character appears and sorts this data into a list.
# The sorted data is used to generate a report, which excludes non-alphabetic characters, showing how many times each letter appears in the text.

main()