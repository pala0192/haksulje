#!C:\Python312\python.exe

# -*- coding: euc-kr -*-
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
print("content-type:text/html; charset=UTF-8\n")
print()

import cgi, os

file= os.listdir('passed_document')

def getList():
    file= os.listdir('passed_document')
    listStr = ''
    for item in file:
        listStr = listStr+'<li><a href="index.py?id={it}">{it}</a></li>'.format(it=item)
    return listStr

form = cgi.FieldStorage()


if  'id' in form:
    pageId = form["id"].value
    description = open('passed_document/'+pageId, 'r',encoding='utf-8').read()
    description = description.replace("<","&lt;")
    description = description.replace(">","&gt;")

else : 
    pageId = '업데이트하실 문서를 선택해주세요'
    description = '현제 선택하신 문서가 없습니다.'
    update_link=''

print('''<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hanmin wiki making practice</title>
    <link rel="stylesheet" href="front.css">
</head>
<body>
    <div style="margin:12%;">
      <h1 style="text-align: center;"><div style="font-size:280%">한민 위키</div>
      <div style="color:gray;font-size:160%">한민고 전용 위키피디아</div></h1>
    </div>
    <br>
    <br>
    
    <div style="text-align: center;">
        <form action="process_update.py" method="post">
            <input type="hidden" name="pageId" value="{pageId}">
            <p><input type="text" name="title" style="width:90%; font-size:280%" placeholder="name" value="{pageId}">
            </p>
            <p><textarea rows="20" style="width:90%; font-size:150%" name="description"
            placeholder="description">{description}</textarea></p>
            <p><input type="submit" style="width:90%; height:60px; font-size:280%"></p>
        </form>
    </div>
    
    <div style="border:black solid 1px; padding:3%;margin-left:1%">
        <h3 style="font-size:300%;">contents</h3>
        <ol style="font-size:100%;padding:1%";>{listStr}</ol>
    </div>
</body>
</html>
    '''.format(listStr=getList(), pageId=pageId, description=description))