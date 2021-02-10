#!/usr/bin/env python3
# This script is called from the page all_users.hmtl, when the user clicks on the 'Find Friends' button.
# It reads the data the user typed into the form.
# Then, it searches the database for records (other users) that are in the appropriate age range.
# Finally, it creates a webpage with all the users retrieved from the database.


# useful for debugging
import cgitb
cgitb.enable()

import urllib.parse

import cgi
form = cgi.FieldStorage()

# Read the minimum and maximum ages that the user typed into the form 
lower_limit = urllib.parse.quote(form.getvalue('lower_limit'))
upper_limit = urllib.parse.quote(form.getvalue('upper_limit'))

# Connect to the database
import sqlite3

conn = sqlite3.connect('people.db')
c = conn.cursor()

# Print the webpage for display to the user
print('Content-type:text/html')
print()
print('<html>')
print('<head>')
print('<title>Users in proper age range</title>')
print('<link rel="stylesheet" type="text/css" href="../cmt118.css">')
print('</head>')

print('<body>')
print('<p>We found the following users whose age is between ' + lower_limit + ' and ' + upper_limit + ':</p>')
# print out the data for users whose age is within the limits.
for result in c.execute('select name,age,image from users where age>=' + lower_limit + ' and age<=' + upper_limit + ';'):
    their_name = result[0]
    their_age = result[1]
    their_image = result[2]

    print('<img src="' + their_image + '"/>')
    print(their_name + ' is ' + str(their_age) + ' years old.</p>')
    print('<hr/>')
conn.close()
print('</body>')
print('</html>')

