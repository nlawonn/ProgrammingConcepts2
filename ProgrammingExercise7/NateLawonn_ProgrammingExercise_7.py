import re

def split_into_sentences(text: str) -> list[str]:
    """
    Takes a paragraph of text and splits it into a list of sentences
    using a regular expression.
    """
    # The regex pattern matches sentences ending in ., !, or ?
    pat = r'.*?[.!?](?=\s+(?:[0-9]\.)?|$)'
    sentences = re.findall(pat, text, flags=re.DOTALL)
    return sentences

def analyze_paragraph():
    """
    Handles user input, calls the processing logic, 
    and prints the formatted results.
    """
    paragraph = input("Please enter a paragraph: ")
    
    # Process the text using split_into_sentences
    sentence_list = split_into_sentences(paragraph)
    
    # Print each sentence
    for sentence in sentence_list:
        print('->',sentence)
        
    # Get the total count using len() function
    total_sentences = len(sentence_list)
    print(f"Total sentences: {total_sentences}")

# This ensures the code runs when script is executed
if __name__ == "__main__":
    analyze_paragraph()