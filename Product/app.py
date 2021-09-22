from flask import Flask, render_template
import routes as r

# 플라스크 객체 생성
app = Flask(__name__)

# 블루프린트 객체 등록
app.register_blueprint(r.prod_bp)
app.register_blueprint(r.store_bp)
app.register_blueprint(r.price_bp)
app.register_blueprint(r.standard_bp)

@app.route('/')
def root():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()



