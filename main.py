def count_words(text):
    words = text.split()
    count = 0

    for word in words:
        count += 1
    
    return count

def count_chars(text):
    lower_case_text = text.lower()
    count_dict = {"a": 1}

    for char in lower_case_text:
        if char in count_dict and char.isalpha() == True:
            count_dict[char] += 1
        if char not in count_dict and char.isalpha() == True:
            count_dict[char] = 1

    return count_dict


def get_book_text(path):
    with open(path) as f:
        text = f.read()
    
    return text

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)

    count_words_in_text = count_words(text)
    count_chars_in_text = count_chars(text)

    # sort the new directory on value 
    # print one entry per line

    list_of_dicts = [{key: value} for key, value in count_chars_in_text.items()]
    sorted_data = sorted(list_of_dicts, key=lambda x: list(x.values())[0], reverse=True)

    print(f"-----{path} has {count_words_in_text} words-----")
    print("Most common characters in the text:")
    print(sorted_data)

main()