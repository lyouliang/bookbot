def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    # num_words = get_num_words(text)
    # print(f"{num_words} words found in the document")
    # chars_dict = get_chars(text)
    # print(chars_dict)
    print_report(text)

def get_num_words(text):
    words = text.split()
    return len(words)

def print_report(text):
    print("--- Begin report of book/frankenstein.txt ---")
    num_words = get_num_words(text)
    print(f"{num_words} found in the document")
    chars_dict = get_chars(text)
    list_of_dicts = [{'key': key, 'value':value} for key, value in chars_dict.items()]
    list_of_dicts.sort(reverse=True, key=sort_on)
    alpha_list = list(map(get_alpha, list_of_dicts))
    for item in alpha_list:
        if item == None:
            continue
        else:
            print(f"The '{item["key"]}' character was found {item["value"]} times")
    print("--- End report ---")

def sort_on(dict):
    return dict['value']

def get_alpha(dict):
    if dict["key"].isalpha():
        return dict

def get_chars(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_book_text(path):
    with open(path) as f:
     file_contents = f.read()
     return file_contents

main()
