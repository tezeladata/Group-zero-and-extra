import nltk
from nltk.util import ngrams
from nltk.tokenize import sent_tokenize, word_tokenize

import numpy as np
from collections import Counter

def search_suggestion(search_term, text):
    token = word_tokenize(text)
    
    # Create n-grams
    bigrams = list(ngrams(token, 2))
    trigrams = list(ngrams(token, 3))
    fourgrams = list(ngrams(token, 4))
    fivegrams = list(ngrams(token, 5))
    
    # Store n-grams in a list for easy access
    grams = [bigrams, trigrams, fourgrams, fivegrams]

    split_term = tuple(search_term.split(' '))
    search_term_length = len(split_term)

    # Get the correct n-gram based on the length of the search term
    if search_term_length - 1 < len(grams):
        counted_grams = Counter(grams[search_term_length - 1])
    else:
        return 'No suggested searches'
    
    matching_terms = [element for element in list(counted_grams.items()) if element[0][:-1] == split_term]
    
    if len(matching_terms) > 0:
        frequencies = [item[1] for item in matching_terms]
        maximum_frequency = np.max(frequencies)
        highest_frequency_term = [item[0] for item in matching_terms if item[1] == maximum_frequency][0]
        combined_term = ' '.join(highest_frequency_term)
    else:
        combined_term = 'No suggested searches'
    
    return combined_term

# Fetch the text file
import requests
file = requests.get('http://www.bradfordtuckfield.com/shakespeare.txt')
file = file.text
text = file.replace('\n', '')

# Example usage
print(search_suggestion(input("Enter phrase: "), text))