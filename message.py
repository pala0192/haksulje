#!C:\Python312\python.exe

# -*- coding: euc-kr -*-
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
print("content-type:text/html; charset=UTF-8\n")

print()

import cgi, os

file= os.listdir('message')
listStr = ''
for item in file:
    listStr = listStr+'<li><a href="message.py?num_name={it}&psadhfhwourasdfhiuiwrfuysiaufhodisufhihjkasdfhl=1">{it}</a></li>'.format(it=item)

form = cgi.FieldStorage()
if 'psadhfhwourasdfhiuiwrfuysiaufhodisufhihjkasdfhl' in form:
  if  'num_name' in form:
      num_name = form["num_name"].value
      message = open('message/'+num_name, 'r',encoding='utf-8').read()
      message = message.replace("<","&lt;")
      message = message.replace(">","&gt;")

      delete_action='''
        <form action="process_message_check.py" method="post">
          <input type="hidden" name="num_name" value="{0}">
          <input type="submit" value="delete" style="width:17%; height:60px; font-size:280%">
        </form>
      '''.format(num_name)
  else : 
      num_name = '현제 고객 메시지가 없습니다'
      message = '~ ~ ~'
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
      <h1 style="text-align: center;"><div style="font-size:200%">고객의 소리 관리창</div>
      </h1>
    </div>
    <br>
    <br>
    
    <div style="margin:1%; padding:4%;border:black solid 2px;">
      
      <div style="border-bottom:solid 2px; padding:1%;">
        <h2 style="font-size:200%; display:inline;">{num_name}</h2>
      </div>
      
      <p style="font-size:150%">{message}</p>
      
    </div>
    
    
    <div style="border:black solid 1px; padding:3%;margin-left:1%">
      <h3 style="font-size:200%;">고객의 소리</h3>
      <ol style="font-size:100%;padding:1%";>{listStr}</ol>
    </div>
    <br>
    <div style="text-align: center;">
      <h3 style="font-size:300%;">문의내용 삭제하기</h3>
      {delete_action}
    </div>
    <br>  
    <br>
    <br>
    <br>  
    <br>
    <li style="font-size:300%;margin-left:2%"><a href="test.py?psadhfhwour=1">관리자창 가기</a></li>
</body>
</html>
      '''.format(num_name=num_name, message= message, listStr=listStr, delete_action=delete_action))

