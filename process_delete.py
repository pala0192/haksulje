#!C:\Python312\python.exe
import cgi, os
form = cgi.FieldStorage()
pageId=form["pageId"].value

os.remove('databox/'+pageId)
os.remove('databox_image/'+pageId)
print("Location: test.py?psadhfhwourasdfhiuiwrfuysiaufhodisufhihjkasdfhl=1")
print()
