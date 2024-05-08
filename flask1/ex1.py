# 파이썬 파일이 직접 스크립트로 실행될 때만 flask 애플리케이션을 실행
from flask import Flask

app = Flask(__name__) ## 현재 모듈의 이름

## 웹에 보여줄 부분
@app.route('/')
def hello_world():
    return ('Hi to the mirror')

## 파이썬 파일을 스크립트로 실행할 때에만 flask 실행
if __name__ == '__main__':
   app.run()

# 
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8000)

# 만약?
if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=8000)
