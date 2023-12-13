import this
from collections import Counter


def calc_hypotenuse(a, b):
    return a ** 2 + b ** 2


print(calc_hypotenuse(880, 874))


def slice_list(s, a, b, c, d):
    return " ".join([s[a:b+1], s[c: d+1]])

list = "xJLVTwNSHOIFufhbhZRLxCakQuqIrBCa1Pb3FKiLe8LvCkRmJR8Pf11ELIeJSxddPhormictopusn8VMlk80Dn3w4BXhceOGQJFk1bKnvdorsaliss1pcK5kSNiThiZ6lupjgPCxdFiCRgFETwcoAH3ge3P2R3MQKrPZZRt.."
print(slice_list(list, 64, 75, 105, 112))


def loop(a, b):
    sum = 0
    for i in range(a, b + 1):
        if i % 2 != 0:
            sum += i
    return sum


print(loop(4243, 8788))


def dictionaries(s):
    return Counter(s.split(" "))


string = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"
dict_words = dictionaries(string)
print(dict_words)

for key, value in dict_words.items():
    print(key, value)