import requests
from key import API_KEY
import time

class VGR():
	def __init__(self):
		self.games = []
		self.headers = {"X-Mashape-Key": API_KEY, "Accept": "application/json"}

	def user_search(self):
		user_input = raw_input("Search for a game title (e.g. 'metroid'): ")
		print "\n"
		search_url_format = "https://igdbcom-internet-game-database-v1.p.mashape.com/games/?fields=name&limit=10&offset=0&search={}".format(user_input)
		response = requests.get(search_url_format, headers=self.headers)

		info = response.json()
		count = 1
		for game in info:
			print str(count) + ". " + str(game["name"])
			if game["id"] not in self.games:
				self.games.append(game["id"])
			count += 1

		print "\n"
		selection = raw_input("Use the numpad to select your game: ")
		print "\n"

		self.game_lookup(self.games[int(selection)-1])

	def game_lookup(self, code):
		game_url_format = "https://igdbcom-internet-game-database-v1.p.mashape.com/games/{}?fields=*".format(code)
		response = requests.get(game_url_format, headers=self.headers)

		info = response.json()

		self.genre_scrape(info[0]['genres'])

	def genre_scrape(self, genres):
		genre = ','.join(map(str, genres)) 
		ranking_url_format = "https://igdbcom-internet-game-database-v1.p.mashape.com/genres/{}?fields=*".format(genre)
		response = requests.get(ranking_url_format, headers=self.headers)

		info = response.json()

		print info
	
if __name__ == '__main__':
	test = VGR()
	test.user_search()