alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

index_of_letter = int(input("Enter an index number for a letter of the alphabet"))

print(alphabet[index_of_letter])

print(alphabet[::2])

print(alphabet[::-2])

name = input("Enter your first and last name")
index_of_space = name.find(" ") # substring to find

first_name = name[:index_of_space] # if you don't specify a start, you get 0
last_name = name[index_of_space+1:] # if you don't specify, you get the last index

print(first_name)
print(last_name)

sentence = input("Enter a sentence")
word_to_find = input("Enter a word to find")

index_of_word_to_find = sentence.find(word_to_find)

print(f"Found the word at index {index_of_word_to_find}")

print(f"up to the word: {sentence[:index_of_word_to_find]}")
print(f'after the word: {sentence[index_of_word_to_find+len(word_to_find):]}')

index_of_space = sentence.find(" ")
start_index = 0

while index_of_space != -1:
    print(sentence[start_index:index_of_space])
    start_index = index_of_space + 1
    index_of_space = sentence.find(" ", start_index)

print(sentence[start_index:])