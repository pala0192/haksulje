#!C:\Python312\python.exe

# -*- coding: euc-kr -*-
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
print("content-type:text/html; charset=UTF-8\n")

print()

import cgi, os

file= os.listdir('databox')
listStr = ''
for item in file:
    listStr = listStr+'<li><a href="test.py?id={it}&psadhfhwourasdfhiuiwrfuysiaufhodisufhihjkasdfhl=1">{it}</a></li>'.format(it=item)


form = cgi.FieldStorage()

if 'psadhfhwourasdfhiuiwrfuysiaufhodisufhihjkasdfhl' in form:
  if  'id' in form:
      pageId = form["id"].value
      description = open('databox/'+pageId, 'r',encoding='utf-8').read()
      description = description.replace("<","&lt;")
      description = description.replace(">","&gt;")
      delete_action='''
        <form action="process_delete.py" method="post">
          <input type="hidden" name="pageId" value="{0}">
          <input type="submit" value="delete" style="width:17%; height:60px; font-size:280%">
        </form>
      '''.format(pageId)
      
      if os.path.isfile('databox_image/{}'.format(pageId)) :
        image_link=open('databox_image/{}'.format(pageId), 'r',encoding='utf-8').read()
      else: image_link=''
      transmit_action='''
        <form action="process_transmit.py" method="post">
          <input type="hidden" name="pageId" value="{pageId}">
          <input type="hidden" name="description" value="{description}">
          <input type="hidden" name="image_link" value="{image_link}">
          <input type="submit" value="approval" style="width:17%; height:60px; font-size:280%">
        </form>
      '''.format(pageId=pageId,description=description,image_link=image_link)

  else : 
      pageId = '현재 문서가 없습니다'
      description = '~ ~ ~'
      delete_action=''
      image_link=''
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
      <h1 style="text-align: center;"><div style="font-size:320%">관리자 창</div>
      </h1>
    </div>
    <br>
    <br>
    
    <div style="margin:1%; padding:4%;border:4px black solid;">
      
      <div style="padding:1%;">
        <h2 style="font-size:300%; display:inline;">{title}</h2>
      </div>
      
      <p style="font-size:150%">{desc}</p>
      <img src="{img_link}">
      <br>
      <br>
      <br>
      <br>
      
    </div>
    
    <div style="border:black solid 1px; padding:3%;margin-left:1%">
      <h3 style="font-size:300%;">contents</h3>
      <ol style="font-size:100%;padding:1%";>{listStr}</ol>
    </div>
    <div style="padding:1%;text-align: center;">
      <br>
      <h5 style="font-size:200%; margin:0%;margin-left:1%">문서 삭제/승인(문서를 선택해주세요)</h5>
      {delete_action}{transmit_action}
      <br>
    </div>
    <br>
    <br>
    <br>
    <li style="font-size:300%;margin-left:2%"><a href="update_check.py?psadhfhwour=1">업뎃 확인창 가기</a></li>
    <li style="font-size:300%;margin-left:2%"><a href="message.py?psadhfhwour=1">고객의 소리 확인창 가기</a></li>
    </li>
    <li style="font-size:300%;margin-left:2%"><a href="data.py?psadhfhwour=1">데이터센터 가기</a></li>
    </li>
</body>
</html>
      '''.format(title=pageId, desc= description, listStr=listStr, delete_action=delete_action,
      img_link=image_link,transmit_action=transmit_action))