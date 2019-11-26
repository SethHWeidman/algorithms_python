from string import ascii_lowercase


def is_unique_lowercase(in_string: str) -> bool:
    """
    Checks if the elements in a string are unique by storing the "checker" in an int
    https://wiki.python.org/moin/BitwiseOperators
    https://www.quora.com/Could-someone-explain-how-this-code-dictates-if-the-string-has-all-unique-characters-or-not
    """
    checker = 0
    for el in in_string:
        if el not in ascii_lowercase:
            raise ValueError("Invalid character")
        el_val = ord(el) - ord("a")
        if checker & (1 << el_val) > 0:
            return False
        checker = checker | (1 << el_val)
    return True


def is_unique(in_string: str) -> bool:
    """
    Checks if the elements in a string are unique using a boolean array
    for the number of characters in the string. 
    Assumes there are 128 maximum characters in the string's possible set of characters
    """
    if len(in_string) > 128:
        return False

    char_set = [False for _ in range(128)]
    for char in in_string:
        char_val = ord(char)
        if char_set[char_val]:
            # char already found in string
            return False
        char_set[char_val] = True

    return True


if __name__ == "__main__":
    S1 = "abcede"
    S2 = "abced"
    print(is_unique(S1))
    print(is_unique(S2))
    print(is_unique_lowercase(S1))
    print(is_unique_lowercase(S2))

    S3 = "ABC"
    print(is_unique(S3))
    print(is_unique_lowercase(S3))
