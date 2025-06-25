from flask import Flask, render_template, request, redirect, session
from models import db, User, Event
from database import init_db

app = Flask(__name__)
app.secret_key = 'secreto123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:500195@localhost/eventos_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
init_db(app)

@app.route('/')
def index():
    eventos = Event.query.all()
    return render_template('index.html', eventos=eventos)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = User(nome=request.form['nome'], email=request.form['email'], senha=request.form['senha'])
        db.session.add(user)
        db.session.commit()
        return redirect('/')
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['email'], senha=request.form['senha']).first()
        if user:
            session['user_id'] = user.id
            return redirect('/')
    return render_template('login.html')

@app.route('/evento/<int:id>')
def evento(id):
    evento = Event.query.get_or_404(id)
    return render_template('evento.html', evento=evento)

@app.route('/add_event', methods=['GET', 'POST'])
def add_event():
    if request.method == 'POST':
        titulo = request.form['titulo']
        data = request.form['data']
        local = request.form['local']
        descricao = request.form['descricao']

        novo_evento = Event(titulo=titulo, data=data, local=local, descricao=descricao)
        db.session.add(novo_evento)
        db.session.commit()

        return redirect('/')
    return render_template('add_event.html')

if __name__ == '__main__':
    app.run(debug=True)
