"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    return open(file_path).read()
    #return 'Contents of your file as one long string'
    

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    word = text_string.split()
    for i in range(len(word) - 2):
        word_tuple = (word[i], word[i + 1])
        if word_tuple not in chains:
            chains[word_tuple] = []
            #word[i+2] == 'Would'
            #{('a', 'fox?'): []}
            #{('a', 'fox?'): ['Would']}
        chains[word_tuple].append(word[i + 2])
    return chains

def make_text(chains):
    """Return text from chains."""
    # pick a random key from the dictionary 
    key = choice(list(chains.keys()))
    #{('a', 'fox?'): ['Would']}
    words = [key[0], key[1]]
    # figure out if "key" is actually in the dictionary (chains)
    # only choose a word when it is
    word = choice(chains[key]) #{('a', 'fox?'): ['Random']}
    
    #create a list to store the keys
    # while word is not KeyError
    # while word is not None:
    #     key = (key[1], word) #current output: {dict[key], rand_word} || {('a', 'fox?'): []}
    #     words.append(word)
    #     word = choice(chains[key]) # pick a random word from chains[key]
    # return ' '.join(words)

    while chains.get(key):
        try:
            word = choice(chains[key])
            words.append(word)
            key = (key[1], word)
        except:
            raise KeyError
    return ' '.join(words)

input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)

# try:
#  word = choice(chains[key])
#  words.append(word)
#  key = (key[1], word)
#except:
#  raise KeyError
# --
# if key in chains:
    # word = choice(chains[key])
    # words.append(word)
    # key = (key[1], word)
# else
    # break
#join 