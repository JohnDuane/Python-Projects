word = input("Enter Word or Sentence: ")

while True:
    print("Choose an operator\n")
    print("  [1]Reverse the sentence")
    print("  [2]Count Vowels")
    print("  [3]Check if palindrome")
    print("  [4]Find and replace a word")
    print("  [5]Format (Title Case)")
    print("  [6]Split into words")
    print("  [7]Word Frequency counter")
    print("  [8]Swap Case")
    print("  [9]Exit")

    op = input("Option: ")


    if op == "1":
        rword = word[::-1]
        print("---------------------------")
        print(rword)
        print("---------------------------")


    elif op == "2":
        vowels = "aeiouAEIOU"
        count = 0

        for x in word:
            if x in vowels:
              count += 1
        print("--------------------")
        print("Number of Vowels: ", count)
        print("--------------------")

    elif op == "3":
        cword = word.replace(" ","").lower()
        
        if (word == cword[::-1]):
            print("----------")
            print("Positive")
            print("----------")
        else:
            print("----------")
            print("Negative")
            print("----------")

    elif op == "4":
        replaced = input("Enter a word that you want to replace: ")

        if replaced in word:
            neword = input("Enter the text that you want to replace: ")
            fin = word.replace(replaced,neword)
            print("-----------------------------")
            print("Heres the revision: ", fin)
            print("-----------------------------")

        else:
            print("------------------------")
            print("The word does not exist")
            print("------------------------")


    elif op == "5":
        print("--------------------------")
        print('"',word.title(),'"')
        print("--------------------------")

    elif op == "6":
        print("--------------------------")
        print('"',word.split(),'"')
        print("--------------------------")

    elif op == "7":
        sword = word.split()

        freq = {}

        for nword in sword:

            if nword in freq:
                freq[nword] += 1, "\n"

            else:
                freq[nword] = 1, "\n"

        print("----------------")
        print(freq)
        print("----------------")

    elif op == "8":
        print("----------------")
        print(word.swapcase())
        print("----------------")

    elif op == "9":

        print("Byee :)")
        break

    else:
        print("Error")
