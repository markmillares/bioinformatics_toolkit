# Installing Python

# import this


# ===== Variables and some arithmetic ====

from random import sample

a = 927
b = 842

hypotenuse = a**2 + b**2


# ==== Strings and lists ====

a = 78
b = 90
c = 93
d = 102

sample_string = "kPHir4MUCbg5cQOYpCK1LkVrQwKGlKHtf8ppePgGnKzRqlYlpjJjQrYzbx0X8BLRNO4aWoIzX3ZuA6ScaphiophryneLUfimbriatusEeDTV8FbetYyuDRYGIG43eGYzpw9c9oEjapJiGo3Bt8rbxKyfLHM6GUcb0FkWBuJiEuh1OOft."

# print(sample_string[a: b + 1], sample_string[c: d + 1])


# ==== Conditions and loops ====

start = 4814
end = 9390
total = 0

for number in range(start, end + 1):
    if number % 2 != 0:
        total += number

# print(total)

# or

result = sum([num for num in range(start, end + 1) if num % 2 != 0])

# print(result)


# ==== Working with files ====

path = "c:/Users/markl/OneDrive/Documents/Mark Lester/Projects/dna-toolset/rosalind_problems/python_village/"

output_file = []

# with open(path + "input.txt", "r") as f:
#     output_file = [line for index, line in enumerate(f.readlines()) if index % 2 != 0]
#     # print(output_file)

# with open(path + "output.txt", "w") as f:
#     f.write("".join(output_file))


# ==== Dictionaries ====
from collections import Counter

sample_string = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"

sample_list = sample_string.split(" ")

sample_dict = Counter(sample_list)

for key, value in sample_dict.items():
    print(key, value)

# or

words_counter = {}

for word in sample_list:
    if word in words_counter:
        words_counter[word] += 1
    else:
        words_counter[word] = 1

print(words_counter)
