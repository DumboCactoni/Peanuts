import sys
print("prevstarttime numberper timeper; questions")
input = sys.stdin.read().strip().split('\n')
info=[int(indice) for indice in input[0].split()]
currnumber=0; starttime=info[0]; questions=[]
for indice in input[1:]:
	for question in indice.split(','):
		questions.append(question)
questions += ["0" for _ in range(10)]
info.append(len(questions)-10)
while True:
	currnumber+=info[1]; starttime+=info[2]
	if str(starttime)[-2]=="6":
		starttime+=40

	currlist=[questions[indice] for indice
	in range(currnumber-info[1], currnumber)]
	print("- [ ]", starttime,
	" ".join(currlist))
	if currnumber >= info[-1]:
                print(currnumber)
                break
