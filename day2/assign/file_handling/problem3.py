# Write a fn. that takes a filename and 'n' and finds the number of sentences with 'n' words.

def number_of_sentence_with_n_words_in_sentencefile(filename,n):
    file_handler = open(filename,"r")  #used to store the content of file in file_handler
    file_list = file_handler.readlines() #used to store the individual lines as list in file_list
    wordcount_in_sentence = 0
    for sentence in file_list:#iterate through the lines
        words = sentence.strip().split() #removes the spaces and splits the sentences into words
        if(len(words) == n):         #checks if the no of words in a sentence is equal to n 
            wordcount_in_sentence += 1
    file_handler.close()
    return wordcount_in_sentence

print(number_of_sentence_with_n_words_in_sentencefile("sentences_1.txt",4))
