# Write a fn. that takes a filename and 'n' as an argument to writes the following pattern to a file.
 
# The pattern increases for 'n' and lines and decreases there-after. Example is for n = 3
               #
              ###
             #####
              ###
               #

def pattern(filename,n):
    output_handler = open(filename,"w")
    for i in range(1,n + 1):
        space_count = n - i
        hash_count = (2 * i - 1)
        output_handler.write(" " * space_count + "#" * hash_count + " " * space_count + "\n")

    for i in range(n-1,0,-1):
        space_count = n - i 
        hash_count = (2 * i -1)
        output_handler.write(" " * space_count + "#" * hash_count + " " * space_count + "\n")
    output_handler.close()


    
pattern("pattern.txt",3)
