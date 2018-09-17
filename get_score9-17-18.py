#Bridger Hope
#9/118
import math
# get the users test scores
def get_scores():
      score1 = float(input("what is your first test score?"))
      score2 = float(input("what is your second test score?"))
      score3 = float(input("what is your third test score?"))
      score4 = float(input("what is your fourth test score?"))
      score5 = float(input("what is your fith test score?"))
      score6 = float(input("what is your sixth test score?"))
      score7 = float(input("what is your seventh test score?"))
      score8 = float(input("what is your eight test score?"))
      score9 = float(input("what is your nineth test score?"))
      score10 = float(input("what is your tenth test score?"))

      all_scores = score1 + score2 + score3+ score4 + score5 + score6 + score7 + score8 + score9 + score10
      avg_score = all_scores/10
      return avg_score

print(get_scores())

    
