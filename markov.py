"""Generate Markov text from text files."""
import sys
from random import choice

#file_path = "green-egg.txt"

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    
    #open the input file provided and read it into 1 string
    return open(file_path).read()


def make_chains(text_string,n_gram):
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

    #create a list by splint the string on spaces
    text_list = text_string.split()
    
    #add the keys to the dict from the list with each key of length n(input)
    chains = {tuple(text_list[i:i+n_gram]):[] for i in range(len(text_list)-n_gram)}
    
    #loop over the dict for each of its keys
    for k in chains.keys():
        #for each n words in the text list and if they match, add the following 
        #word to the values
        for i in range(0,len(text_list)-n_gram): 
            if tuple(text_list[i:i+n_gram]) == k:
                chains[k].append(text_list[i+n_gram])
    
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []
    current_key = choice(list(chains.keys()))
        
    # a, b = current_key
    # words.append(a)
    # words.append(b)

    for word in current_key:
        words.append(word)
    
    #perform following commands until key not found in dict or 
    #value for the key is an empty list 
    while current_key in chains and len(chains[current_key]) != 0:
        #choose a random word from the values
        chosen_word = choice(chains[current_key])
        #append the chosen word to the output
        words.append(chosen_word)
        #create a new key tuple of lenth n using the current key and the chosen 
        #word
        current_key = current_key[1:]+(chosen_word,)
    
    
    return " ".join(words)


#input_path = "green-eggs.txt"
input_path = sys.argv[1]
input_n = int(sys.argv[2])

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text,input_n)

# Produce random text
random_text = make_text(chains)

print(random_text)

