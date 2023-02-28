from bs4 import BeautifulSoup

# Read the input HTML file
with open('63fcf5c1ddfb9 - 536100channelfull368186.csv', 'r') as file:
    html = file.read()

# Parse the HTML using Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')

# Remove all anchor tags
for anchor in soup.find_all('a'):
    anchor.decompose()

# Remove all video tags
for video in soup.find_all('video'):
    video.decompose()

# Remove all image tags
for img in soup.find_all('img'):
    img.decompose()

# Loop through all the tables in the HTML
for table in soup.find_all('table'):

    # Create a new unordered list element
    ul = soup.new_tag('ul')

    # Loop through each row of the table and create a new list item for each cell
    for row in table.find_all('tr'):
        li = soup.new_tag('li')
        if row.td is not None and row.td.find_next_sibling() is not None:
            li.string = row.td.text + ' ' + row.td.find_next_sibling().text
        elif row.td is not None:
            li.string = row.td.text
        if li.string:
            ul.append(li)

    # Replace the table with the unordered list
    table.replace_with(ul)

# Write the modified HTML to an output file
with open('output.csv', 'w') as file:
    file.write(str(soup))
