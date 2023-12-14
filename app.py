import pip
#from flask import Flask, render_template
#app=Flask(__name__)
#@app.route('/')
#@app.route('/index')
#@app.route('/home')
#@app.route('/user/<name>')

#from flask import url_for
#@app.route('/test')
#def test_ur1_for():
#    return 'test page'

#@app.route('/hello')
#def hello():
#    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'
#@app.route('/user/<name>')
#def user_page(name):
#   return 'User:%s' % name
from werkzeug.security import generate_password_hash,check_password_hash
from flask import Flask,render_template,url_for,redirect,flash,request
from config import Config
from flask_sqlalchemy import SQLAlchemy
import sys
import os
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(app.root_path,'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config.from_object(Config)
app.config['SECRET_KEY'] = 'dev'
db=SQLAlchemy(app)
from flask_login import UserMixin
class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20))
    username=db.Column(db.String(20))
    passsword_hash=db.Column(db.String(128))

    def set_password(self,password):
        self.passsword_hash=generate_password_hash(password)

    def validate_password(self,password):
        return check_password_hash(self.passsword_hash,password)
class Movie_info(db.Model):
    movie_id=db.Column(db.String(4),primary_key=True)
    movie_name=db.Column(db.String(60))
    release_date=db.Column(db.String(12))
    movie_country=db.Column(db.String(10))
    type=db.Column(db.String(10))
    year=db.Column(db.String(10))
class Actor_info(db.Model):
    actor_id=db.Column(db.String(4),primary_key=True)
    actor_name=db.Column(db.String(30))
    gender=db.Column(db.String(10))
    actor_country=db.Column(db.String(20))
class Relation(db.Model):
    id=db.Column(db.String(4),primary_key=True)
    movie_id=db.Column(db.String(4))
    actor_id=db.Column(db.String(4))
    relation_type=db.Column(db.String(10))
class Movie_box(db.Model):
    movie_id=db.Column(db.String(4),primary_key=True)
    box=db.Column(db.String(10))

import click
@app.cli.command()
@click.option('--username',prompt=True,help='The username used to login.')
@click.option('--password',prompt=True,hide_input=False,confirmation_prompt=True,help='The password used to login.')
def admin(username,password):
    """Create user."""
    db.create_all()

    user=User.query.first()
    if user is not None:
        click.echo('Updating user...')
        user.username=username
        user.set_password(password)
    else:
        click.echo('Creating user...')
        user=User(username=username,name='Admin')
        user.set_password(password)
        db.session.add(user)

    db.session.commit()
    click.echo('Done.')

from flask_login import LoginManager
login_manager=LoginManager(app)
login_manager.login_view='login'
@login_manager.user_loader
def load_user(user_id):
    user=User.query.get(int(user_id))
    return user
from flask_login import login_user
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        if not username or not password:
            flash('Invalid input.')
            return redirect(url_for('login'))
        user=User.query.first()
        if username==user.username and user.validate_password(password):
            login_user(user)
            flash('Login success.')
            return redirect(url_for('index'))
        flash('Invalid username or password.')
        return redirect(url_for('login'))
    return render_template('login.html')
from flask_login import login_required,logout_user
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Goodbye.')
    return redirect(url_for('index'))

@app.cli.command()
def forge():
    """Generate fake data."""
    db.create_all()
    name='Mia L'
    movies_information=[
        {'movie_id':'1001','movie_name':'战狼2','release_date':'2017/7/27','movie_country':'中国','type':'战争','year':'2017'},
        {'movie_id':'1002','movie_name':'哪吒之魔童降世','release_date':'2019/7/26','movie_country':'中国','type':'动画','year':'2019'},
        {'movie_id':'1003','movie_name':'流浪地球','release_date':'2019/2/5','movie_country':'中国','type':'科幻','year':'2019'},
        {'movie_id':'1004','movie_name':'复仇者联盟4','release_date':'2019/4/24','movie_country':'美国','type':'科幻','year':'2019'},
        {'movie_id':'1005','movie_name':'红海行动','release_date':'2018/2/16','movie_country':'中国','type':'战争','year':'2018'},
        {'movie_id':'1006','movie_name':'唐人街探案2','release_date':'2018/2/16','movie_country':'中国','type':'喜剧','year':'2018'},
        {'movie_id':'1007','movie_name':'我不是药神','release_date':'2018/7/05','movie_country':'中国','type':'喜剧','year':'2018'},
        {'movie_id':'1008','movie_name':'中国机长','release_date':'2019/9/30','movie_country':'中国','type':'剧情','year':'2019'},
        {'movie_id':'1009','movie_name':'速度与激情8','release_date':'2017/4/14','movie_country':'美国','type':'动作','year':'2017'},
        {'movie_id':'1010','movie_name':'西虹市首富','release_date':'2018/7/27','movie_country':'中国','type':'喜剧','year':'2018'},
        {'movie_id':'1011', 'movie_name': '复仇者联盟3', 'release_date': '2018/5/11', 'movie_country': '美国', 'type': '科幻','year': '2018'},
        {'movie_id':'1012', 'movie_name': '捉妖记2', 'release_date': '2018/2/16', 'movie_country': '中国', 'type': '喜剧','year': '2018'},
        {'movie_id': '1013', 'movie_name': '八佰', 'release_date': '2020/8/21', 'movie_country': '中国', 'type': '战争','year': '2020'},
        {'movie_id': '1014', 'movie_name': '姜子牙', 'release_date': '2020/10/01', 'movie_country': '中国', 'type': '动画','year': '2020'},
        {'movie_id': '1015', 'movie_name': '我和我的家乡', 'release_date': '2020/10/01', 'movie_country': '中国', 'type': '剧情','year': '2020'},
        {'movie_id': '1016', 'movie_name': '你好，李焕英', 'release_date': '2021/2/12', 'movie_country': '中国', 'type': '喜剧','year': '2021'},
        {'movie_id': '1017', 'movie_name': '长津湖', 'release_date': '2021/9/30', 'movie_country': '中国', 'type': '战争','year': '2021'},
        {'movie_id': '1018', 'movie_name': '速度与激情9', 'release_date': '2021/5/21', 'movie_country': '中国', 'type': '动作','year': '2021'},
    ]
    actors=[{'actor_id':'2001','actor_name':'吴京','gender':'男','actor_country':'中国'},
            {'actor_id':'2002','actor_name':'饺子','gender':'男','actor_country':'中国'},
            {'actor_id':'2003','actor_name':'屈楚萧','gender':'男','actor_country':'中国'},
            {'actor_id':'2004','actor_name':'郭帆','gender':'男','actor_country':'中国'},
            {'actor_id':'2005','actor_name':'乔罗素','gender':'男','actor_country':'美国'},
            {'actor_id':'2006','actor_name':'小罗伯特·唐尼','gender':'男','actor_country':'美国'},
            {'actor_id':'2007','actor_name':'克里斯·埃文斯','gender':'男','actor_country':'美国'},
            {'actor_id':'2008','actor_name':'林超贤','gender':'男','actor_country':'中国'},
            {'actor_id':'2009','actor_name':'张译','gender':'男','actor_country':'中国'},
            {'actor_id':'2010','actor_name':'黄景瑜','gender':'男','actor_country':'中国'},
            {'actor_id':'2011','actor_name':'陈思诚','gender':'男','actor_country':'中国'},
            {'actor_id':'2012','actor_name':'王宝强','gender':'男','actor_country':'中国'},
            {'actor_id':'2013','actor_name':'刘昊然','gender':'男','actor_country':'中国'},
            {'actor_id':'2014','actor_name':'文牧野','gender':'男','actor_country':'中国'},
            {'actor_id':'2015','actor_name':'徐峥','gender':'男','actor_country':'中国'},
            {'actor_id':'2016','actor_name':'刘伟强','gender':'男','actor_country':'中国'},
            {'actor_id':'2017','actor_name':'张涵予','gender':'男','actor_country':'中国'},
            {'actor_id':'2018','actor_name':'F·加里·格雷','gender':'男','actor_country':'美国'},
            {'actor_id':'2019','actor_name':'范·迪塞尔','gender':'男','actor_country':'美国'},
            {'actor_id':'2020','actor_name':'杰森·斯坦森','gender':'男','actor_country':'美国'},
            {'actor_id':'2021','actor_name':'闫非','gender':'男','actor_country':'中国'},
            {'actor_id':'2022','actor_name':'沈腾','gender':'男','actor_country':'中国'},
            {'actor_id':'2023','actor_name':'安东尼·罗素','gender':'男','actor_country':'美国'},
            {'actor_id':'2024','actor_name':'克里斯·海姆斯沃斯','gender':'男','actor_country':'美国'},
            {'actor_id':'2025','actor_name':'许诚毅','gender':'男','actor_country':'中国'},
            {'actor_id':'2026','actor_name':'梁朝伟','gender':'男','actor_country':'中国'},
            {'actor_id':'2027','actor_name':'白百何','gender':'女','actor_country':'中国'},
            {'actor_id':'2028','actor_name':'井柏然','gender':'男','actor_country':'中国'},
            {'actor_id':'2029','actor_name':'管虎','gender':'男','actor_country':'中国'},
            {'actor_id':'2030','actor_name':'王千源','gender':'男','actor_country':'中国'},
            {'actor_id':'2031','actor_name':'姜武','gender':'男','actor_country':'中国'},
            {'actor_id':'2032','actor_name':'宁浩','gender':'男','actor_country':'中国'},
            {'actor_id':'2033','actor_name':'葛优','gender':'男','actor_country':'中国'},
            {'actor_id':'2034','actor_name':'范伟','gender':'男','actor_country':'中国'},
            {'actor_id':'2035','actor_name':'贾玲','gender':'女','actor_country':'中国'},
            {'actor_id':'2036','actor_name':'张小斐','gender':'女','actor_country':'中国'},
            {'actor_id':'2037','actor_name':'陈凯歌','gender':'男','actor_country':'中国'},
            {'actor_id':'2038','actor_name':'徐克','gender':'男','actor_country':'中国'},
            {'actor_id':'2039','actor_name':'易烊千玺','gender':'男','actor_country':'中国'},
            {'actor_id':'2040','actor_name':'林诣彬','gender':'男','actor_country':'美国'},
            {'actor_id':'2041','actor_name':'米歇尔·罗德里格兹','gender':'女','actor_country':'美国'},
            ]
    movie_box=[{'movie_id':'1001','box':'56.84'},
               {'movie_id':'1002','box':'50.15'},
               {'movie_id': '1003', 'box': '46.86'},
               {'movie_id': '1004', 'box': '42.5'},
               {'movie_id': '1005', 'box': '36.5'},
               {'movie_id': '1006', 'box': '33.97'},
               {'movie_id': '1007', 'box': '31'},
               {'movie_id':'1008','box':'29.12'},
               {'movie_id': '1009', 'box': '26.7'},
               {'movie_id': '1010', 'box': '25.47'},
               {'movie_id': '1011', 'box': '23.9'},
               {'movie_id': '1012', 'box': '22.37'},
               {'movie_id': '1013', 'box': '30.10'},
               {'movie_id': '1014', 'box': '16.02'},
               {'movie_id': '1015', 'box': '28.29'},
               {'movie_id': '1016', 'box': '54.13'},
               {'movie_id': '1017', 'box': '53.48'},
               {'movie_id': '1018', 'box': '13.92'},
               ]
    relation=[{'id':'1','movie_id':'1001','actor_id':'2001','relation_type':'主演'},
              {'id':'2', 'movie_id':'1001', 'actor_id':'2001', 'relation_type':'导演'},
              {'id':'3', 'movie_id':'1002', 'actor_id':'2002', 'relation_type':'导演'},
              {'id':'4', 'movie_id':'1003', 'actor_id':'2001', 'relation_type':'主演'},
              {'id':'5', 'movie_id':'1003', 'actor_id':'2003', 'relation_type':'主演'},
              {'id':'6', 'movie_id':'1003', 'actor_id':'2004', 'relation_type':'导演'},
              {'id':'7', 'movie_id':'1004', 'actor_id':'2005', 'relation_type':'导演'},
              {'id':'8', 'movie_id':'1004', 'actor_id':'2006', 'relation_type':'主演'},
              {'id':'9', 'movie_id':'1004', 'actor_id':'2007', 'relation_type':'主演'},
              {'id':'10','movie_id': '1005','actor_id':'2008', 'relation_type':'导演'},
              {'id':'11', 'movie_id':'1005','actor_id':'2009', 'relation_type':'主演'},
              {'id':'12','movie_id': '1005','actor_id':'2010', 'relation_type':'主演'},
              {'id':'13','movie_id': '1006','actor_id':'2011', 'relation_type':'导演'},
              {'id':'14','movie_id': '1006', 'actor_id':'2012','relation_type': '主演'},
              {'id':'15','movie_id': '1006', 'actor_id':'2013','relation_type': '主演'},
              {'id':'16','movie_id': '1007', 'actor_id':'2014','relation_type': '导演'},
              {'id':'17','movie_id': '1007', 'actor_id':'2015','relation_type': '主演'},
              {'id':'18','movie_id': '1008', 'actor_id':'2016', 'relation_type':'导演'},
              {'id':'19','movie_id': '1008', 'actor_id':'2017', 'relation_type':'主演'},
              {'id':'20','movie_id': '1009', 'actor_id':'2018', 'relation_type':'导演'},
              {'id':'21','movie_id': '1009', 'actor_id':'2019', 'relation_type':'主演'},
              {'id':'22','movie_id': '1009', 'actor_id':'2020', 'relation_type':'主演'},
              {'id':'23','movie_id': '1010', 'actor_id':'2021', 'relation_type':'导演'},
              {'id':'24','movie_id': '1010', 'actor_id':'2022', 'relation_type':'主演'},
              {'id':'25','movie_id': '1011', 'actor_id':'2023', 'relation_type':'导演'},
              {'id':'26','movie_id': '1011', 'actor_id':'2006', 'relation_type':'主演'},
              {'id':'27','movie_id': '1011', 'actor_id':'2024', 'relation_type':'主演'},
              {'id':'28','movie_id': '1012', 'actor_id':'2025', 'relation_type':'导演'},
              {'id':'29','movie_id': '1012', 'actor_id':'2026', 'relation_type':'主演'},
              {'id':'30','movie_id': '1012', 'actor_id':'2027', 'relation_type':'主演'},
              {'id':'31','movie_id': '1012', 'actor_id':'2028', 'relation_type':'主演'},
              {'id':'32','movie_id': '1013', 'actor_id':'2029', 'relation_type':'导演'},
              {'id':'33','movie_id': '1013', 'actor_id':'2030', 'relation_type':'主演'},
              {'id':'34','movie_id': '1013', 'actor_id':'2009', 'relation_type':'主演'},
              {'id':'35','movie_id': '1013', 'actor_id':'2031', 'relation_type':'主演'},
              {'id':'36','movie_id': '1015', 'actor_id':'2032', 'relation_type':'导演'},
              {'id':'37','movie_id': '1015', 'actor_id':'2015', 'relation_type':'导演'},
              {'id':'38', 'movie_id':'1015', 'actor_id':'2011', 'relation_type':'导演'},
              {'id':'39', 'movie_id':'1015', 'actor_id':'2015', 'relation_type':'主演'},
              {'id':'40', 'movie_id':'1015', 'actor_id':'2033', 'relation_type':'主演'},
              {'id':'41', 'movie_id':'1015', 'actor_id':'2034', 'relation_type':'主演'},
              {'id':'42', 'movie_id':'1016', 'actor_id':'2035', 'relation_type':'导演'},
              {'id':'43', 'movie_id':'1016', 'actor_id':'2035', 'relation_type':'主演'},
              {'id':'44', 'movie_id':'1016', 'actor_id':'2036', 'relation_type':'主演'},
              {'id':'45', 'movie_id':'1016', 'actor_id':'2022', 'relation_type':'主演'},
              {'id':'46', 'movie_id':'1017', 'actor_id':'2037', 'relation_type':'导演'},
              {'id':'47', 'movie_id':'1017', 'actor_id':'2038', 'relation_type':'导演'},
              {'id':'48', 'movie_id':'1017', 'actor_id':'2008', 'relation_type':'导演'},
              {'id':'49', 'movie_id':'1017', 'actor_id':'2001', 'relation_type':'主演'},
              {'id':'50', 'movie_id':'1017', 'actor_id':'2039', 'relation_type':'主演'},
              {'id':'51', 'movie_id':'1018', 'actor_id':'2040', 'relation_type':'导演'},
              {'id':'52', 'movie_id':'1018', 'actor_id':'2019', 'relation_type':'主演'},
              {'id':'53', 'movie_id':'1018', 'actor_id':'2041', 'relation_type':'主演'},
              ]
    user=User(name=name)
    db.session.add(user)
    for m in movies_information:
        movie_info=Movie_info(movie_id=m['movie_id'],movie_name=m['movie_name'],release_date=m['release_date'],movie_country=m['movie_country'],type=m['type'],year=m['year'])
        db.session.add(movie_info)
    for a in actors:
        actor=Actor_info(actor_id=a['actor_id'],actor_name=a['actor_name'],gender=a['gender'],actor_country=a['actor_country'])
        db.session.add(actor)
    for b in movie_box:
        box=Movie_box(movie_id=b['movie_id'],box=b['box'])
        db.session.add(box)
    for r in relation:
        rela=Relation(id=r['id'],movie_id=r['movie_id'],actor_id=r['actor_id'],relation_type=r['relation_type'])
        db.session.add(rela)
    db.session.commit()
    click.echo('Done.')

import click
@app.cli.command()
@click.option('--drop',is_flag=True,help='Create after drop.')
def initdb(drop):
    """Initialize the database."""
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')

@app.context_processor
def inject_user():
    user=User.query.first()
    return dict(user=user)
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404
from flask_login import login_required,current_user
@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        if not request.method=='POST':
            return redirect(url_for('index'))
        movie_id=request.form.get('movie_id')
        movie_name=request.form.get('movie_name')
        release_date=request.form.get('release_date')
        movie_country=request.form.get('movie_country')
        type=request.form.get('type')
        year=request.form.get('year')
        actor_id=request.form.get('actor_id')
        actor_name=request.form.get('actor_name')
        gender=request.form.get('gender')
        actor_country=request.form.get('actor_country')
        box=request.form.get('box')
        id=request.form.get('id')
        relation_type=request.form.get('relation_type')
        if movie_id is not None and movie_name is not None and release_date is not None and movie_country is not None and type is not None and year is not None:
            if len(movie_id)>4 or len(movie_name)>60 or len(release_date)>12 or len(movie_country)>10 or len(type)>10 or len(year)>10:
                flash('Invalid input.')
                return redirect(url_for('index'))
            movie_info=Movie_info(movie_id=movie_id,movie_name=movie_name,movie_country=movie_country,release_date=release_date,type=type,year=year)
            db.session.add(movie_info)
            db.session.commit()
        if actor_id is not None and actor_name is not None and gender is not None and actor_country is not None:
            if len(actor_id)>4 or len(actor_name)>30 or len(gender)>10 or len(actor_country)>20:
                flash('Invalid input.')
                return redirect(url_for('index'))
            actor=Actor_info(actor_id=actor_id,actor_name=actor_name,actor_country=actor_country,gender=gender)
            db.session.add(actor)
            db.session.commit()
        if movie_id is not None and box is not None:
            if len(movie_id)>4 or len(box)>10:
                flash('Invalid input.')
                return redirect(url_for('index'))
            box=Movie_box(movie_id=movie_id,box=box)
            db.session.add(box)
            db.session.commit()
        if id is not None and actor_id is not None and movie_id is not None and relation_type is not None:
            if len(id)>4 or len(movie_id)>4 or len(actor_id)>4 or len(relation_type)>10:
                flash('Invalid input.')
                return redirect(url_for('index'))
            relation=Relation(id=id,movie_id=movie_id,actor_id=actor_id,relation_type=relation_type)
            db.session.add(relation)
            db.session.commit()
        flash('Item created.')
        return redirect(url_for('index'))
    user=User.query.first()
    movies_information=Movie_info.query.all()
    actors=Actor_info.query.all()
    box=Movie_box.query.all()
    relation=Relation.query.all()
    return render_template('index.html',user=user,movies_information=movies_information,actors=actors,box=box,relation=relation)

@app.route('/settings',methods=['GET','POST'])
@login_required
def settings():
    if request.method=='POST':
        name=request.form['name']
        if not name or len(name)>20:
            flash('Invalid input')
            return redirect(url_for('settings'))
        current_user.name=name
        db.session.commit()
        flash('Settings updated.')
        return redirect(url_for('index'))
    return render_template('settings.html')

@app.route('/movies_info/m_edit/<int:movie_id>',methods=['GET','POST'])
@login_required
def m_edit(movie_id):
    movies_info = Movie_info.query.get_or_404(movie_id)
    if request.method=='POST':
        movie_id = request.form.get('movie_id')
        movie_name = request.form.get('movie_name')
        release_date = request.form.get('release_date')
        movie_country = request.form.get('movie_country')
        type = request.form.get('type')
        year = request.form.get('year')
        if movie_id is not None and movie_name is not None and release_date is not None and movie_country is not None and type is not None and year is not None:
            if len(movie_id) > 4 or len(movie_name) > 60 or len(release_date) > 12 or len(movie_country) > 10 or len(type) > 10 or len(year) > 10:
                flash('Invalid input.')
                return redirect(url_for('m_edit',movie_id=movie_id))
        movies_info.movie_id=movie_id
        movies_info.movie_name=movie_name
        movies_info.release_date=release_date
        movies_info.movie_country=movie_country
        movies_info.type=type
        movies_info.year=year
        db.session.commit()
        flash('Item updated.')
        return redirect(url_for('index'))
    return render_template('m_edit.html',movies_info=movies_info)
@app.route('/actors_info/a_edit/<int:actor_id>',methods=['GET','POST'])
@login_required
def a_edit(actor_id):
    actors_info = Actor_info.query.get_or_404(actor_id)
    if request.method=='POST':
        actor_id = request.form.get('actor_id')
        actor_name = request.form.get('actor_name')
        gender = request.form.get('gender')
        actor_country = request.form.get('actor_country')
        if actor_id is not None and actor_name is not None and gender is not None and actor_country is not None:
            if len(actor_id)>4 or len(actor_name)>30 or len(gender)>10 or len(actor_country)>20:
                flash('Invalid input.')
                return redirect(url_for('a_edit',actor_id=actor_id))
        actors_info.actor_id=actor_id
        actors_info.actor_name=actor_name
        actors_info.gender=gender
        actors_info.actor_country=actor_country
        db.session.commit()
        flash('Item updated.')
        return redirect(url_for('index'))
    return render_template('a_edit.html',actors_info=actors_info)
@app.route('/relations/r_edit/<int:id>',methods=['GET','POST'])
@login_required
def r_edit(id):
    relations = Relation.query.get_or_404(id)
    if request.method=='POST':
        id = request.form.get('id')
        movie_id=request.form.get('movie_id')
        actor_id=request.form.get('actor_id')
        relation_type = request.form.get('relation_type')
        if id is not None and actor_id is not None and movie_id is not None and relation_type is not None:
            if len(id)>4 or len(movie_id)>4 or len(actor_id)>4 or len(relation_type)>10:
                flash('Invalid input.')
                return redirect(url_for('r_edit',id=id))
        relations.id=id
        relations.movie_id=movie_id
        relations.actor_id=actor_id
        relations.relation_type=relation_type
        db.session.commit()
        flash('Item updated.')
        return redirect(url_for('index'))
    return render_template('r_edit.html',relations=relations)
@app.route('/boxes/b_edit/<int:movie_id>',methods=['GET','POST'])
@login_required
def b_edit(movie_id):
    boxes = Movie_box.query.get_or_404(movie_id)
    if request.method=='POST':
        movie_id=request.form.get('movie_id')
        box = request.form.get('box')
        if movie_id is not None and box is not None:
            if len(movie_id)>4 or len(box)>10:
                flash('Invalid input.')
                return redirect(url_for('b_edit',movie_id=movie_id))
        boxes.movie_id=movie_id
        boxes.box=box
        db.session.commit()
        flash('Item updated.')
        return redirect(url_for('index'))
    return render_template('b_edit.html',boxes=boxes)
@app.route('/movies_info/m_delete/<int:movie_id>',methods=['POST'])
@login_required
def m_delete(movie_id):
    movies_info=Movie_info.query.get_or_404(movie_id)
    db.session.delete(movies_info)
    db.session.commit()
    flash('Item deleted.')
    return redirect(url_for('index'))
@app.route('/actors_info/a_delete/<int:actor_id>',methods=['POST'])
@login_required
def a_delete(actor_id):
    actors_info=Actor_info.query.get_or_404(actor_id)
    db.session.delete(actors_info)
    db.session.commit()
    flash('Item deleted.')
    return redirect(url_for('index'))
@app.route('/relations/r_delete/<int:id>',methods=['POST'])
@login_required
def r_delete(id):
    relations=Relation.query.get_or_404(id)
    db.session.delete(relations)
    db.session.commit()
    flash('Item deleted.')
    return redirect(url_for('index'))
@app.route('/boxes/b_delete/<int:movie_id>',methods=['POST'])
@login_required
def b_delete(movie_id):
    boxes=Movie_box.query.get_or_404(movie_id)
    db.session.delete(boxes)
    db.session.commit()
    flash('Item deleted.')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
