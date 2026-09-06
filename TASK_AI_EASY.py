# 1. Define common stop words to ignore
STOP_WORDS = ["the", "is", "at", "which", "and", "to", "a", "an", "for", "my", "i"]

def clean_and_tokenize(text):
    # TODO: Convert text to lowercase, split into words, and filter out stop words
    pass

def classify_message(text):
    # TODO: Get filtered keywords and use if-else logic to classify the message
    pass

# Test your code here
print(classify_message("the app crashes every time I open it"))