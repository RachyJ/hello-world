'''Simple million word count program.
    main idea is Python pairs words
    with the number of times
    that number appears in the triple quoted string.
    Credit to William J. Turkel and Adam Crymble for the word
    frequency code used below. I just merged the two ideas.
'''

wordstring = '''SCENE I. Yorkshire. Gaultree Forest.
Enter the ARCHBISHOP OF YORK, MOWBRAY, LORD HASTINGS, and others
'''

wordlist = wordstring.split()

wordfreq = [wordlist.count(w) for w in wordlist]

print("String\n {} \n".format(wordstring))
print("List\n {} \n".format(str(wordlist)))
print("Frequencies\n {} \n".format(str(wordfreq)))
print("Paires\n {}".format(str(list(zip(wordlist,wordfreq)))))