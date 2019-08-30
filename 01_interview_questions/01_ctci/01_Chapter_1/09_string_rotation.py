
def string_rotation(str1: str, str2: str) -> bool:
    '''
    Return whether str2 is a "rotated" version of str1
    '''

    return len(str1) == len(str2) and str2 in (str1 + str1)


if __name__=="__main__":
    print(string_rotation('waterbottle', 'erbottlewat'))  
    print(string_rotation('waterbottle', 'erbttlewas'))    
    print(string_rotation('waterbottle', 'erbttlewat'))      