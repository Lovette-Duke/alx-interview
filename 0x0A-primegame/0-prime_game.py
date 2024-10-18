#!/usr/bin/python3
"""Prime game."""


def isWinner(x, nums):
    """find the winner of each game session"""
    if x < 1 or not nums:
        return None
    m_wins, b_wins = 0, 0
    # generate primes with a limit of the max number in nums
    n_max = max(nums)
    primes = [True for _ in range(1, n_max + 1, 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n_max + 1, i):
            primes[j - 1] = False
    # filter the number of primes less than n_max in nums for each round
    for _, n_max in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n_max])))
        b_wins += primes_count % 2 == 0
        m_wins += primes_count % 2 == 1
    if m_wins == b_wins:
        return None
    return 'Maria' if m_wins > b_wins else 'Ben'
