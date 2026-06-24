"""
PROBLEM STATEMENT:
Write a program to Find longest word.
"""

def find_longest_word(sentence):

    """Finds the longest word in a given sentence.
       This function splits the sentence into individual words based on whitespace 
       and iterates through them to identify the word with the maximum length. 
       The time complexity of this approach is O(n), where n is the length of the sentence."""
    
    if not sentence.strip():
    
        return ""
        
    words = sentence.split()
    
    longest_word = words[0]
    
    for word in words:
    
        if len(word) > len(longest_word):
        
            longest_word = word
            
    return longest_word

user_sentence = input("Enter a sentence: ")

result = find_longest_word(user_sentence)

print(f"The longest word is: {result}")