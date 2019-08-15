from string import ascii_lowercase

def palindrome_permutation(in_str: str) -> bool:
    '''
    Assumes in_str has only letters and spaces
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


if __name__=="__main__":
    print(palindrome_permutation('Mr  John    Smith    '))
    print(palindrome_permutation('abc'))
    print(palindrome_permutation('aba')) 
    print(palindrome_permutation('abA'))        