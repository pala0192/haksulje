#!C:\Python312\python.exe
import cgi, os
form = cgi.FieldStorage()
num_name=form["num_name"].value

os.remove('message/'+num_name)
print("Location: message.py?psadhfhwourasdfhiuiwrfuysiaufhodisufhihjkasdfhl=1")
print()

