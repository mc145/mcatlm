import sys 
import os 
problem_subject = input("What subject is this problem from (geometry, algebra, number theory, or combinatorics?\n")
difficulty = int(input("What is the difficulty of this problem in your rating scale?\n")) 
subject_matter = input("What is the subject matter of this problem (i.e. homethety, totient function)? \n")
year_attempted = int(input("What year did you most recently attempt this problem?\n"))

contest_problem = input("What contest problem is this?\n")
contest = input("What contest is this problem from?\n")
print("_________________________________________________________________\n")
print("Insert Problem (in LaTeX) \n")
problem = sys.stdin.read() 
print("_________________________________________________________________\n")
print("Insert Solution (in LaTeX) \n")
solution = sys.stdin.read() 

# store problem as [contest.tex] 

os.system("add.sh") 


problem_file = open("problem" + contest_problem + ".tex", "x")
problem_file.write(problem) 

if(solution != ""):
    solution_file = open("solution" + contest_problem + ".tex", "x")
    solution_file.write(solution)


# Created list of different contests in contest.txt 
#__________________________________________________________________
current_contests = open("contest.txt", "r") 
current_contests_line = current_contests.readline().strip() 
add_contest = True
while(current_contests_line != ''):
    if(current_contests_line == contest):
         add_contest = False
    current_contests_line = current_contests.readline().strip() 

current_contests_read = open("contest.txt", "r") 
current_contest_list = current_contests_read.read()

if add_contest == True:
    current_contest_list+='\n'
    current_contest_list+=contest 

current_contests_write = open("contest.txt", "w") 
current_contests_write.write(current_contest_list)

#_________________________________________________________________________











