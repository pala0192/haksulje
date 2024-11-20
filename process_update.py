#!C:\Python312\python.exe
import cgi
form = cgi.FieldStorage()
pageId=form["pageId"].value
title=form["title"].value
description=form["description"].value
    
opened_file=open('update/'+pageId,'w',encoding='utf-8')
opened_file.write(title+"\n")
opened_file.write(description)
opened_file.close()

print("Location: index.py")
print()
