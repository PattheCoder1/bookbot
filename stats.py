def get_word_count(book_text):
    words =  book_text.split()
    return len(words)

def get_character_count(book_text):
    characters = {}
    for char in book_text:
        lchar = char.lower()
        if lchar in characters:
            characters[lchar] += 1
        else:
            characters[lchar] = 1
    return characters


def get_sorted_characters(characters):
    sorted_char = []
    for char, count in characters.items():
        if char.isalpha():
            char_dict = {"char": char, "count": count}
            sorted_char.append(char_dict)
    
    def sort_on(char_dict):
        return char_dict["count"]

    sorted_char.sort(reverse=True, key=sort_on)

    return sorted_char

