#! /usr/bin/python
import requests
import conts as conts


class RiotAPI(object):

	def __init__(self,api_key,regions=conts.REGIONS['North_America']):
		self.api_key = api_key
		self.region = regions

	def _request(self,api_url,params={}):
		args = {'api_key':self.api_key}
		for key, value in params.items():
			if key not in args:
				args[key] = value
				print(key+"ASDASD"+"\n"+value)
			response = requests.get(
				conts.URL['base'].format(
					proxy=self.region,
					region=self.region,
					url=api_url
					),
			params=args
			)
			print response.url
			return response.json()	

	def get_summoner_by_name(self,name):
		api_url = (conts.URL['summoner_by_name']).format(
			version=conts.API_VERSIONS['summoner'],
			names=name
			)
		return self._request(api_url,conts.API_VERSIONS)
	
	def get_stats_by_name(self,name):
		a = self.get_summoner_by_name(name)
	 	b = a[name.lower()]
		c = b['id']
		api_url = (conts.URL['stats_by_id']).format(
			version=conts.API_VERSIONS['stats'],
			names = c
			)+'?api_key=RGAPI-9F0BFC59-A908-4A21-8032-901C0E8AFB31'
		print api_url
		URL = conts.URL['base'].format(
				proxy=self.region,
				region=self.region,
				url=api_url
				)
		return requests.get(URL).json()


