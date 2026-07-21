import sys
sys.stdin = open("main.in","r")
sys.stdout = open("main.txt", "w")
number_of_problems = [44, 47, 28, 21, 25, 21, 21, 31, 21, 21, 26, 32]
current_indice = 0
for chapter_number in range(3,15):
    print("##", chapter_number)
    for question_number in range(1,number_of_problems[current_indice]+1):
        print("- [ ]", question_number)
    current_indice += 1