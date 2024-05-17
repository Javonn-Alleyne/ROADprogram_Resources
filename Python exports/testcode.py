import pandas as pd

with open ("Ashley_Tamisha_Rasheda__D01025__D01025__May 16 2024__Station4leftcamera__9-38 AM 2024-05-16.txt", "r") as file:
    content = file.read()
    content = content.replace("(", "")
    content = content.replace(")", "")
#open the text file to be used
#remove the brackets "()" from the file raw file to aid in processing the '.csv' file format

import re #imoprt the regular expression 're' module to manipulate the data in the textfile
lightness_factors = re.search("(?<=Upper Limit).*(?=79.2%)",content,re.S).group(0)
#line 11 expression states:
    #create an object called 'Lightness_factors' and within the range of the object 
    #match an empty string that contains a string called '72.9%' only if there is a string called 'Upper Limit' before it with in the text file
    #to simplyfy. Eveything inbetween 'Tone Respones' and '79.2%' should be printed

lightness_factors_lines=lightness_factors.split("\n") #split the entire string into a list where each word is a list item and print them on a new line
lightness_factors_lines[0] #create a list and initalise it to/at 0

for line in lightness_factors_lines:
    print(line)
#print all the lines in the list

#with open ('test_results.txt', 'w') as file1:
    #for line in lightness_factors_lines:
        #file1.write(line+'\n')
#export results and 'write' to a new file
#ignore section

file1.close() #close file1
file.close() #close file

df = pd.DataFrame(lightness_factors_lines)
df.to_csv('csvtest.csv', index=False)
# uses the pandas library to export results to a '.csv' file
# it works :)