
#Standard Imports

#File Imports

#Import the spam/ham sample datasets
from Data.categorical_data import spam_emails, ham_emails


#Function that trains the model weights based off ham
    #Loops through ham
    #Calls function to transfer string to an array
    #loops through the new array
    #for each word in the array 
        #If new word (use .includes)
            #create a new weight for it at 0 and 
            #Adjust in the negative
        #If old word
            #Adjust the weight by -0.01

#Function that trains the model weights based off spam
    #Refer to above except positive weights










#Function that gets called on text change that analyzes the current string using .includes to analyze similar words. multiply similar words by weight and then sum them for an output with a sigmoid function in order to keep it below 1 and above -1
    #Display in the textbox somewhere


