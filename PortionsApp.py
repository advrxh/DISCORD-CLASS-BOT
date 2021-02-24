from sys import exit
import sys, pprint, os

from studentProfileHandler import ReturnPortionsSpecific

# subject = sys.argv[1]

subject = input("\nSubject :")

subjectCodes = {
	"-m" : "mathematics",
	"-c" : "chemistry",
	"-b" : "biology",
	"-p" : "physics",
	"-h" : "history",
	"-e" : "economics",
	"-g" : "geography",
	"-ci" : "civics",
	"-hi" : "hindi",
	"-en" : "english"
}

subjectCodeIndex =["-m", "-c", "-b", "-p", "-h", "-e", "-g", "-ci", "-hi","-en" ]
state = False

def TutOpen(subject):
	os.system(f'start https://youtube.com/results?search_query=edumantra+{subject.replace(" ", "+")}')

for code in subjectCodeIndex:
	if subject == code:
		portions = ReturnPortionsSpecific(subjectCodes[code])
		portions = list(portions.values())
		for i, lesson in enumerate(portions):
			print("Lesson-" + str(i+1) + ': ' + str(lesson))
		index = int(input("\nEnter the index no of the lesson to open the tutorial:"))
		TutOpen(portions[index-1])
		exit()
	else:
		continue




