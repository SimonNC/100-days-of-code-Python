#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("./input/Names/invited_names.txt") as invited_names:
    name_list = (invited_names.readlines())

with open("./input/Letters/starting_letter.txt") as file:
    contents = file.read()

    for name in name_list:
        name = name.strip()
        new = contents.replace("[name]", name)
        with open(f"./Output/ReadyToSend/{name}.txt", "w") as final_file:
            final_file.write(new)
