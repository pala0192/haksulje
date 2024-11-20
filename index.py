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
    listStr = listStr+'<li><a href="index.py?id={it}">{it}</a></li>'.format(it=item)


form = cgi.FieldStorage()

file_list = []
for files in file:
  file_list.append(files)


file_count_num=0
file_num_and_list={}
file_keys_list = []

for file in file_list:
  file_num_and_list[file]=file_count_num
  file_keys_list.append(file)
  file_count_num=file_count_num+1



if  'id' in form:
    pageId = form["id"].value
    description = open('passed_document/'+pageId, 'r',encoding='utf-8').read()
    description = description.replace("<","&lt;")
    description = description.replace(">","&gt;")
    description = description.replace("\n", "<br>")
    update_link = '<a href="update.py?id={}" style="font-size:200%">문서 편집</a>'.format(pageId)
    file_num = file_num_and_list[pageId]
    if pageId==file_keys_list[0]:
      Previous_file_name=''
      next_file_name=file_keys_list[file_num+1]
    elif pageId==file_keys_list[-1]:
      Previous_file_name=file_keys_list[file_num-1]
      next_file_name=''
    else:
      Previous_file_name=file_keys_list[file_num-1]
      next_file_name=file_keys_list[file_num+1]
    if os.path.isfile('passed_image/{}'.format(pageId)) :
      image_link=open('passed_image/{}'.format(pageId), 'r',encoding='utf-8').read()
    else: image_link=''

else : 
    pageId = '선택중인 문서가 없습니다'
    description = '문서를 열람하시려면 문서를 선택해주세요'
    update_link=''
    file_num = 0
    Previous_file_name=''
    next_file_name=file_keys_list[0]
    image_link=''
    

message_action='''
      <form action="process_message.py" method="post">
        <input type="text" style="width:60%; font-size:180%" name="num_name" placeholder="학번이름(예:21017이서준)">
        <input type="text" style="width:60%; font-size:180%" name="message" placeholder="문의및 신고내용">
        <input type="submit" value="send" style="width:10%; height:40px; font-size:180%">
      </form>
    '''

print('''<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Hanmin wiki making practice</title>
  <link href="front.css" rel="stylesheet">
</head>

<body>
    <div>
        <form action="process_search.py" method="post" style="display: inline;position: relative; right: -72%;">
          <input type="text" name="searchInput" style="width:17%; height:38px; font-size:100%" placeholder="문서 명을 검색하세요">
          <input type="submit" value="제출" style="width:7%; height:38px; font-size:100%">
        </form>
    </div>
    <div style="margin:12%;text-align: center;font-size:330%">
      <h1>한민 위키</h1>
      <h1 style="color:gray;font-size:70%;margin-top:-5%">한민고 전용 위키피디아</h1>
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
      <div style="text-align: center;">
        <a href="index.py?id={Previous_file_name}" style="font-size:150%;">&lt;&lt;&lt;Previous file</a>
        <a href="index.py?id={next_file_name}" style="font-size:150%;">next file&gt;&gt;&gt;</a>
      </div>
    </div>
    <br>
    <div style="text-align: center;">
      <h4 style="font-size:250%; margin:0%">문서 추가하기</h4>
      <a href="create.py" style="font-size:200%">(문서 생성)</a>
      <br>
      <br>
      <br>
      <h4 style="font-size:250%; margin:0%">문서 편집하기(문서를 선택해주세요)</h4>
      {ud_link}
    </div>
    <br>
    <br>
    <br>  
    <br>
    <br>
    
    <div style="padding:1%;margin-left:2%">
      <h4 style="font-size:200%;">고객 문의함</h4>
      {message_action}
    </div>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
</body>
</html>
      '''.format(title=pageId, desc= description, listStr=listStr, ud_link=update_link,
      Previous_file_name=Previous_file_name,next_file_name=next_file_name,message_action=message_action,img_link=image_link))
