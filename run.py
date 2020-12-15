# -*- coding: utf-8 -*-
# 기본 템플릿
import os
from flask import Flask, render_template, request, redirect, url_for, session
from flask import jsonify

from flask_socketio import SocketIO

app = Flask(__name__)
# 세션처리
app.secret_key = 'sakccsdcocjk2sdjkdskcj'
# [2] 시크릿키 지정 (환경변수)
app.config['SECRET_KEY'] = '12341234' #  비밀번호
# [3] SocketIO 생성시 Flask 객체를 래핑
socketio = SocketIO( app, cors_allowed_origins="*", async_mode='threading' )


@app.route('/')
def home():    
    # 렌더링시 데이터를 전달하고 싶으면 키=값 형태로 파라미터를 추가
    # **kargs
    return render_template('index3.html', name='사용자명')


@app.route('/top')
def top():
    return '상의 페이지'

@app.route('/pants')
def pants():
    return '하의 페이지'

@app.route('/acc')
def acc():
    return '악세서리 페이지'







if __name__ == '__main__':
    #app.run(debug=True)
    # [4] 소켓io를 이용하여 서버가동 (래핑해서 가동)
    socketio.run( app,  debug=True)
