def get_book_wordcount(file_text):
    # split return list of words
    wc = file_text.split()
    # count how many elements in list
    return len(wc)

def char_count(file_text):
    # key is character and value is number of times it appears in text
    char_freq = {}
    for char in file_text.lower():
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    
    return char_freq

def sort_key(chars):
    return chars["num"]

def sort_char_freq(characters):
    list_of_dicts = []
    for key, value in characters.items():
        new_dict = {"char": key, "num": value}
        list_of_dicts.append(new_dict)
    
    list_of_dicts.sort(reverse=True, key=sort_key)
    return list_of_dicts
    
