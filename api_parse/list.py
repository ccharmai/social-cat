import requests

base_url = '127.0.0.1:8000'

class Cat:
	def __init__(self, id, owner, name, sex, age, breed, hair):
		self.id = id
		self.owner = owner
		self.name = name
		self.sex = sex
		self.age = age
		self.breed = breed
		self.hair = hair
		self.owner_name = self.get_owner_name()

	def print(self):
		print('id =', self.id)
		print('owner_id =', self.owner)
		print('owner_name =', self.owner_name)
		print('name =', self.name)
		print('sex =', self.sex)
		print('age =', self.age)
		print('breed =', self.breed)
		print('hair =', self.hair)
		print()

	def get_owner_name(self):
		p = requests.get(url=f'http://{base_url}/api/user/{self.owner}/')
		return p.json()['username']

r = requests.get(url=f'http://{base_url}/api/cats/')
cats = []

i = 0
while True:
	try:
		cd = r.json()[i]
		cat = Cat(cd['id'], cd['owner'], cd['name'], cd['sex'], cd['age'], cd['breed'], cd['hair'])
		cats.append(cat)
	except:
		break
	i += 1

print(f'Найдено {i} котов\n')
for z in range(2):
	cats[z].print()

