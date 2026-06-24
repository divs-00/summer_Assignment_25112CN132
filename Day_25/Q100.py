"""
PROBLEM STATEMENT:
Write a program to Sort words by length.
"""

def sort_words_by_length(sentence):

    """Sorts the words in a given sentence by their length in ascending order.
       This function splits the sentence into a list of words, then sorts them 
       based on the length of each word while preserving the original order for words of equal length.
       The time complexity of this approach is O(n * log(n)), where n is the number of words in the sentence."""
    
    if not sentence.strip():
    
        return []
        
    words = sentence.split()
    
    sorted_words = sorted(words, key=len)
    
    return sorted_words

user_sentence = input("Enter a sentence: ")

result = sort_words_by_length(user_sentence)

print(f"Words sorted by length: {result}")