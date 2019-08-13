
def is_permuation(str1: str, str2: str) -> bool:
    '''
    Checks if two strings are permutations of each other.
    '''

    if len(str1) != len(str2):
        return False

    char_counts = [0 for _ in range(128)]

    for char1 in str1:
        char_val = ord(char1)
        char_counts[char_val] += 1
        
    for char2 in str2:
         char_val = ord(char2)

         char_counts[char_val] -= 1
         if char_counts[char_val] < 0:
            return False

    return True



if __name__=="__main__":
    S1 = 'abcede'
    S2 = 'abced'
    S3 = 'abcde'
    print(is_permuation(S1, S2))
    print(is_permuation(S2, S3))