def main():
    path = "books/frankenstein.txt"
    text = book_text(path)
    num_words = get_num_words(text)
    count_letters = get_count_letters(text)
    list_sorted = chars_dict_to_sorted_list(count_letters)
    
    print()
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document")
    print()
    
    for item in list_sorted:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

def book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_count_letters(text):
    char = {}
    for c in text:
        lowered = c.lower()
        if lowered in char:
            char[lowered] += 1
        else:
            char[lowered] = 1
    return char

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()
