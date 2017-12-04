from urllib.request import Request, urlopen
import json
import webbrowser

def get_user_repos_url():
	url = "https://api.github.com/user"
	token = "112a65ea1b16d630621e81c50e58d1a8f24ba53a"
	request = Request(url)
	request.add_header('Authorization', 'token %s' % token)
	response = urlopen(request)
	text = response.read().decode("utf8")
	n = json.loads(text)
	b = n.get("repos_url")
	return b

def get_user(repos_url):
	url = repos_url
	token = "112a65ea1b16d630621e81c50e58d1a8f24ba53a"
	request = Request(url)
	request.add_header('Authorization', 'token %s' % token)
	response = urlopen(request)
	text = response.read().decode("utf8")
	n = json.loads(text)
	v = []
	for items in range(len(n)):
		dictionary = n[items]
		v.append(dictionary.get("url"))
	return v

def get_all_pulls_url(pulls_url):
	z = []
	for items in range(len(pulls_url)):
		url = pulls_url[items]
		token = "112a65ea1b16d630621e81c50e58d1a8f24ba53a"
		request = Request(url)
		request.add_header('Authorization', 'token %s' % token)
		response = urlopen(request)
		text = response.read().decode("utf8")
		n = json.loads(text)
		w = n.get("pulls_url")
		e = w.replace("{/number}","")
		z.append(e)
	return z

def get_open_pulls_url(pull_url):
	z=[]
	for items in pull_url:
		url = items
		token = "112a65ea1b16d630621e81c50e58d1a8f24ba53a"
		request = Request(url)
		request.add_header('Authorization', 'token %s' % token)
		response = urlopen(request)
		text = response.read().decode("utf8")
		q = json.loads(text)
		e = []
		for items in range(len(q)):
			w = q[items]
			r = w.get("state")
			if r == "open":
				e.append(w.get("html_url"))
	return e

def open_link(links):
	for items in links:
		webbrowser.open(items)

all_links = get_open_pulls_url(get_all_pulls_url(get_user(get_user_repos_url())))
open_link(all_links)
