# Robel

import re
import urllib
import urllib.request as urllib2
from collections import Counter

import requests
from bs4 import BeautifulSoup as bs
from bs4 import *
from urllib.parse import urljoin

url = input("Enter your URL here: ")
depth = int(input("Enter the depth here: "))

response = urllib.request.urlopen(url)
webContent = response.read()
f = open('Webpage.html', 'wb')
f.write(webContent)
f.close

content = open("Webpage.html").read()

soup = bs(webContent, 'lxml')

def crawl(pages, depth=3):
    indexed_url = []  # a list for the main and sub-HTML websites in the main website
    for i in range(depth):
        for page in pages:
            if page not in indexed_url:
                indexed_url.append(page)
                try:
                    c = urllib2.urlopen(page)
                except:
                    print("Could not open %s" % page)
                    continue
                soup = BeautifulSoup(c.read(), 'lxml')
                links = soup('a')  # finding all the sub_links
                for link in links:
                    if 'href' in dict(link.attrs):
                        url = urljoin(page, link['href'])
                        if url.find("'") != -1:
                            continue
                        url = url.split('#')[0]
                        if url[0:4] == 'http':
                            indexed_url.append(url)
        pages = indexed_url
    return indexed_url


pagelist = [url]
urls = crawl(pagelist, depth=depth)
print(urls)
print()

# Task 2:
# identifying email addresses from the webpage and using regex to list them
emails = re.findall(r'([\w\.-]+@[\w\.-]+\.[\w-]{2,5})(?:\.[\w]{2,5})?', content)
print("Emails listed in the webpage are: ")
for email in emails:
    print(email)
print()

# identifying phone numbers from the webpage and using regex to list them
# specifically made for norwegian numbers only
numbers = re.findall(r'(\+47[ -]?\d{8}|\d{2}[ ]\d{2}[ ]\d{2}[ ]\d{2}[ ]|\d{3}[ ]\d{2}[ ]\d{3})', content)
print("Phone numbers listed in the webpage are: ")
for number in numbers:
    print(number)
print()
 # (\+47[ -]?\d{8}|\d{3}[ ]\d{2}[ ]\d{3}|\d{2}[ ]\d{2}[ ]\d{2}[ ]\d{2})


# Task 3
# Identifying comments inside the source with line nr
def search_string_in_file(file_name, string_to_search):
    """Search for the given string in file and return lines containing that string,
    along with line numbers"""
    line_number = 1
    list_of_results = []
    # Open the file in read only mode
    with open('Webpage.html', 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            line_number += 1
            if string_to_search in line:
                # If yes, then add the line number & line as a tuple in the list
                list_of_results.append((line_number, line.rstrip()))
    # Return list of tuples containing line numbers and lines where string is found
    return list_of_results

matched_lines1 = search_string_in_file('Webpage.html', '<!--')      # HTML-comments
matched_lines2 = search_string_in_file('Webpage.html', '// ')       # JavaScript (Css) comments
matched_lines3 = search_string_in_file('Webpage.html', '/*')        # JavaScript (Css) comments
matched_lines = matched_lines1 + matched_lines2 + matched_lines3
print('Total Matched lines : ', len(matched_lines))
for elem in matched_lines:
    print('Line Number = ', elem[0], ' :: Line = ', elem[1])
print()

# Task 4
# Identifying special data using the user provided regular expression
user_input = input("Type your regex here: ")        # it is expecting your input
print("User typed: '{}'. Input type: {}.".format(user_input, type(user_input)))
special_data = re.findall(r"" + user_input, content)
print(special_data)
print()


# Task 5
# We get the words within 'ps''
text_p = (''.join(s.findAll(text=True)) for s in soup.findAll('p'))
c_p = Counter((x.strip().lower() for y in text_p for x in y.split()))
'''
# We get the words within 'divs'
text_div = (''.join(s.findAll(text=True)) for s in soup.findAll('div'))
c_div = Counter((x.strip().lower() for y in text_div for x in y.split()))'''

 # We sum the two counters and get a list with words count from most to less common
total = c_p #c_div +
list_most_common_words = total.most_common(10)
print('Top 10 most common words on the webpage are: ')
for top10 in list_most_common_words:
    print(top10)
