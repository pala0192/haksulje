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
listStr = ''
for item in file:
    listStr = listStr+'<li><a href="data.py?psadhfhwourasdfhiuiwrfuysiaufhodisufhihjkasdfhl=1&id={it}">{it}</a></li>'.format(it=item)


form = cgi.FieldStorage()

if 'psadhfhwourasdfhiuiwrfuysiaufhodisufhihjkasdfhl' in form:
    if  'id' in form:
        pageId = form["id"].value
        description = open('passed_document/'+pageId, 'r',encoding='utf-8').read()
        description = description.replace("<","&lt;")
        description = description.replace(">","&gt;")
        if os.path.isfile('passed_image/{}'.format(pageId)) :
            image_link=open('passed_image/{}'.format(pageId), 'r',encoding='utf-8').read()
        else: image_link=''
        delete_action='''
            <form action="process_data_delete.py" method="post">
            <input type="hidden" name="pageId" value="{0}">
            <input type="submit" value="delete" style="width:17%; height:60px; font-size:280%">
            </form>
        '''.format(pageId)

    else : 
        pageId = '선택중인 문서가 없습니다'
        description = '문서를 삭제하시려면 문서를 선택해주세요'
        image_link=''
        delete_action=''


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
      <h1 style="text-align: center;"><div style="font-size:320%">데이터 관리</div>
      <div style="font-size:280%">-(삭제) 기능-</div>
      </h1>
    </div>
    <br>
    <br>
    
    <div style="margin:1%; padding:4%;border:4px black solid">
      
      <div style="border-bottom:solid 2px; padding:1%;">
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
    <br>
    <br>
    <br>
    <div style="text-align: center;">
        <h5 style="font-size:200%; margin:0%">문서 업데이트 승인/비승인(삭제)</h5>
        {delete_action}
    </div>
    <br>  
    <br>
    <br>
    <br>  
    <br>
    
    <li style="font-size:300%;margin-left:2%;"><a href="test.py?psadhfhwour=1">관리자창 가기</a></li>
</body>
</html>
      '''.format(title=pageId, desc= description, listStr=listStr,img_link=image_link,delete_action=delete_action))