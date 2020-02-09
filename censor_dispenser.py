# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

# replaces the string-variabe word in the string-variable text by *-characters
def censor_word(word, text):
    # determine the replacement_string by detemining the length of the string and replacing every character in the string by *-characters
    replacement_string = ""
    for i in range(0, len(word)):
        replacement_string = replacement_string + "*"
    # replaces the string-variable word in the string-variable text by string-variable replacement_string
    new_text = text.replace(word, replacement_string)
    return new_text
