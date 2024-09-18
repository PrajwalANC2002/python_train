# Write a fn. that takes a filename and 'n' and finds the number of words with 'n' characters. Assume one word per line

def number_of_words_with_n_char_in_wordfile(filename,n):
    file_handler = open(filename,"r")  #used to store the content of file in file_handler
    file_list = file_handler.readlines() #used to store the individual lines as list in file_list 
    wordcount = 0
    for sentence in file_list:              #iterates through the sentences
        word = sentence.strip() #removes the spaces in the sentence 
        if(len(word) == n):     #checks if the no of characters in a word is equal to n
            wordcount += 1      #increment the wordcount
    file_handler.close()
    return wordcount

print(number_of_words_with_n_char_in_wordfile("words1.txt",10))


