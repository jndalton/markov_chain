"""
Codecademy python 2 final project.
Markov Chain Text Generator.
Jack Dalton.
May 19, 2019.
"""

#Import methods from fetch_data.py and cc_markov.py
from fetch_data.py import fetch_web_data
from cc_markov.py import MarkovChain

mc = MarkovChain()

# links to necessary works

catalog = {
"Romeo and Juliet": "http://shakespeare.mit.edu/romeo_juliet/full.html",
"Macbeth": "http://shakespeare.mit.edu/macbeth/full.html",
"The Bell Jar": "http://gutenberg.ca/ebooks/plaths-belljar/plaths-belljar-00-e.html"
}
link = ""

"""
The next three functions determine the chosen book, number of passages,
and the number of words per passage that the generated strict will have.
"""

def choose_book():
    print "Which book would you like to see mimicked?"
    print "Enter 1 for Romeo and Juliet, 2 for Macbeth, and 3 for The Bell Jar."
    choice = ""
    link = ""

    while choice = "":
        choice = raw_input("Enter a number:")
        if choice == 1:
            print "Romeo and Juliet passage generator initializing..."
            link = catalog["Romeo and Juliet"]
        elif choice == 2:
            print "Macbeth passage generator initializing..."
            link = catalog["Macbeth"]
        elif choice == 3:
            print "The Bell Jar passage generator initializing..."
            link = catalog["The Bell Jar"]
        else:
            choice = ""
    return link

def choose_number_passages():
    print "How many passages would you like to have generated?"
    number_passages = raw_input("Enter a number 1-5: ")
    if number_passages > 0 and number_passages < 6:
        return number_passages
    else:
        print "Invalid number of passages, try again."
        choose_number_passages()

def choose_number_words():
    print "How many words would you like per passage?"
    number_words = raw_input("Enter a number 4-100")
    if number_words >= 4 and number words <= 100:
        return number_words
    else:
        print "Invalid number of words, try again."

def generate_passages():
    print ""
    print "Welcome to the MHS reading list passage generator."
    choose_book()
    choose_number_passages()
    choose_number_words()
    mc.add_string(fetch_data.fetch_web_data(link))
    for current_passage in range(number_passages):
        try:
            temp = mc.generate_text(number_words)
            formatted = " ".join(temp)
            print "Passage #" + str(current+1) + ": " + formatted
            break
        except UnicodeEncodeError:
            pass

generate_passages()
