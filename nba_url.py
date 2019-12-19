import lxml
import requests

url_page = requests.get('http://www.espn.com/nba/players')
url_tree = html.fromstring(page.content)

url = url_tree.xpath('//div//a//*[@class = "small-logos"]')
