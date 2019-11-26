def string_one_away(str1: str, str2: str) -> bool:
    """
    Checks if strings are "one edit" away from one another
    """

    def string_one_edit_away(str1: str, str2: str):
        num_diff = 0
        for char1, char2 in zip(str1, str2):
            if char1 != char2:
                num_diff += 1
        return num_diff == 1

    def string_one_delete_away(short_str: str, long_str: str):
        i = 0
        j = 0
        found_diffs = 0
        while i < len(short_str):
            if short_str[i] != long_str[j]:
                found_diffs += 1
                j += 1
            else:
                i += 1
                j += 1

            if found_diffs > 1:
                return False

        return True

    if len(str1) == len(str2):
        return string_one_edit_away(str1, str2)
    elif len(str1) == len(str2) - 1:  # str1 is shorter
        return string_one_delete_away(str1, str2)
    elif len(str2) == len(str1) - 1:  # str2 is shorter
        return string_one_delete_away(str2, str1)
    else:
        return False


def string_one_away_2(str1: str, str2: str) -> bool:
    """
    Checks if strings are "one edit" away from one another
    More concise, clever than prior method, but less understandable
    """
    if abs(len(str1) - len(str2)) > 1:
        return False

    # tie goes to str1
    short_str = str2 if len(str2) < len(str1) else str1
    long_str = str1 if len(str2) < len(str1) else str2

    short_ind = 0
    long_ind = 0
    found_difference = False
    while short_ind < len(short_str) and long_ind < len(long_str):
        if short_str[short_ind] != long_str[long_ind]:
            if found_difference:
                return False
            found_difference = True

            # in particular, "don't" move pointer for edit
            if len(short_str) == len(long_str):
                short_ind += 1
        else:
            short_ind += 1

        long_ind += 1

    return True


if __name__ == "__main__":
    # print(string_one_away('pale', 'pae')) # True
    # print(string_one_away('pale', 'pare')) # True
    # print(string_one_away('pale', 'pair')) # False
    # print(string_one_away('pale', 'pail')) # False

    print(string_one_away_2("pale", "pae"))  # True
    print(string_one_away_2("pale", "pare"))  # True
    print(string_one_away_2("pale", "pair"))  # False
    print(string_one_away_2("pale", "pail"))  # False
