# TJ-Tasks-2026--KISHAN-SINGH-

# Basic NLP Message Classifier

## About the Project

This is a beginner-level Natural Language Processing (NLP) project.

The program takes a customer message, cleans the text by removing common stop words and punctuation, and then classifies the message into one of three categories:

- Technical Support
- Billing Support
- General Inquiry

The classification is done using basic Python `if-elif-else` logic and predefined keywords.

## Features

- Converts text to lowercase
- Removes punctuation
- Splits sentences into words
- Removes common stop words
- Finds important keywords
- Classifies messages using simple keyword matching

## Technologies Used

- Python
- Python built-in `string` library

No external NLP or machine learning libraries are used.

## How It Works

The program follows these steps:

1. Take the customer message as input.
2. Convert the message to lowercase.
3. Remove punctuation.
4. Split the message into individual words.
5. Remove common stop words.
6. Check the remaining keywords.
7. Classify the message into the appropriate department.

## Classification Rules

### Technical Support

The message is classified as Technical Support if it contains:

- crash
- crashes
- bug
- broken
- error

### Billing Support

The message is classified as Billing Support if it contains:

- bill
- charged
- payment
- subscription

### General Inquiry

If none of the above keywords are found, the message is classified as General Inquiry.

## Example

### Input

"My app crashes every time I open it!"

### Filtered Keywords

```text
['app', 'crashes', 'every', 'time', 'open', 'it']