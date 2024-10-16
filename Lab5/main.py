def encrypt(some_string, stride):

    scrambled_string = ""

    for starting_index in range(stride):
        scrambled_string += some_string[starting_index::stride]

    return scrambled_string

def decrypt(scrambled_string, stride):
    chunk_size = len(scrambled_string) // stride
    remainder = len(scrambled_string) % stride

    original_string = ""

    for starting_index in range(chunk_size):
        chunk_number = 0
        current_index = starting_index
        while current_index < len(scrambled_string):
            original_string += scrambled_string[current_index]
            current_index += chunk_size
            if chunk_number < remainder:
                current_index += 1
            chunk_number += 1

    current_index = chunk_size
    for character in range(remainder):
        original_string += encrypted_string[current_index]
        current_index += chunk_size + 1

    return original_string

message = "salted popcorns!"

for stride in range(1, len(message)):
    encrypted_string = encrypt(message, stride)
    print(encrypted_string)
    print(decrypt(encrypted_string, stride))
