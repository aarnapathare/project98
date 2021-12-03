def countnumberofwords():
    filename = input("Enter the File name ")
    file = open(filename)
    numberofwords = 0
    for line in file :
        words = line.split()
        print(words)
        numberofwords = numberofwords+len(words)
    print("Number of Words are ", numberofwords)

countnumberofwords()


    
