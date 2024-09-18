# Write a fn. which takes two input filenames and one output filename and writes the concatanated output to the output file
# but after sorting

def concat_two_files_after_sort(file1,file2,output_file):
    file1_handler = open(file1,"r")
    file2_handler = open(file2,"r")

    output_file_handler = open(output_file,"w")

    file1_data = file1_handler.readlines()
    file2_data = file2_handler.readlines()


    output_data = file1_data + file2_data

    output_file_handler.writelines(sorted(output_data))

    output_file_handler.close()

concat_two_files_after_sort("words1.txt","words2.txt","problem6_out.txt")
