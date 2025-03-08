from nltk import word_tokenize

#makes text lowercase, removes "/" and ".", and converts most written numbers to numerals,
#e.g., "sixty" -> "60"
def clean_up(text):
    text = text.lower()
    text = text.replace("/", "")
    text = text.replace(".", "")
    #token = token.replace("ing", "in") #chaotic way to fix

    #doesn't include every number but it's enough to make human error checking a little easier at least
    written_numbers = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "ten": "10",
        "eleven": "11",
        "twelve": "12",
        "thirteen": "13",
        "fourteen": "14",
        "fifteen": "15",
        "sixteen": "16",
        "seventeen": "17",
        "eighteen": "18",
        'nineteen': "19",
        "twenty": "20",
        "twenty-six" : "26",
        "thirty": "30",
        "thirty-nine" : "39",
        "forty": "40",
        "forty-four": "44",
        "forty-six": "46",
        "forty-seven": "47",
        "fifty": "50",
        "fifty-one": "51",
        "sixty": "60",
        "sixty-nine" : "69",
        "seventy": "70",
        "seventy-one" : "71",
        "eighty": "80",
        "ninety": "90",
        "thousand": "1000",
    }
    if text in written_numbers:
        return written_numbers[text]
    return text

def token_not_punctuation(text):
   return text.isalnum() or text.replace("'","").isalnum() or text.replace("-", "").isalnum() or text.replace("*", "a").isalnum()

def clean_file(input_file, output_file):
    with open(input_file, 'r') as original:
        with open(output_file, 'w') as cleaned:
            #create a blacklist of SC speaker codes and disfluencies that CoP usually doesn't transcribe
            black_list = {"f634", "f631", "f1071", "m1070", "f718", "f1077", "m1078", "f718", "m734",
                          "mm", "mmhm", "em", "erm", "eh", "uh", "uhhuh", "um",
                          "ehm", "huh", "er",  "uh-huh", "hm"}

            #create a set of new line triggers because CoP spits out really long lines that need to be broken up
            #new_line_triggers = {"and", "but", "so", "no", "yeah", "yes", "oh", "well"}

            #needed more line breaks for 1485 because CoP had too much trouble with it and comparison is hard
            new_line_triggers = {"and", "but", "so", "no", "yeah", "yes", "oh", "well",
                                 "squirrel", "i", "what", "who", "did", "will", "does", "which"}



            #need to deal with contractions in two separate ways
            #because nltk is inconsistent about tokenizing them for some reason
            contraction_endings = {"'nt", "'ll", "'d", "'ve", "'t","'t've","'s","'n","'d", "'re",
                            "'all", "'mon", "n't", "'m"}
            contraction_words = {"didn't", "o'clock", "don't", "i'm", "can't", "isn't", "that's", "you've", "mummy's"}

            #go through each line, separate tokens, remove punctuation and add to new file
            for line in original:
                tokens = word_tokenize(line)
                in_brackets = 0
                for token in tokens:
                    token = clean_up(token)

                    #human transcriptions have "[inhale]", "[laugh]" etc. which we want to cut out
                    if token == "[":
                         in_brackets = 1
                    elif token == "]":
                         in_brackets = 0

                    if not in_brackets and token not in black_list and token_not_punctuation(token):
                        #add line breaks
                        if token in new_line_triggers:
                             cleaned.write('\n')

                        #deal with possible contractions and add spaces
                        if token not in contraction_endings:
                            #add space only if token is not a contraction
                            cleaned.write(" ")
                            #cut out "'" used for quotes while keeping genuine contractions
                            if token not in contraction_words:
                                token = token.replace("'","")

                        #finally write token to file
                        cleaned.write(token)

if __name__ == '__main__':
    #clean_file('SC349_CoP_Original.txt','SC349_CoP_Cleaned.txt')  #accidentally done with US English transcription
    #clean_file('SC349_CoP_Original2.txt','SC349_CoP_Cleaned2.txt')
    clean_file("SC1485_CoP_Original.txt", "SC1485_CoP_Cleaned.txt")
    #clean_file("SC1521_CoP_Original.txt", "SC1521_CoP_Cleaned.txt")
    #clean_file("SC579_CoP_Original.txt", "SC579_CoP_Cleaned.txt")

    #clean_file('SC349_Human_Original.txt', 'SC349_Human_Cleaned.txt')
    clean_file('SC1485_Human_Original.txt', 'SC1485_Human_Cleaned.txt')
    #clean_file('SC1521_Human_Original.txt', 'SC1521_Human_Cleaned.txt')
    #clean_file('SC579_Human_Original.txt', 'SC579_Human_Cleaned.txt')