from typing import List


def min_coins_memo(
    coin_value_list: List[int], change: int, known_results: List[int] = None
) -> int:

    if not known_results:
        known_results = [0] * (change + 1)

    min_coins = change
    if change in coin_value_list:
        known_results[change] = True
        return 1

    elif known_results[change] > 0:
        return known_results[change]

    else:
        for i in [c for c in coin_value_list if c <= change]:
            num_coins = 1 + min_coins_dp(coin_value_list, change - i, known_results)
            if num_coins < min_coins:
                min_coins = num_coins
                known_results[change] = min_coins

    return min_coins


def min_coins_dp(coin_value_list: List[int], change: int, min_coins: List[int]) -> int:

    for cents in range(change + 1):
        coin_count = cents
        for j in [c for c in coin_value_list if c <= cents]:
            if min_coins[cents - j] + 1 < coin_count:
                coin_count = min_coins[cents - j] + 1
        min_coins[cents] = coin_count

    return min_coins[change]


if __name__ == "__main__":
    print(min_coins_memo([1, 5, 10, 25], 63))
    print(min_coins_dp([1, 5, 10, 25], 63, [0] * 64))
