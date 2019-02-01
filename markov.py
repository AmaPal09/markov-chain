"""Generate Markov text from text files."""

from random import choice

#file_path = "green-egg.txt"

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here

    return open(file_path).read()


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """
    text_list = text_string.split()
    chains = {(text_list[i], text_list[i+1]):[] for i in range(0,len(text_list) -1)}

    for k in chains.keys():
        for i in range(0,len(text_list) -2):
            if (text_list[i], text_list[i+1]) == k:
                chains[k].append(text_list[i+2])

    
    

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []
    current_key = choice(list(chains.keys()))
    # print(current_key)
    # chosen_word = choice(chains[current_key])
    # current_key = (current_key[1],chosen_word)
    # print(chosen_word, current_key)
    a, b = current_key
    words.append(a)
    words.append(b)
    #for current_key, v in chains.items():
    while True:
        if current_key in chains and len(chains[current_key]) != 0:
    # if (current_key in chains) or (len(chains[current_key]) != 0):
            # a, b = current_key
            # words.append(a)
            # words.append(b)
            # chosen_word = choice(chains[current_key])
            chosen_word = choice(chains[current_key])
            words.append(chosen_word)
            current_key = (current_key[1],chosen_word)
        else: 
            break


    #print(words)


    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
