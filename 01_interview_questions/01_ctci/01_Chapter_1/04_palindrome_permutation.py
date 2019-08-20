from string import ascii_lowercase
from collections import Counter

def palindrome_permutation(in_str: str) -> bool:
    '''
    Checks if a string is a permutation of a palindrome
    '''
    counter = {}
    list_str = [char.lower() for char in in_str]
    for char in list_str:
        if char not in ascii_lowercase:
            continue
        else:
            if char not in counter:
                counter[char] = 1
            else:
                counter[char] += 1
    
    num_odd = 0
    for count in counter.values():
        if count % 2 == 1:
            num_odd += 1
        if num_odd > 1:
            return False

    return True


def palindrome_permutation_counter(in_str: str) -> bool:
    '''
    Checks if a string is a permutation of a palindrome
    Uses collections.Counter
    '''
    counter = Counter()
    list_str = [char.lower() for char in in_str]
    for char in list_str:
        if char not in ascii_lowercase:
            continue
        else:
            counter[char] += 1
    
    num_odd = 0
    for count in counter.values():
        if count % 2 == 1:
            num_odd += 1
        if num_odd > 1:
            return False

    return True


def palindrome_permutation_count_ongoing(in_str: str) -> bool:
    '''
    Checks if a string is a permutation of a palindrome
    Uses collections.Counter
    Checks as we iterate through the string, rather than just at the end
    '''
    counter = Counter()
    count_odd = 0
    list_str = [char.lower() for char in in_str]
    for char in list_str:
        if char not in ascii_lowercase:
            continue
        else:
            counter[char] += 1
            if counter[char] % 2 == 1:
                count_odd += 1
            else:
                count_odd -= 1

    return count_odd <= 1


def palindrome_permutation_bit_vector(in_str: str) -> bool:
    '''
    Checks if a string is a permutation of a palindrome
    Uses the binary representation of a single int to store the data 
    '''

    def _create_bit_vector(in_str: str) -> int:
        bit_vector = 0
        for char in in_str:
            char_lower = char.lower()
            if char_lower not in ascii_lowercase:
                continue
            else:
                char_num = ord(char_lower) - ord('a')
                bit_vector = _toggle(bit_vector, char_num)
        
        return bit_vector

    def _toggle(bit_vector: int, index: int) -> int:
        if index < 0:
            return bit_vector

        # if 
        #   index = 4
        # then
        #   bin(1 << index) = 10000
        mask = 1 << index
        # if we have an even count at that index
        if bit_vector & mask == 0:
            # set it to be odd
            bit_vector |= mask
        # odd count            
        else:
            # turn it off
            bit_vector &= ~mask

        return bit_vector

    def _check_exactly_one_bit_set(bit_vector: int) -> bool:
        return bit_vector & (bit_vector - 1) == 0

    bit_vector = _create_bit_vector(in_str)    

    return bit_vector == 0 or _check_exactly_one_bit_set(bit_vector)



if __name__=="__main__":
    # print(palindrome_permutation_count_ongoing('Mr  John    Smith    '))
    # print(palindrome_permutation_count_ongoing('abc'))
    # print(palindrome_permutation_count_ongoing('aba')) 
    # print(palindrome_permutation_count_ongoing('abA'))

    print(palindrome_permutation_bit_vector('Mr  John    Smith    '))
    print(palindrome_permutation_bit_vector('abc'))
    print(palindrome_permutation_bit_vector('aba')) 
    print(palindrome_permutation_bit_vector('abA'))