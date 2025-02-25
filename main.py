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
        "fifty-one" : "50",
        "sixty" : "60",
        "seventy" : "70",
        "eighty" : "80",
        "ninety" : "90",
        "thousand" : "1000",
    }
    if text in written_numbers:
        return written_numbers[text]
    return text

def clean_up(text):
    text = text.lower()
    text = text.replace_written_numbers(text)
    text = text.replace("/", "")
    text = text.replace(".", "")
    # token = token.replace("ing", "in") #chaotic way to fix
    return text

def clean_file(input_file, output_file):
    with open(input_file, 'r') as original:
        with open(output_file, 'w') as cleaned:
            black_list = {"f634", "f631", "mm", "mmhm", "em", "erm", "eh", "uh", "uhhuh", "um",
                          "ehm", "huh", "er", "f1071", "m1070", "f718", "f1077", "m1078"}
            new_line_trigger = {"and", "but", "so", "no", "yeah", "yes"}
            contraction_endings = {"'nt", "'ll", "'d", "'ve", "'t","'t've","'s","'n","'d", "'re",
                            "'all", "'mon", "n't", "'m"} #nltk inconsistent about tokenizing these for some reason
            contractions = {"didn't", "o'clock", "don't", "i'm", "can't", "isn't", "that's", "you've"}
            for line in original:
                tokens = word_tokenize(line)
                in_brackets = 0
                for token in tokens:
                    token = clean_up(token)
                    if token == "[":
                         in_brackets = 1
                    elif token == "]":
                         in_brackets = 0
                    if not (token.replace("'", "").isalnum() or token.replace("-", "").isalnum()):
                        print(token)
                    if not in_brackets and token not in black_list and (token.replace("'","").isalnum() or token.replace("-", "").isalnum()):
                        if token in new_line_trigger:
                             cleaned.write('\n')
                        if token not in contraction_endings:
                            cleaned.write(" ")                           #add space if not contraction
                            if token not in contractions:
                                token = token.replace("'","")   #human transcription uses "'" for quotes and nltk gets confused
                        cleaned.write(token)

if __name__ == '__main__':
    #clean_file('SC349_CoP_Original.txt','SC349_CoP_Cleaned.txt')
    clean_file('SC349_CoP_Original2.txt','SC349_CoP_Cleaned2.txt')
    clean_file("SC1485_CoP_Original.txt", "SC1485_CoP_Cleaned.txt")
    clean_file("SC1521_CoP_Original.txt", "SC1521_CoP_Cleaned.txt")

    clean_file('SC349_Human_Original.txt', 'SC349_Human_Cleaned.txt')
    clean_file('SC1485_Human_Original.txt', 'SC1485_Human_Cleaned.txt')
    clean_file('SC1521_Human_Original.txt', 'SC1521_Human_Cleaned.txt')