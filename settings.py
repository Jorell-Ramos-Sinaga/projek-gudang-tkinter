from json import load, dump
import json

class Settings:

	def __init__(self):

		#APP CONF
		self.title = "Database App"


		#WINDOW CONF
		base = 60
		ratio = (16, 9)
		self.width = base*ratio[0]
		self.height = base*ratio[1]
		self.screen = f"{self.width}x{self.height}+1000+400"


		#IMG CONF
		self.logo = "img/logo.jpg"
		self.users_path = "users.json"

		#DATABASE
		self.load_data_from_json()
		self.data_counter = self.load_data_counter()

	#LOAD & SAVE JSON DATA

	def load_data_from_json(self):
		with open("data/database.json", "r") as file_json:
			self.database = load(file_json)

	def save_data_to_json(self):
		with open("data/database.json", "w") as file_json:
			dump(self.database, file_json, default=str)

	def load_userData(self, path):
		with open(path, "r") as json_data:
			data = json.load(json_data)
		return data

	def load_data_counter(self):
		with open("data/counter.json", "r") as json_data:
			self.data_counter = load(json_data)
		return self.data_counter

	def save_data_counter(self):
		with open("data/counter.json", "w") as json_data:
			dump(self.data_counter, json_data)

	#LOGIN