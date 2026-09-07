import string


# Common stop words
STOP_WORDS = [
    "the", "is", "at", "which", "and",
    "to", "a", "an", "for", "my", "i"
]

# Function to clean and tokenize the text
def clean_and_tokenize(text):
    
    # Convert text to lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Split the text into words
    words = text.split()

    # Remove stop words
    keywords = []

    for word in words:
        if word not in STOP_WORDS:
            keywords.append(word)

    return keywords


# Function to classify the message
def classify_message(text):
    
    # Get the filtered keywords
    keywords = clean_and_tokenize(text)

    # Check for technical support keywords
    if ("crash" in keywords or
        "crashes" in keywords or
        "bug" in keywords or
        "broken" in keywords or
        "error" in keywords):
        
        return keywords, "Technical Support"

    # Check for billing support keywords
    elif ("bill" in keywords or
          "charged" in keywords or
          "payment" in keywords or
          "subscription" in keywords):
        
        return keywords, "Billing Support"

    # If no keyword matches
    else:
        return keywords, "General Inquiry"


# Test the program
messages = [
    "The app crashes every time I open it!",
    "I was charged for my subscription.",
    "Can you tell me more about your services?"
]


for message in messages:
    keywords, result = classify_message(message)

    print("Message:", message)
    print("Filtered Keywords:", keywords)
    print("Classification:", result)
    print()