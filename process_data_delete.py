#!C:\Python312\python.exe
import cgi, os
form = cgi.FieldStorage()
pageId=form["pageId"].value

os.remove('passed_document/'+pageId)
os.remove('passed_image/'+pageId)
print("Location: data.py?psadhfhwourasdfhiuiwrfuysiaufhodisufhihjkasdfhl=1")
print()