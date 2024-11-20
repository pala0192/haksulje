#!C:\Python312\python.exe

# -*- coding: euc-kr -*-
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
print("content-type:text/html; charset=UTF-8\n")

print()

import cgi, os

file= os.listdir('update')

form = cgi.FieldStorage()

listStr = ''
for item in file:
    listStr = listStr+'<li><a href="update_check.py?id={it}&psadhfhwourasdfhiuiwrfuysiaufhodisufhihjkasdfhl=1">{it}</a></li>'.format(it=item)
if 'psadhfhwourasdfhiuiwrfuysiaufhodisufhihjkasdfhl' in form:
  if  'id' in form:
      pageId = form["id"].value
      content = open('update/'+pageId, 'r',encoding='utf-8')
      content= content.readlines()
      title=content[0]
      title=title.replace("\n","")
      description = content[1]
      description = description.replace("<","&lt;")
      description = description.replace(">","&gt;")

      delete_action='''
        <form action="process_update_delete.py" method="post">
          <input type="hidden" name="pageId" value="{0}">
          <input type="submit" value="delete" style="width:17%; height:60px; font-size:170%">
        </form>
      '''.format(pageId)
      transmit_action='''
        <form action="process_update_transmit.py" method="post">
          <input type="hidden" name="pageId" value="{pageId}">
          <input type="hidden" name="description" value="{description}">
          <input type="hidden" name="title" value="{title}">
          <input type="submit" value="approval" style="width:17%; height:60px; font-size:170%">
        </form>
      '''.format(pageId=pageId,description=description,title=title)

  else : 
      pageId = '현재 문서가 없습니다'
      content=''
      title=''
      description = '~ ~ ~'
      delete_action=''
      transmit_action=''


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
      <h1 style="text-align: center;"><div style="font-size:200%">업데이트 관리자 창</div>
      </h1>
    </div>
    <br>
    <br>
    
    <div style="margin:1%; padding:4%; border:4px black solid;">
      
      <div style="border-bottom:solid 2px; padding:1%;">
        <h2 style="font-size:300%; display:inline;">{pageId}</h2>
      </div>
      <p style="font-size:300%">{title}</p>
      <p style="font-size:150%">{desc}</p>

    </div>
    
    
    <div style="padding:3%;border:black solid 2px;margin-left:1%">
      <h3 style="font-size:300%;">contents</h3>
      <ol style="font-size:100%;padding:1%";>{listStr}</ol>
    </div>
    <br>
    
    <div style="padding:1%">
      
      <br>
      
      <h5 style="font-size:200%; text-align: center;">delete
      {delete_action}{transmit_action}
      </h5>
      <br>
    </div>
    <br>  
    <br>
    <br>
    <br>  
    <br>
    
    <li style="font-size:300%;margin-left:2%"><a href="test.py?psadhfhwour=1">관리자창 가기</a></li>
</body>
</html>
      '''.format(pageId=pageId,title=title, desc= description, listStr=listStr, delete_action=delete_action,
      transmit_action=transmit_action))