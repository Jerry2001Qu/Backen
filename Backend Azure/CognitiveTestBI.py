# 'dataset' holds the input data for this script

import requests
from pprint import pprint
import urllib.request
import urllib
from bs4 import BeautifulSoup
import json

subscription_key = "b5729be1199d4540b1759c630e1fab79"
assert subscription_key

text_analytics_base_url = "https://westcentralus.api.cognitive.microsoft.com/text/analytics/v2.0/"

language_api_url = text_analytics_base_url + "languages"
key_phrase_api_url = text_analytics_base_url + "keyPhrases"

search_term = dataset[0]
search_term = search_term.replace(" ", "%20")

url = 'http://export.arxiv.org/api/query?search_query=all:' + search_term + '&start=0&max_results=1'
data = urllib.request.urlopen(url).read()
parsed_data = BeautifulSoup(data, "html.parser")
print(parsed_data)
summary = parsed_data.find('summary').text
print(summary)

documents = { 'documents': [
    { 'id': '1', 'text': summary
 }
]}

headers   = {'Ocp-Apim-Subscription-Key': subscription_key}
response  = requests.post(key_phrase_api_url, headers=headers, json=documents)
key_phrases = response.json()
pprint(key_phrases)

import wikipedia

wiki_summary = [][]

for i in range(0, len(key_phrases['documents'][0]['keyPhrases'])):
    wiki_search = wikipedia.search(key_phrases['documents'][0]['keyPhrases'][i], results=1)
    print(wiki_search)
    wiki_summary.append(wikipedia.summary(wiki_search[0]))
