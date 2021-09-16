# initialize starter parameters
whitespaces = {" ", "\n", "\t"}
filename = "test.txt"


def is_whitespace(string: str) -> bool:
    """
    :param string: any string that should be checked
    :return: True if string is a whitespace else False
    """
    
    return string in whitespaces


def parse_string(text_to_parse: str) -> list:
    """
    :param text_to_parse: text that will be split by whitespaces
    :return: list of strings from text_to_parse split by whitespaces without empty strings
    """
    
    result = []  # result list
    current_word = []  # separate words split by whitespaces
    # current_word is a list, not a string because string is immutable
    # and will reallocate memory on each symbol appended
    
    # for each symbol in text
    for char in text_to_parse:
        if is_whitespace(char):
            # if char is a whitespace there are 2 cases for previous symbol
            # it was not a whitespace, then current_word is not empty and it needs to be saved and cleared
            # it was a whitespace, then current_word is empty and char is skipped
            if current_word:
                # save current_word and clear it (join is used to correctly cast list to string)
                result.append("".join(current_word))
                current_word.clear()
        else:
            # if char is not a whitespace store it in current_word
            current_word.append(char)
    
    return result


def main():
    with open(filename) as file:
        # read all text from file and pass it to parse function
        result = parse_string(file.read())
    
    print(result)


if __name__ == '__main__':
    main()
