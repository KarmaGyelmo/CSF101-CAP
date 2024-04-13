################################
# Karma Gyelmo
# 1EE
# 02230315
################################
# REFERENCES
# https://codingwithjohn.com/rock-paper...
# https://github.com/kying18/rock-paper...
# https://github.com/ShaunHalverson/Pyt...
################################
# SOLUTION
# Your Solution Score: 49977
# 5
################################

#Read the input.txt file
def read_input(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            input_file = [line.strip().replace(' ', '') for line in lines]  # Extract and format conditions pairs
            return input_file
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return []

def calculate_score(input_file):
    #creating a variable and assigning the scores for it
    A = 1
    B = 2
    C = 3
    X = 0
    Y = 3
    Z = 6
# Initializing score
    score = 0  
    for conditions in input_file:
         
        if conditions == 'AX':
            #If opponent chooses Rock and the event should end by loss
            #I should choose scissor and accordingly score is updated
            score += C + X
        elif conditions == 'AY':
             #If opponent chooses Rock and the event should end by draw
            #I should choose ROCK and accordingly score is updated
            score += A + Y
        elif conditions == 'AZ':
            #If opponent chooses Rock and the event should end by win
            #I should choose paper and accordingly score is updated

            score += B + Z
            #The selection logic remains the same further and score is updated every instance
        elif conditions == 'BX':
            score += A + X
        elif conditions == 'BY':
            score += B + Y
        elif conditions == 'BZ':
            score += C + Z
        elif conditions == 'CX':
            score += B + X
        elif conditions == 'CY':
            score += C + Y
        elif conditions == 'CZ':
            score += A + Z

    #I am returning the total score 
    return score

#I could have directly writte the input txt location into the fuunction parameters but 
#for more efficiency i gave the file location to a variable so that it can be easily changed. 
input_file = 'input_5_cap1 (1).txt' 


input_file = read_input(input_file)
if input_file:
    total_score = calculate_score(input_file)
    print(f"Total score: {total_score}")