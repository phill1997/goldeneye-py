#!/usr/bin/env python3.7

#Python implementation here

message = input("Enter a message: ")
print("\n", "Message in lower case: ", message.lower())
print("\n", "Message in upper case: ", message.upper())
print("\n", "Message as a title case: ", message.title())
print("\n", "Message with capitalization: ", message.capitalize())
words = message.split()
print("\n", "Message split into list ", words)

sorted_words = sorted(words)
print("\n", "Alphabetic first word: ", sorted_words[0]) # Capital and lower case words will make a differnce
#as to what words are sorted first. Consider making the list all upper or lower case so the alphabetizing is accurate.
print("\n", "Alphabetic last word: ", sorted_words[-1])
