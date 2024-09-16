# Write a function which takes two argumets and checks if the first string is an anagram of the second string. Should return True if string is anagram, else False
# An anagram is a word or phrase formed by rearranging the letters of a different word. For example, cinema is an anagram of iceman.

string1 = "cinema"
string2 = "iceman"

def is_anagram(s1,s2):
    letters_count_s1 = {}    #dictionary for string 1 letter count
    letters_count_s2 = {}    #dictionary for string 2 letter count

    if(len(s1) != len(s2)):  #if lenghts are not equal no need to check other condition
        return False
    else:
        for i in s1:                   #to create a dictionary for letter count in string1
            if( i in letters_count_s1):
                letters_count_s1[i] += 1
            else:
                letters_count_s1[i] = 1

        for j in s2:
            if( j in letters_count_s2): #to create a dictionary for letter count in string2
                letters_count_s2[j] += 1
            else:
                letters_count_s2[j] = 1

    if( letters_count_s2 == letters_count_s1):
        return True
    else:
        return False


print(is_anagram(string1,string2))

