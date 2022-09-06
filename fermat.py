import math
import random


def prime_test(N, k):
    # This is main function, that is connected to the Test button. You don't need to touch it.
    return fermat(N, k), miller_rabin(N, k)


def mod_exp(x, y, N):
    if y == 0:
        return 1
    z = mod_exp(x, math.floor(y / 2), N)
    if y % 2 == 0:
        return pow(z, 2) % N
    else:
        return (x * pow(z, 2)) % N


def fprobability(k):
    return 1 - pow(1 / 2, k)  # 1-(1/2)^k


def mprobability(k):
    # You will need to implement this function and change the return value.   
    return 1 - pow(4, -k)  # 1-4^-k


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


def miller_rabin(N, k):
    # TODO: are we okay with our list having multiple of the same values?
    # because if N<= k then we have a problem and it never completes the list
    # maybe create a separate case for that? so if k >= N then make the list be N-1 in length.
    # Complexity O(klog^3(n))
    list_ofa = set()
    while len(list_ofa) < k:
        list_ofa.add(random.randint(1, N - 1))

    for a in list_ofa:
        # I think this is where we call mod_exp(x,y,n)
        if mod_exp(a, N - 1, N) != 1:
            return "composite"
        # else:
    #         repeat s − 1 times: # not sure what s is yet
    #         x ← x2 mod n
    #         if x = n − 1 then
    #             continue WitnessLoop
    #     return “composite”
    return 'prime'
