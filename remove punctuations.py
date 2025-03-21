import string

def remove_punctuations(input_string):
    # Create a translation table that maps punctuations to None
    translator = str.maketrans('', '', string.punctuation)
    
    # Use the translation table to remove punctuations
    return input_string.translate(translator)

# Example usage
input_string = "Hello, world! This is a test string with punctuations."
output_string = remove_punctuations(input_string)
print("Original String:", input_string)
print("String without Punctuations:", output_string)
