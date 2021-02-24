import arrow, json, os
from pathlib import Path



def createStudent(name, description):
	studentProfile = {
	"name" : name,
	"dateCreated": arrow.utcnow().format('MMM-DD-YYYY'),
	"timeCreated": arrow.utcnow().format('HH-mm-ss-A'),
	"PortionsCovered" : f"{name}PortionsData.json",
	"notes" : {},
	"description" : str(description)
	}

	studentPortionsData = {
	"name" : f"{name}",
	"chemistry" : list() ,
	"biology" : list(),
	"physics" : list(),
	"history" : list(),
	"economics":list(),
	"geography":list(),
	"civics" : list(),
	"mathematics":list(),
	"hindi":{
	'detail' : list(),
	'nonDetail' :list()
	},
	"english" : {
	'detail' : list(),
	'nonDetail' : list(),
	'poems' : list()
	}
	}

	# dataProfile = open(f'/student-profiles/f{name}PortionsData.json', 'r+')
	# studentProfile = open(f'/student-profiles/f{name}Profile.json', 'r+')

	studentProfile = json.dumps(studentProfile)
	studentPortionsData = json.dumps(studentPortionsData)

	Path(f'{name}Profile.json').touch()
	os.system(f'copy "{name}Profile.json" {os.getcwd()}\\student-profiles')
	os.remove(f'{name}Profile.json')


	with open(f'{os.getcwd()}\\student-profiles\\{name}Profile.json', 'r+') as studentProfileFile:
		studentProfileFile.write(studentProfile)

	Path(f'{name}PortionsData.json').touch()
	os.system(f'copy "{name}PortionsData.json" {os.getcwd()}\\student-profiles')
	os.remove(f'{name}PortionsData.json')

	with open(f'{os.getcwd()}\\student-profiles\\{name}PortionsData.json', 'r+') as studentProfileFile:
		studentProfileFile.write(studentPortionsData)


def ReturnPortionsSpecific(subject):
	with open('portions.json', 'r+', encoding = 'utf-8') as file:
		portions = json.load(file)

		return portions[subject]

def ReturnPortions():
	with open('portions.json', 'r+', encoding = 'utf-8') as file:
		portions = json.load(file)

		return portions



def UpdatePortion(name, subject, subSection,indexNumber):
	
	if subSection is None:
		with open(f'{os.getcwd()}\\student-profiles\\{name}PortionsData.json', 'r+', encoding = 'utf-8') as file:
			
			data = json.load(file)
			data_dict = dict(data)

			# print(data_dict)
		os.remove(f'{os.getcwd()}\\student-profiles\\{name}PortionsData.json')

		Path(f'{name}PortionsData.json').touch()
		os.system(f'copy "{name}PortionsData.json" {os.getcwd()}\\student-profiles')
		os.remove(f'{name}PortionsData.json')


		with open('portions.json', 'r+', encoding='utf-8') as f:
			portionsData = json.load(f)
			data_dict[subject].append(portionsData[subject][str(indexNumber)])

			
			with open(f'{os.getcwd()}\\student-profiles\\{name}PortionsData.json', 'r+', encoding = 'utf-8') as file:
				file.write(str(data_dict).replace("'", '"'))
	else:
		with open(f'{os.getcwd()}\\student-profiles\\{name}PortionsData.json', 'r+', encoding = 'utf-8') as file:
			
			data = json.load(file)
			data_dict = dict(data)
			print('data bfr : ' + str(data_dict))

			# print(data_dict)
		os.remove(f'{os.getcwd()}\\student-profiles\\{name}PortionsData.json')

		Path(f'{name}PortionsData.json').touch()
		os.system(f'copy "{name}PortionsData.json" {os.getcwd()}\\student-profiles')
		os.remove(f'{name}PortionsData.json')

		with open('portions.json', 'r+', encoding='utf-8') as f:
			portionsData = json.load(f)

			data_dict[subject][subSection] = portionsData[subject][subSection][str(indexNumber)]

			with open(f'{os.getcwd()}\\student-profiles\\{name}PortionsData.json', 'r+', encoding = 'utf-8') as file:
				file.write(str(data_dict).replace("'", '"'))

				print('data aftr : ' + str(data_dict))
		 
def CheckStudentExistence(name):
	if os.path.isfile(f'{os.getcwd()}\\student-profiles\\{name}Profile.json'):
		return True
	else:
		return False
# print(list(ReturnPortionsSpecific('mathematics').values()))