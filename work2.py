"""work2.py"""

import itertools

def generate_words(sequence):
    letters = [char for char in sequence if char.isalpha()]
    unique_words = set()
    
    for length in range(1, len(letters) + 1):
        for comb in itertools.combinations_with_replacement(letters, length):
            for perm in itertools.permutations(comb):
                word = ''.join(perm)
                unique_words.add(word)
    
    sorted_words = sorted(unique_words, key=lambda x: (len(x), x))
    
    return sorted_words


if __name__ == "__main__":
    input_sequence = input("Enter a sequence: ")
    words = generate_words(input_sequence)

    print(len(words))
    for word in words:
        print(word)
