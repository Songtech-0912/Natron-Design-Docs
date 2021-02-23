import os
import markdown
from bs4 import BeautifulSoup

# Define markdown files we want to convert
# These should be placed in the order they will come in the final website
# Currently only 2 pages are finished - that's why this list only has 2 items
filenames = ["src/index.md", "src/implementation-guide.md"]

print("Merging files...\n")

# Read markdown files and merge their text content together
merged_filecontent = ""
file = ""
"""
To say the least... this is not semantic or pythonic at all
however it works
so I'm not changing it
"""
for file in filenames:
    file = open(file).read()
    file += "\n \n"
    merged_filecontent += file
print(merged_filecontent)
print("Merge complete!")

# Convert the merged markdown into html
html_filecontent = markdown.markdown(merged_filecontent)

# Print statement below is for debug-only
# print(html_filecontent)

print("Generating HTML from markdown contents...")

# Inject converted HTML into our index.html file
with open("template/index.html", encoding="utf8") as file:
    mainHTML = file.read()

soup = BeautifulSoup(mainHTML, features="html5lib")
markdown_container = soup.select_one("#markdownContentGoesHere")
html_content_beautifulsoup = BeautifulSoup(html_filecontent, "html.parser")
markdown_container.insert(1, html_content_beautifulsoup)

# BeautifulSoup injects utf8 encodings, so we have to decode it
outputHTML = str(soup)

# Write our final html to the doc/ folder, ready to publish with gh-pages
# If the doc/ folder already exists, then delete it

os.system("touch index.html")
with open("index.html", "w") as file:
    file.write(outputHTML)
print("Everything done! Compiled HTML at ./index.html")
