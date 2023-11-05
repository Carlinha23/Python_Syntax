# this should print "HELLO", "HEY", "YO", and "YES"

def print_upper_words(words, must_start_with):
    """Print words from the list that start with specified letters in uppercase."""
    for word in words:
        if word[0].lower() in must_start_with:
            print(word.upper())
            
print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})