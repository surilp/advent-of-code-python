import functools
import itertools
from functools import cache
from utils.utils import file_to_collection


def get_player1_dice():
    current = -3
    while True:
        current += 6
        yield current


def get_player2_dice():
    current = 0
    while True:
        current += 6
        yield current


def play_game_part1(input_file):
    p1_position, p2_position = extract_player_positions(input_file)
    p1_score = 0
    p2_score = 0
    p1_dice_iterator = iter(get_player1_dice())
    p2_dice_iterator = iter(get_player2_dice())
    die_roll = 0
    while True:
        p1_position, p1_score = location_update_and_score(p1_position, player_dice_result(next(p1_dice_iterator)),
                                                          p1_score)
        die_roll += 3
        if p1_score >= 1000:
            break
        p2_position, p2_score = location_update_and_score(p2_position, player_dice_result(next(p2_dice_iterator)),
                                                          p2_score)
        die_roll += 3
        if p2_score >= 1000:
            break
    return (p2_score if p1_score > p2_score else p1_score) * die_roll


def extract_player_positions(input_file):
    input_data = file_to_collection(input_file)
    p1_position = int(input_data[0][-1])
    p2_position = int(input_data[1][-1])
    return p1_position, p2_position


def player_dice_result(dice_result):
    total = (((dice_result - 2) + dice_result) * (3)) // 2
    return total


def location_update_and_score(current_location, dice_sum, current_sum):
    updated_location = (current_location + dice_sum) % 10
    updated_location = updated_location if updated_location != 0 else 10
    return updated_location, updated_location + current_sum


def play_game_part2(input_file):
    p1_position, p2_position = extract_player_positions(input_file)
    return play_game_part2_helper(p1_position, 0, p2_position, 0, True)


@cache
def play_game_part2_helper(player1_position, player1_score, player2_position, player2_score, is_player1_turn):
    p1_wins = 0
    p2_wins = 0
    for roll_result in itertools.product((1, 2, 3), (1, 2, 3), (1, 2, 3)):
        if is_player1_turn:
            new_position, new_score = location_update_and_score(player1_position, sum(roll_result),
                                                                player1_score)
            if new_score >= 21:
                p1_wins += 1
            else:
                new_p1_wins, new_p2_wins = play_game_part2_helper(new_position, new_score, player2_position,
                                                                  player2_score,
                                                                  False)
                p1_wins += new_p1_wins
                p2_wins += new_p2_wins
        else:
            new_position, new_score = location_update_and_score(player2_position, sum(roll_result),
                                                                player2_score)

            if new_score >= 21:
                p2_wins += 1
            else:
                new_p1_wins, new_p2_wins = play_game_part2_helper(player1_position, player1_score, new_position,
                                                                  new_score,
                                                                  True)
                p1_wins += new_p1_wins
                p2_wins += new_p2_wins

    return p1_wins, p2_wins
