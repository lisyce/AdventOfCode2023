from day07_1 import get_hand_type, HandTypes, by_rank_comparator
from collections import Counter
from functools import cmp_to_key


def joker_hand_type(hand: str) -> HandTypes:
    joker_count = Counter(hand)["J"]
    current_type = get_hand_type(hand)

    if joker_count == 0:
        return current_type

    if current_type >= 5:
        return HandTypes.FIVE_KIND
    elif current_type == HandTypes.THREE_KIND:
        return HandTypes.FOUR_KIND
    elif current_type == HandTypes.TWO_PAIR:
        return HandTypes.FULL_HOUSE if joker_count == 1 else HandTypes.FOUR_KIND
    elif current_type == HandTypes.ONE_PAIR:
        return HandTypes.THREE_KIND
    else:
        return HandTypes.ONE_PAIR


def hand_comparator(x: tuple[str, int], y: tuple[str, int]) -> int:
    # 252322143 too high
    x = x[0]
    y = y[0]
    x_type = joker_hand_type(x)
    y_type = joker_hand_type(y)

    if x_type < y_type:
        return -1
    elif x_type > y_type:
        return 1
    
    # need to compare first card
    card_ranks = "AKQT98765432J"
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