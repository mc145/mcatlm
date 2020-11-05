import sys 
problem_subject = input("What subject is this problem from (geometry, algebra, number theory, or combinatorics?\n")
difficulty = int(input("What is the difficulty of this problem in your rating scale?\n")) 
subject_matter = input("What is the subject matter of this problem (i.e. homethety, totient function)? \n")
year_attempted = int(input("What year did you most recently attempt this problem?\n"))
author = input("What is the author of this problem?\n")
contest = input("What contest is this problem from?\n")
print("_________________________________________________________________\n")
print("Insert Problem (in LaTeX) \n")
problem = sys.stdin.read() 
print(problem) 

