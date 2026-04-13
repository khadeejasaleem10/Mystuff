# ADD CODE: make it so that the program can use the randint function

def main() :
  MAX_SCORE = 300
  MIN_SCORE = 0
  NUM_SCORES = 10
  
  # ADD CODE: Create an empty list named scores
  
  # ADD CODE: To the scores list append NUM_SCORES scores in the 
  # range [MIN_SCORE, MAX_SCORE]

  
  # ADD CODE: Insert one print statement to print the scores list (no loop)  
  
  scoreCutoff = int(input("Display bowling scores at or above which score? "))
  print(getScores(scores, scoreCutoff))

# ADD CODE for getScores
# getScores creates a new list of scores at or above a certain cutoff score
# @param scores The list of scores to check
# @param scoreCutoff Holds the cutoff score.
# @return A list containing those scores at or above the cutoff.


main()
