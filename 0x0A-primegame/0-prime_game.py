#!/usr/bin/python3
'''prime game'''

def isWinner(x, nums):
    """"""    """
    Determines the winner of a prime game played by two players, Maria and Ben.

    Args:
        x (int): The number of rounds played in the game.
        nums (list): A list of consecutive integers starting from 1 up to and including n.

    Returns:
        str: The name of the player who won the most rounds. If the winner cannot be determined, returns None.
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    Ben = 0
    Maria = 0

    a = [1 for x in range(sorted(nums)[-1] + 1)]

    a[0], a[1] = 0, 0
    for i in range(2, len(a)):
        rm_multiples(a, i)

    for i in nums:
        if sum(a[0:i + 1]) % 2 == 0:
            Ben += 1
        else:
            Maria += 1

    if Ben > Maria:
        return "Ben"
    elif Maria > Ben:
        return "Maria"
    else:
        return None


def rm_multiples(lst, x):
    """removes multiples of x from lst"""
    for i in range(2, len(lst)):
        try:
            lst[i * x] == 0
        except (ValueError, IndexError):
            break