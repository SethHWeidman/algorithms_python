
def urlify(in_str: str, true_length: int) -> str:

    num_spaces = 0
    for char in in_str:
        if char == ' ':
            num_spaces += 1

    

# if __name__=="__main__":
#     S1 = 'abcede'
#     S2 = 'abced'
#     S3 = 'abcde'
#     print(is_permuation(S1, S2))
#     print(is_permuation(S2, S3))