from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
'''
def get_page(url):
    try:
        if url == "http://www.udacity.com/cs101x/index.html":
            return ('<html> <body> This is a test page for learning to crawl! '
                    '<p> It is a good idea to '
                    '<a href="http://www.udacity.com/cs101x/crawling.html">learn to '
                    'crawl</a> before you try to  '
                    '<a href="http://www.udacity.com/cs101x/walking.html">walk</a> '
                    'or  <a href="http://www.udacity.com/cs101x/flying.html">fly</a>. '
                    '</p> </body> </html> ')
        elif url == "http://www.udacity.com/cs101x/crawling.html":
            return ('<html> <body> I have not learned to crawl yet, but I '
                    'am quite good at '
                    '<a href="http://www.udacity.com/cs101x/kicking.html">kicking</a>.'
                    '</body> </html>')
        elif url == "http://www.udacity.com/cs101x/walking.html":
            return ('<html> <body> I cant get enough '
                    '<a href="http://www.udacity.com/cs101x/index.html">crawling</a>! '
                    '</body> </html>')
        elif url == "http://www.udacity.com/cs101x/flying.html":
            return ('<html> <body> The magic words are Squeamish Ossifrage! '
                    '</body> </html>')
        elif url == "http://top.contributors/velak.html":
            return ('<a href="http://top.contributors/jesyspa.html">'
                    '<a href="http://top.contributors/forbiddenvoid.html">')
        elif url == "http://top.contributors/jesyspa.html":
            return ('<a href="http://top.contributors/elssar.html">'
                    '<a href="http://top.contributors/kilaws.html">')
        elif url == "http://top.contributors/forbiddenvoid.html":
            return ('<a href="http://top.contributors/charlzz.html">'
                    '<a href="http://top.contributors/johang.html">'
                    '<a href="http://top.contributors/graemeblake.html">')
        elif url == "http://top.contributors/kilaws.html":
            return ('<a href="http://top.contributors/tomvandenbosch.html">'
                    '<a href="http://top.contributors/mathprof.html">')
        elif url == "http://top.contributors/graemeblake.html":
            return ('<a href="http://top.contributors/dreyescat.html">'
                    '<a href="http://top.contributors/angel.html">')
        elif url == "A1":
            return '<a href="B1"> <a href="C1">  '
        elif url == "B1":
            return '<a href="E1">'
        elif url == "C1":
            return '<a href="D1">'
        elif url == "D1":
            return '<a href="E1"> '
        elif url == "E1":
            return '<a href="F1"> '
    except:
        return ""
    return ""


def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote


def union(p, q):
    for e in q:
        if e not in p:
            p.append(e)


def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links


def crawl_web(url, depth):
    if depth == 0:
        return None

    html = urlopen(url)
    soup = bs(html, 'lxml')

    links = soup.findAll


print(crawl_web("http://www.udacity.com/cs101x/index.html", 3))'''

import requests
from bs4 import BeautifulSoup
url = input("Enter your URL: ")

master_request = requests.get(url)
master_soup = bs(master_request.content, 'lxml')
master_atags = master_soup.find_all("a", href=True)
master_links = []
sub_links = {}
for master_atag in master_atags:
    master_href = master_atag.get('href')
    print(master_href)
    master_links.append(master_href)
    sub_request = requests.get(master_href)
    sub_soup = BeautifulSoup(sub_request.content, 'html.parser')
    sub_atags = sub_soup.find_all("a", href=True)
    sub_links[master_href] = []
    for sub_atag in sub_atags:
        sub_href = sub_atag.get('href')
        sub_links[master_href].append(sub_href)
        print("\t"+sub_href)