import requests
import re
def getgiflink(url):
    if re.findall(r'https?://tenor.com/view\S+', url):
      tenor_http = requests.get(url)
      direct_link_list = re.findall(r"https?://media1.tenor.com/m\S+.gif", tenor_http.text)
      direct_link = direct_link_list[0]
      return direct_link
    else:
      print("Link is not a tenor link.")
