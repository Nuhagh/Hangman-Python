# -*- Nuha Alghamdi -*-
# -*- nuhaalghamdi92@gmail.com -*-
# -*- Oct 19 2019 -*-


import random

#list of lists
#each element in the list is a list contains string define the type of words (as a hint) and a list of words
wordlists=[["Fruits",["apple","grapes","kiwi","melon"]],["School",["book","pencil","pen","stabler"]],["Sky",["moon","sun","clouds","birds"]]]
#variable for the selected word from the list, its hint, and its index
word=""
hint=""
index=-1

#To draw hangman based on the number of faulty attempts
def draw_hangman(tries):
    if 4<tries<10:
        print("   -----   ")
    if 4<tries<9:
        print("     0     ")
    if 4<tries<8:
        print("     |     ")
    if tries==6:
        print("    /      ")
    if tries==5:
        print("   /   \\   ")
    if tries==4:
        print("   -----   ")
        print("   \\ 0     ")
        print("     |     ")
        print("   /  \\   ")

    if tries==3:
        print("   -----   ")
        print("   \\ 0 /  ")
        print("     |     ")
        print("   /   \\   ")
    if tries==2:
        print("   -----   ")
        print("   \\ 0 /| ")
        print("     |     ")
        print("   /   \\   ")
    if tries==1:
        print("   -----   ")
        print("   \\ 0 /_|")
        print("     |     ")
        print("   /   \\   ")
    if tries==0:
        print("   -----   ")
        print("     0_|   ")
        print("    /|\\   ")
        print("    / \\   ")


#Ask user about his name
name=input("Enter your name: ")
#Welcoming the user :)
print("Welcome ", name)
print("--------------------")



#To swap between underscores and correctly guessed chars
def correct_char(guess,answer,word):
    #Count the number of occurance of each guessed letter
    char_count=word.count(guess)
    for letter in word:
        #Initial value
        char_index=-1
        #Check if a the guessed character match a letter in the word and it appears one time
        if letter == guess and char_count==1:
            #Index of the correctly guessed char
            char_index=word.index(letter)
            #Convert the string into list to exchange a value in a specific index
            answer=list(answer)
            #Change the _ in the index with the correct char
            answer[char_index*2]=guess
        #Check if a the guessed character match a letter in the word and it appears multiple times
        elif letter == guess and char_count>1:
            #Get all the indices of the guessed char
            indices = [i for i, a in enumerate(word) if a == guess]
            #Replace each _ in the word with the same char
            for index in indices:
                char_index=index
                answer=list(answer)
                answer[char_index*2]=guess
    #Make the variable a string again
    answer=''.join(answer)
    return answer

#To print number of reminder turns and call the drawing function
def wrong_char(tries):
    if tries>0:
        print(tries," turns are left")
    else:
        print("You lose. You let a kind man die.")
    draw_hangman(tries)


#This variable for the user if he wants to play multiple times
repeat="y"


while repeat=="y":
    #number of allowed turns
    turns=10
    print("Guess the word in ten attempts.")

    #This loop to select a random wordlist from wordlists
    for item in wordlists:
        #Index of the selected list
        list_index=random.randint(0,len(wordlists)-1)
        #Get the hint of the list
        hint=wordlists[list_index][0]
        #Get the index of a randomly selected word from the selected list
        index=random.randint(0,len(wordlists[list_index][1])-1)
        #The selected word to be guessed by the user
        word=wordlists[list_index][1][index]
    #Print the hint
    print("Hint: ",hint)
    #Print  _ _ _ _
    answer="_ "*len(word)
    #The word after guessing the characters
    user_word=""
    while user_word != word and turns>0:
        print("\n")
        print("Guess the word: ", answer)
        #Get user input (his guess)
        guess=input()
        #Check if the guessed char is already a char in the selected word
        if guess in word:
            #Call the function that will swap each _ with the correctly guessed char
            answer=correct_char(guess,answer,word)
            user_word=answer
            user_word=user_word.replace(" ","")
        #If the guessed char is a wrong one
        else:
            #The user loses one attempt and wrong_char will be called
            turns=turns-1
            wrong_char(turns)
    #Congratulate the user if he guessed all the chars of the word correctly before finishing his attempts

    if turns>0:
        print(word)
        print("Congratulations!")
    #Ask the user if he wants to play again if he guessed the word correctly or finished his attempts
    repeat=input("Play again? Press y for yes and n for no: ")
    while repeat != "n" and repeat != "y":
        repeat=input("PLEASE press y for yes and n for no: ")
