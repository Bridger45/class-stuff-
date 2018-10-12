#Bridger Hope
#10/18
import math
# get the users grade
def get_scores():
      grade1 = float(input("what is your first grade?"))
      grade2 = float(input("what is your second grade percentage?"))
      grade3 = float(input("what is your third test score?"))
      grade4 = float(input("what is your fourth test score?"))
      grade5 = float(input("what is your fith test score?"))
      grade6 = float(input("what is your sixth test score?"))
      grade7 = float(input("what is your seventh test score?"))
      grade8 = float(input("what is your eight test score?"))
      grade9 = float(input("what is your nineth test score?"))
      grade10 = float(input("what is your tenth test score?"))

      all_scores = grade1 + grade2 + grade3 + grade4 +
      grade5 + grade6 + grade7 + grade8 + grade9 + grade10
      avg_score = all_scores/10
      return avg_score

print(get_scores())
input()
print("press enter to enter")
