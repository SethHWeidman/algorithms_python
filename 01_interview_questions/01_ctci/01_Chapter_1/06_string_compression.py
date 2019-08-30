def string_compression(in_str: str) -> bool:
    '''
    aaabbbbcccd -> a3b4c3d1
    '''
    out_list = []
    num_chars = 1
    i = 0
    while i < len(in_str):
        if i == len(in_str) - 1:
            out_list.append(in_str[i])
            out_list.append(str(num_chars))            
        elif in_str[i] != in_str[i+1]:
            out_list.append(in_str[i])
            out_list.append(str(num_chars))
            num_chars = 1
        else:
            num_chars += 1
        i += 1

    out_str = ''.join(out_list) 
    
    # handle the last element of the list
    return out_str if len(out_str) < len(in_str) else in_str


if __name__=="__main__":
    print(string_compression('aaabbbbcccdds'))
    print(string_compression('abced'))