import math
import random

# Time complexity: O(1)
# Space Complexity:
def prime_test(N, k):
    # This is main function, that is connected to the Test button. You don't need to touch it.
    return fermat(N, k), miller_rabin(N, k)

# Time complexity: O(1)
# algorithm will stop after at most n recursive calls.
# each call it multiplies n-bit numbers, for a total running time of O(n^3)
# Space Complexity:

def mod_exp(x, y, N):
    if y == 0:
        return 1
    z = mod_exp(x, math.floor(y / 2), N) # recursive call.
    if y % 2 == 0:
        return pow(z, 2) % N
    else:
        return (x * pow(z, 2)) % N

# Time complexity: O(1)
# Space Complexity:
def fprobability(k):
    return 1 - 1/pow(2, k)  # 1-1/(2)^k

# Time complexity: O(1)
# Space Complexity:
def mprobability(k):
    return 1 - pow(4, -k)  # 1-1/(4^k)

# Time complexity:
# Space Complexity:
def fermat(N, k):
    # TODO: are we okay with our list having multiple of the same values?
    # because if N<= k then we have a problem and it never completes the list
    # maybe create a separate case for that? so if k >= N then make the list be N-1 in length.
    list_ofa = set()
    while len(list_ofa) < k:
        list_ofa.add(random.randint(1, N - 1))

    for a in list_ofa:
        # I think this is where we call mod_exp(x,y,n)
        if mod_exp(a, N - 1, N) != 1:
            return "composite"
    return 'prime'

# Time complexity:
# Space Complexity:
def miller_rabin(N, k):
    # TODO: are we okay with our list having multiple of the same values?
    # because if N<= k then we have a problem and it never completes the list
    # maybe create a separate case for that? so if k >= N then make the list be N-1 in length.
    # Complexity O(klog^3(n))

    if k >= N:
        length_of_list = N-1
    else:
        length_of_list = k

    list_ofa = set()
    while len(list_ofa) < length_of_list:
        list_ofa.add(random.randint(1, N - 1))

    for a in list_ofa:
        if mod_exp(a, N - 1, N) != 1:
            return "composite"
        else:
            new_exp = N-1
            while new_exp % 2 == 0:
                # we want to check first if it is equal to -1 aka N-1. If so return, because we found a prime
                if mod_exp(a, new_exp/2, N) == N-1:
                    break
                if mod_exp(a, new_exp / 2, N) != 1:
                    # if it is not equal to 1
                    return "composite"
                else:
                    # decrement new_exp
                    new_exp = new_exp/2
    return 'prime'
