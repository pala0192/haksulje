#!C:\Python312\python.exe
import cgi,os
form = cgi.FieldStorage()
searchInput=form["searchInput"].value
if os.path.isfile('passed_document/{}'.format(searchInput)) :
    print("Location: index.py?id={}".format(searchInput))
    print()
else:
    print("Location: searchError.py")
    print()
