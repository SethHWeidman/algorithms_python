

def move_tower(height: int,
               from_pole: str,
               to_pole: str,
               with_pole: str) -> None:
    if height > 0:
        move_tower(height - 1, from_pole, with_pole, to_pole)
        print(move_disk(height, from_pole, to_pole))
        move_tower(height - 1, with_pole, to_pole, from_pole)


def move_disk(height: int, 
              from_pole: str, 
              to_pole: str) -> str:
    return "Moved disk {0} from '{1}' to '{2}'".format(
        height, from_pole, to_pole)


if __name__ == '__main__':
    move_tower(3, 'A', 'B', 'C')
