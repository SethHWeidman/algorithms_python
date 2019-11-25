def int_to_base_str(n: int, base: int) -> str:
    convert_string = "0123456789ABCDEF"
    print("Entering function")
    print(n, base)
    if n < base:
        return convert_string[n]
    else:
        print("Entering else statement")
        print(n // base, base, convert_string[n % base])
        return int_to_base_str(n // base, base) + convert_string[n % base]


if __name__ == "__main__":
    print(int_to_base_str(11, 3))
