from collections import Counter
from enum import IntEnum, auto
from functools import cmp_to_key

class HandTypes(IntEnum):
    HIGH_CARD = auto()
    ONE_PAIR = auto()
    TWO_PAIR = auto()
    THREE_KIND = auto()
    FULL_HOUSE = auto()
    FOUR_KIND = auto()
    FIVE_KIND = auto()


def get_hand_type(hand: str) -> HandTypes:
    counts = Counter(hand)
    most_common = counts.most_common(2)
    most_common_count = most_common[0][1]
    second_most_common_count = most_common[1][1] if most_common_count < 5 else 5

    if most_common_count == 5:
        return HandTypes.FIVE_KIND
    elif most_common_count == 4:
        return HandTypes.FOUR_KIND
    elif most_common_count == 3:
        # full house or 3 kind?
        if second_most_common_count == 2:
            return HandTypes.FULL_HOUSE
        return HandTypes.THREE_KIND
    elif most_common_count == 2:
        # two or one pair?
        if most_common_count == second_most_common_count:
            return HandTypes.TWO_PAIR
        return HandTypes.ONE_PAIR
    
    return HandTypes.HIGH_CARD


def by_rank_comparator(x: str, y: str, card_ranks: str) -> int:
    first_diff_idx = 0
    while x[first_diff_idx] == y[first_diff_idx]:
        first_diff_idx += 1

    for char in card_ranks:
        if char == x[first_diff_idx]:
            return 1
        elif char == y[first_diff_idx]:
            return -1
        
    return 0


def hand_comparator(x: tuple[str, int], y: tuple[str, int]) -> int:
    x = x[0]
    y = y[0]
    x_type = get_hand_type(x)
    y_type = get_hand_type(y)

    if x_type < y_type:
        return -1
    elif x_type > y_type:
        return 1
    
    # need to compare first card
    card_ranks = "AKQJT98765432"
    return by_rank_comparator(x, y, card_ranks)
    

if __name__ == "__main__":
    hand_bids = []

    with open("input.txt") as f:
        for line in f.readlines():
            line = line.split(" ")
            hand_bids.append((line[0], int(line[1])))
    
    hand_bids = sorted(hand_bids, key=cmp_to_key(hand_comparator))
    
    total = 0
    for idx, (hand, bid) in enumerate(hand_bids):
        total += (idx + 1) * bid
    
    print(total)
