#!C:\Python312\python.exe

# -*- coding: euc-kr -*-
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
print("content-type:text/html; charset=UTF-8\n")
print()


print('''<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hanmin wiki making practice</title>
    <link rel="stylesheet" href="front.css">
</head>
<body>
    <br>
    <br>
    <div style="text-align: center;">
        <form action="process_create.py" method="post">
            <p><input type="text" name="title" style="width:90%; font-size:200%" placeholder="name">
            </p>
            <p><textarea rows="20" name="description"
            style="width:90%; font-size:150%" placeholder="description"></textarea></p>
            <p><textarea row="20" name="image_link" style="width:90%; font-size:40%; height=70px" placeholder="image_link"></textarea></p>
            <p><input type="submit"  style="width:90%; font-size:280%"></p>
        </form>
    </div>
    <div style="margin:12%;">
        <h1 style="text-align: center;"><a href="index.py"><span style="font-size:150%">돌아가기</span>
        </a></h1>
    </div>
    <br>
</body>
</html>
    ''')