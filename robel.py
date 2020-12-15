# Task 2:
# identifying email addresses from the source code and using regex to list them
emails = re.findall(r'([\w\.-]+@[\w\.-]+\.[\w-]{2,5})(?:\.[\w]{2,5})?', content)
print("Emails listed in the webpage are: ")
for email in emails:
    print(email)
print()

# identifying phone numbers from the source code and using regex to list them
# specifically made for norwegian numbers only
numbers = re.findall(r'((?:\+47[ -]?\d{8})|\d{2}[ ]\d{2}[ ]\d{2}[ ]\d{2}[ ]?)', content)
print("Phone numbers listed in the webpage are: ")
for number in numbers:
    print(number)
print()

'''
# Task 3
# Identifying comments inside the source code
comment = re.findall(r'<!--(.*) -->', content)
# JavaScript (Css) comments
comments1 = re.findall(r'\/\*[^\n\r]+?(?:\*\)|[\n\r])', content)
comments2 = re.findall(r'\/\/ (?:([^\n\r]+?(?:\*\)|[\n\r])))', content)
comments = comment + comments1 + comments2
for cmt in comments:
    print(cmt)
print()'''

def search_string_in_file(file_name, string_to_search):
    """Search for the given string in file and return lines containing that string,
    along with line numbers"""
    line_number = 1
    list_of_results = []
    # Open the file in read only mode
    with open('UiA.html', 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            line_number += 1
            if string_to_search in line:
                # If yes, then add the line number & line as a tuple in the list
                list_of_results.append((line_number, line.rstrip()))
    # Return list of tuples containing line numbers and lines where string is found
    return list_of_results

matched_lines1 = search_string_in_file('UiA.html', '<!--')      # HTML-comments
matched_lines2 = search_string_in_file('UiA.html', '// ')       # JavaScript (Css) comments
matched_lines3 = search_string_in_file('UiA.html', '/*')        # JavaScript (Css) comments
matched_lines = matched_lines1 + matched_lines2 + matched_lines3
print('Total Matched lines : ', len(matched_lines))
for elem in matched_lines:
    print('Line Number = ', elem[0], ' :: Line = ', elem[1])
print()

# Task 4
# Identifing special data using the user provided regular expression
user_input = input("Type your regex here: ")        # it is expecting your input
print("User typed: '{}'. Input type: {}.".format(user_input, type(user_input)))
special_data = re.findall(" " + user_input, content)
print(special_data)
print()

# Task 5
# We get the words within 'ps''
text_p = (' '.join(s.findAll(text=True)) for s in soup.findAll('p'))
c_p = Counter((x.strip().lower() for y in text_p for x in y.split()))

# We get the words within 'divs'
text_div = (' '.join(s.findAll(text=True)) for s in soup.findAll('div'))
c_div = Counter((x.strip().lower() for y in text_div for x in y.split()))

 # We sum the two counters and get a list with words count from most to less common
total = c_div + c_p
list_most_common_words = total.most_common(10)
print('Top 10 most common words on the webpage are: ')
for top10 in list_most_common_words:
    print(top10)