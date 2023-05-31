#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """
    Tell Winner
    """

    name = {'Maria': 0, 'Ben': 0}
    for i in range(x):
        if (number_of_prime(nums[i]) % 2 == 0):
            name['Ben'] += 1
        else:
            name['Maria'] += 1
    if (name['Ben'] > name['Maria']):
        return 'Ben'
    elif (name['Ben'] < name['Maria']):
        return 'Maria'
    else:
        return None


def number_of_prime(number):
    """
    Calculate number of prime number using
    method Sieve of Eratosthenes
    :parm:number lastnumber of prime from 1
    :return: number of prime number form 1 up to number included
    """
    if number <= 0:
        return 0
    prime = [True for i in range(number + 1)]
    p = 2
    while p * p <= number:
        if prime[p]:
            for i in range(p * 2, number + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    count = 0
    for i in range(number + 1):
        if prime[i]:
            count += 1
    return count
