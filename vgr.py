import requests
from key import API_KEY

class VGR():
	def __init__(self):
		self.games = []
		self.headers = {"X-Mashape-Key": API_KEY, "Accept": "application/json"}
		self.genres = []
		self.selection = 0
		self.search = []
		self.recommendations = []

	def user_search(self):
		user_input = raw_input("Search for a game title (e.g. 'metroid'): ")
		print "\n"
		search_url_format = "https://igdbcom-internet-game-database-v1.p.mashape.com/games/?fields=name&limit=10&offset=0&search={}".format(user_input)
		response = requests.get(search_url_format, headers=self.headers)

		info = response.json()
		count = 1
		for game in info:
			print str(count) + ". " + str(game["name"])
			if game["id"] not in self.search:
				self.search.append(game["id"])
			count += 1

		print "\n"
		selection = raw_input("Use the numpad to select your game: ")
		print "\n"

		self.selection = self.search[int(selection)-1]
		self.game_lookup(self.search[int(selection)-1])

	def game_lookup(self, code):
		game_url_format = "https://igdbcom-internet-game-database-v1.p.mashape.com/games/{}?fields=*".format(code)
		response = requests.get(game_url_format, headers=self.headers)

		game_info = response.json()
		self.genres = game_info[0]['genres']

		self.genre_scrape(self.genres)

	def genre_scrape(self, genres):
		genre = ','.join(map(str, genres))
		genre_url_format = "https://igdbcom-internet-game-database-v1.p.mashape.com/genres/{}?fields=*".format(genre)
		response = requests.get(genre_url_format, headers=self.headers)

		genre_info = response.json()
		self.temp = []
		
		print "Your genres are: "

		for x in range(len(self.genres)):
			print genre_info[x]['name']
			for games in genre_info[x]['games']:
				if len(self.genres) == 1:
					self.games.append(games)
				else:
					if games in self.temp:
						self.games.append(games)
					else:
						self.temp.append(games)
		
		print str(len(self.games)) + " games found\n"

		print "Pulling data from servers... Please wait.\n"

		for games in self.games:
			try:
				game_url_format = "https://igdbcom-internet-game-database-v1.p.mashape.com/games/{}?fields=*".format(games)
				response = requests.get(game_url_format, headers=self.headers)

				game_info = response.json()

				rec_score = 0

				rec_score += game_info[0]['rating']

				if game_info[0]['id'] != self.selection:
						self.recommendations.append([game_info[0]['name'], rec_score])
			except KeyError:
				pass

		print "Analysis complete, your game recommendations are: "
		self.recommend()

	def recommend(self):
		self.recommendations.sort(key=lambda item: item[1], reverse=True)
		if len(self.recommendations) == 0:
			print "No games found"
		else:
			for games in range(5):
				print self.recommendations[games][0]

if __name__ == '__main__':
	test = VGR()
	test.user_search()