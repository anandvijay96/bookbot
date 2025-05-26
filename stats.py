def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def count_book_text_count(filepath):
    book_text = get_book_text(filepath)
    word_count = len(book_text.split())
    return word_count

def char_count_dict(filepath):
    book_text = get_book_text(filepath)
    word_count = book_text.split()
    char_count = {}
    for word in word_count:
        for char in word:
            char = char.lower()
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def sort_on(char_list):
    return char_list["count"]

def sort_char_list_count(char_list):
    sorted_list = []
    for char in char_list:
        sorted_list.append({"char": char, "count": char_list[char]})
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list