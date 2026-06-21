"""
PROBLEM STATEMENT:
Write a program to Count words in a sentence.
"""

def count_words(sentence):

    """Counts the total number of words in the given sentence string.
       We can use Python's split() method, which automatically handles consecutive whitespace and splits the string into a list of individual words. 
       We then find the length of this list to get the total word count. 
       The time complexity of this approach is O(n), where n is the length of the sentence, as it iterates through the string to split it."""
    
    words = sentence.split()
    
    return len(words)

input_sentence = input("Enter a sentence: ")

word_count = count_words(input_sentence)

print(f"The number of words in the sentence is: {word_count}")