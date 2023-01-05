from bs4 import BeautifulSoup
# import lxml


with open("website.html") as file:
    contents = file.read()

# create an object from BeautifulSoup class and provide markup(contents) and parser(html or lxml if it doesn't work)
soup = BeautifulSoup(contents, "html.parser")

# print(soup.title)  # gives title line
# print(soup.title.name)  # gives name of the tag
# print(soup.title.string)  # gives the string within the specified tag
# print(soup.a)  # gives first anchor tag
#
# print(soup.body.h1)  # so basically the contents in the html file can be accessed just like python object

# find_all() function gives all the specified item/elements
# all_anchor_tags = soup.find_all(name="a")  # gives all  the anchor tags whose name is a
# print(all_anchor_tags)

# all_para_tags = soup.find_all(name="p")  # gives all the paragraphs
#
# print(all_para_tags)

all_anchor_tags = soup.find_all(name="a")  # gives all  the anchor tags whose name is a

# for tag in all_anchor_tags:
#     print(tag.get("href"))  # get function gives the value of the attribute
#     print(tag.getText())   # getText() gives the string or text within the tags

# if we want a particular item it can be accessed by specifying attribute or tag name or id name to isolate it
heading = soup.find(id="name", name="h1")  # note this is find while above code has find all
# print(heading)

section_heading = soup.find(name="h3", class_="heading")  # same as above but here class name is specified
# print(section_heading)
# print(section_heading.getText())  # access text within
# print(section_heading.name)  # access name of the tag
# print(section_heading.get("class"))  # to get hold of value of attribute

# to drill deeper into the code and find the exact items we're looking for, css selectors can be used

company_url = soup.select_one(selector="p a")  # looking  te first match of  a sitting inside p
print(company_url)

name = soup.select_one(selector="#name")  # searching by id name id is specified with #
print(name)

headings = soup.select(".heading")  # same as above here class name is specified using .
print(headings)
# main take away is that you can use css selectors to get items from html file




