#!/usr/bin/python3


def split_by_bit(bit, words):
    zeros = [word for word in words if word[bit] == "0"]
    ones = [word for word in words if word[bit] == "1"]
    return (zeros, ones)


def bin2int(word):
    i = 0
    for b in word:
        i *= 2
        if b == "1":
            i += 1
    return i


with open('3.txt') as input:
    lines = [line.rstrip() for line in input.readlines()]
    bits = len(lines[0])

    oxy = lines
    bit = 0
    while len(oxy) > 1:
        (zeros, ones) = split_by_bit(bit, oxy)
        bit += 1
        if len(zeros) > len(ones):
            oxy = zeros
        else:
            oxy = ones
    
    co2 = lines
    bit = 0
    while len(co2) > 1:
        (zeros, ones) = split_by_bit(bit, co2)
        bit += 1
        if len(zeros) <= len(ones):
            co2 = zeros
        else:
            co2 = ones

    oxy = bin2int(oxy[0])
    co2 = bin2int(co2[0])
    print(oxy * co2)
