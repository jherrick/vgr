import requests
from key import API_KEY

class VGR(user_input):
	def __init__(self):
		self.games = []
		self.input = user_input
		self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

	def user_search(self, self.input):
		search_url_format = "https://www.giantbomb.com/api/search/?api_key={}&format=json&query={}&resources=game".format(API_KEY, search)
		response = requests.get(search_url_format, headers=self.headers)

		game_lookup(response.json())

	def game_lookup(self, response):
		game_url_format = "https://www.giantbomb.com/api/game/{}/?api_key={}".format(API_KEY, game)

		for game in json["results"]:
			games.append(game["api_detail_url"])

			url_format = "https://www.giantbomb.com/api/game/3030-4725/?api_key={}".format(API_KEY)

#json = response.json()
#print "Search for ... "
#search = "metroid"