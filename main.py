import string


def read_content(src):
    with open(src) as f:
        file_contents = f.read()
    
    return file_contents


def count_words(file_contents):   
    return(len(file_contents.split()))


def count_characters(file_contents):
    char_dict = {}
    alphabet = list(string.ascii_lowercase)
    [char_dict.update({x: 0}) for x in alphabet]
    content_lower = file_contents.lower()

    for char in content_lower:
        if char in alphabet:
            char_dict[char] = char_dict[char] + 1
    
    return char_dict


def create_report(src, word_count, chars_count):
    report = f"--- Begin report of {src} ---\n" \
            f"{word_count} words found in the document\n\n"
    
    for key in chars_count:
        report += f"The '{key}' character was found {chars_count[key]} times\n"
    
    report += "--- End report ---"

    return report


def main():
    src = "books/frankenstein.txt"

    file_contents = read_content(src)
    word_count = count_words(file_contents)
    chars_count = count_characters(file_contents)
    report_created = create_report(src, word_count, chars_count)

    print(file_contents)
    print(word_count)
    print(chars_count)
    print(report_created)


main()
