import requests


# -- Getting Quiz Data --
qns_res = requests.get(url='https://opentdb.com/api.php?amount=10&type=boolean')
qns_res.raise_for_status()

question_data = qns_res.json()['results']


