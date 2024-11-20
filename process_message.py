#!C:\Python312\python.exe

import cgi
form = cgi.FieldStorage()
message=form["message"].value
num_name=form["num_name"].value

opened_file=open('message/'+num_name,'w',encoding='utf-8')
opened_file.write(message)
opened_file.close()

print("Location: index.py")
print()