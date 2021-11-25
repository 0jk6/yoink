#!/usr/bin/python
import sys
import requests


class Steal:
	def __init__(self, url, filename):
		print("-----------------Yoink-----------------")
		self.url = url
		self.filename = filename
		self.path = "D:\\yoinked\\" #you may need to change this path for your PC

		if(self.url == "" or self.filename == ""):
			self.help()
			exit()

	def get(self):
		try:
			print("sending http request to the server...")
			r = requests.get(self.url)
			self.saveFile(r.content)
		except:
			print("Something went wrong...")

	def saveFile(self, content):
		try:
			print(f"saving {self.filename} in the cwd...")
			with open(self.path + self.filename, "wb") as f:
				f.write(content)
				f.close()
			print("DONE!")
			print("---------------------------------------")
		except:
			print("Something went wrong...")

	@staticmethod
	def help():
		print("|-------------------------------------------------|")
		print("|       Yoink = steal files from any website      |")
		print("|-------------------------------------------------|")

		print("|Help: Yoink takes two arguments                  |")
		print("|argv[1] = url with 'https' included in it        |")
		print("|argv[2] = filename                               |")

		print("|-------------------------------------------------|")

try:
	url = sys.argv[1]
	filename = sys.argv[2]
	s = Steal(url, filename)
	s.get()
except Exception as e:
	Steal.help()