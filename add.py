import sys 
import os 
import shutil 
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






# Created list of different contests in contest.txt 
#__________________________________________________________________
add_contest = True

current_contests = open("contests.txt", "r") 

contest_line = current_contests.readline().strip() 
contest_list = []
while contest_line != '':
    contest_list.append(contest_line) 
    contest_line = current_contests.readline().strip() 

append_contest = ""
for contests in contest_list:
    append_contest+='\n' 
    append_contest+= contests 
    if contests == contest:
        add_contest = False 
if add_contest:
    append_contest+='\n'
    append_contest+=contest 
    contest_write = open("contests.txt", "w") 
    contest_write.write(append_contest) 



#_________________________________________________________________________

if add_contest:
    directory = contest 
    parent_dir = "C:/Users/Akshay Agarwal/Desktop/mcatlm"
    path = os.path.join(parent_dir, directory) 
    os.mkdir(path) 
    problem_file = open("C:/Users/Akshay Agarwal/Desktop/mcatlm/" + contest + "/" + "problem" + contest_problem + ".tex", "x")
    problem_file.write(problem)
    if(solution != ""):
        solution_file = open("C:/Users/Akshay Agarwal/Desktop/mcatlm/" + contest + "/" + "solution" + contest_problem + ".tex", "x")
        solution_file.write(solution)
else: 
    problem_file = open("C:/Users/Akshay Agarwal/Desktop/mcatlm/" + contest + "/" + "problem" + contest_problem + ".tex", "x")
    problem_file.write(problem)
    if(solution != ""):
        solution_file = open("C:/Users/Akshay Agarwal/Desktop/mcatlm/" + contest + "/" + "solution" + contest_problem + ".tex", "x")
        solution_file.write(solution)



    













