# write a program to read the text from a given the poem.txt and find out whether it contains the word 'twinkle'

with open("pyTuturiol\poem.txt") as p :
    text = p.read()
    if 'twinkle' in text.lower():
            print("The poem contains the word 'twinkle'")
            print("Number of occurrences:", text.lower().count('twinkle'))
    else:
        print("The poem does not contain the word 'twinkle'")
    p.close()