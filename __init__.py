import random, urllib.request, json, sys, re

from opsdroid.matchers import match_regex
from opsdroid.skill import Skill

usage = ("<pre>Usage: '!tg key=value' or 'value'\ne.g. '!tg highway=steps' or '!tg highway=*' or 'steps'</pre>")

class TagInfo(Skill):
	# match the user input, it can be anywhere, without .* it would have to be at the start of the message which wouldn't work for my matrix-xmpp bridge
	@match_regex(r'.*?!tg (?P<input>.*)', case_sensitive=False)
	async def hello(self, message):
		# get user input
		input_text = message.regex.group('input')
		try: 

			if re.search(r'^help$', input_text):
				await message.respond(usage)

			elif re.search(r' ', input_text):
				await message.respond(usage)

			# when querying wildcard like highway=*
			elif re.search(r'^[a-zA-Z:_]+=\*$', input_text):
				osm_key,osm_value=input_text.split('=')
				text = "<pre>\n### Occurence of " + osm_key + "=" + osm_value + " ###\n\n"
				# get results via taginfo API
				with urllib.request.urlopen("https://taginfo.openstreetmap.cz/api/4/key/values?key=" + osm_key + "&filter=all&lang=cz&sortname=count&sortorder=desc&page=1&rp=10") as url:
					data = json.loads(url.read().decode())
					for element in data['data']:
						# taginfo API returns empty string instead of * on website, so I had to convert it back to * and str.replace() doesn't behave as I expected thus used .re
						text += (element['value'] + " - " + str(element['count']) + "\n")
					# return everything at once as answer to chat
					text += "</pre>"
					await message.respond(text)

			# when querying wildcard like highway=steps
			elif re.search(r'^[a-zA-Z:_]+=[a-zA-Z:_]+$', input_text):
				osm_key,osm_value=input_text.split('=')
				text = "<pre>\n### Occurence of " + osm_key + "=" + osm_value + " ###\n\n"
				# get results via taginfo API
				with urllib.request.urlopen("https://taginfo.openstreetmap.cz/api/4/tag/stats?key=" + osm_key + "&value=" + osm_value) as url:
					data = json.loads(url.read().decode())
					# and feed it to text string, otherwise there's problem with mixing types
					for element in data['data']:
						text += (element['type'] + " - " + str(element['count']) + "\n")

				text += "\n### and most common tag combinations ###\n\n"
				# here we go with another taginofo query
				with urllib.request.urlopen("https://taginfo.openstreetmap.cz/api/4/tag/combinations?key=" + osm_key + "&value=" + osm_value + "&sortorder=desc") as url:
					data = json.loads(url.read().decode())
					for element in data['data']:
						# taginfo API returns empty string instead of * on website, so I had to convert it back to * and str.replace() doesn't behave as I expected thus used .re
						text += (element['other_key'] + ":" + re.sub('^$', ' *', element['other_value']) + " - " + str(element['together_count']) + "\n")
					# return everything at once as answer to chat
					text += "</pre>"
					await message.respond(text)

			# when query singe word i.e. value
			elif re.search(r'^[a-zA-Z:_]+$', input_text):
				osm_value=input_text
				text = "<pre>\n### Occurence of value " + osm_value + " ###\n\n"
				# get results via taginfo API
				with urllib.request.urlopen("https://taginfo.openstreetmap.cz/api/4/search/by_value?query=" + osm_value + "&sortname=count_all&sortorder=desc&page=1&rp=10&format=json_pretty") as url:
					data = json.loads(url.read().decode())
					for element in data['data']:
						# taginfo API returns empty string instead of * on website, so I had to convert it back to * and str.replace() doesn't behave as I expected thus used .re
						text += (element['key'] + " = " + element['value'] + " - " + str(element['count_all']) + "\n")
					# return everything at once as answer to chat
					text += "</pre>"
					await message.respond(text)

			else:
				await message.respond(usage)

		except:
			# if parsing of user params fails give usage info
				await message.respond(usage)
