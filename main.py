# This is a sample Python script.
from nltk import word_tokenize

def replace_written_numbers(text):
    written_numbers = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine" : "9",
        "ten" : "10",
        "eleven" : "11",
        "twelve" : "12",
        "thirteen" : "13",
        "fourteen" : "14",
        "fifteen" : "15",
        "sixteen" : "16",
        "seventeen" : "17",
        "eighteen" : "18",
        'nineteen' : "19",
        "twenty" : "20",
        "thirty" : "30",
        "forty" : "40",
        "forty-four" : "44",
        "forty-seven" : "47",
        "fifty" : "50",
        "sixty" : "60",
        "seventy" : "70",
        "eighty" : "80",
        "ninety" : "90",
        "thousand" : "1000",
    }
    if text in written_numbers:
        return written_numbers[text]
    return text

def clean_file(input_file, output_file):
    with open(input_file, 'r') as original:
        with open(output_file, 'w') as cleaned:
            blacklist = {"F634", "F631", "f634", "f631"} #speaker codes
            new_line_trigger = {"and", "but", "so"}

            for line in original:
                tokens = word_tokenize(line)
                in_brackets = 0
                for token in tokens:
                    token = token.lower()
                    token = replace_written_numbers(token)
                    if token == "[":
                         in_brackets = 1
                    elif token == "]":
                         in_brackets = 0
                    if not in_brackets and token.isalnum() and token not in blacklist:
                        if token in new_line_trigger: #
                             cleaned.write('\n')
                        cleaned.write(token)
                        cleaned.write(" ")


# # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    clean_file('SC349_CoP_Original.txt','SC349_CoP_Cleaned.txt')
    clean_file('SC349_Human_Original.txt','SC349_Human_Cleaned.txt')