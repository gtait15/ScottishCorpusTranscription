# This is a sample Python script.
import nltk
from nltk import word_tokenize
nltk.download('punkt_tab')

#Press Shift+F10 to execute it or replace it with your code.
# Press Ddef print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#


# # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open('SC349_CP_Original.txt', 'r', encoding="utf-8") as original:
        with open('SC349_CP_Cleaned.txt', 'w') as cleaned:
            word_count = 0
            for line in original:
                tokens = word_tokenize(line)
                ignored = 0
                for token in tokens:
                    token.lower()
                    if token == "[":
                         ignored = 1
                    elif token == "]":
                         ignored = 0
                    if not ignored and token.isalnum():
                        word_count += 1
                        cleaned.write(token)
                        cleaned.write(" ")
                        if word_count > 16:
                             cleaned.write('\n')
                             word_count = 0


