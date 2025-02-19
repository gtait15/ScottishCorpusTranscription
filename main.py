# This is a sample Python script.
from nltk import word_tokenize

def clean_file(input_file, output_file):
    with open(input_file, 'r') as original:
        with open(output_file, 'w') as cleaned:
            for line in original:
                tokens = word_tokenize(line)
                in_brackets = 0
                for token in tokens:
                    if token == "[":
                         in_brackets = 1
                    elif token == "]":
                         in_brackets = 0
                    if not in_brackets and token.isalnum():
                        token = token.lower()
                        if token == "and" or token == "but" or token == "so": #
                             cleaned.write('\n')
                        cleaned.write(token)
                        cleaned.write(" ")


# # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    clean_file('SC349_CoP_Original.txt','SC349_CoP_Cleaned.txt')
