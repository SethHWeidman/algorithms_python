from string import ascii_letters

def urlify(in_str: str, true_length: int) -> str:
    '''
    Performs "URLification"
    Assumes in_str has only letters and spaces
    '''
    orig_str_ind = 0
    final_str_ind = 0
    out_list = []
    while final_str_ind < true_length:
        current_orig_char = in_str[orig_str_ind]
        if current_orig_char in ascii_letters:
            out_list.append(current_orig_char)
            final_str_ind += 1
            orig_str_ind += 1
        else:
            final_str_ind += 1
            out_list.append('%20')
            # keep skipping until you don't see a space
            while current_orig_char not in ascii_letters:
                orig_str_ind += 1
                current_orig_char = in_str[orig_str_ind]
    
    return ''.join(out_list)                


if __name__=="__main__":
    print(urlify('Mr  John    Smith    ', 13))
