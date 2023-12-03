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

from flask import Flask,render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy
import sys
import os
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(app.root_path,'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config.from_object(Config)
db=SQLAlchemy(app)
class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20))
class Movie_info(db.Model):
    movie_id=db.Column(db.Integer,primary_key=True)
    movie_name=db.Column(db.String(60))
    release_date=db.Column(db.String(12))
    country=db.Column(db.String(10))
    type=db.Column(db.String(10))
    year=db.Column(db.Integer)
class Actor_info(db.Model):
    actor_id=db.Column(db.Integer,primary_key=True)
    actor_name=db.Column(db.String(30))
    gender=db.Column(db.String(10))
    country=db.Column(db.String(20))
class Relation(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    movie_id=db.Column(db.Integer)
    actor_id=db.Column(db.Integer)
    relation_type=db.Column(db.String(10))
class Movie_box(db.Model):
    movie_id=db.Column(db.Integer,primary_key=True)
    box=db.Column(db.Float(10))

import click
@app.cli.command()
def forge():
    """Generate fake data."""
    db.create_all()
    name='Mia L'
    movies_information=[
        {'movie_id':1001,'movie_name':'战狼2','release_date':'2017-07-27','country':'中国','type':'战争','year':2017},
        {'movie_id':1002,'movie_name':'哪吒之魔童降世','release_date':'2019-07-26','country':'中国','type':'动画','year':2019},
        {'movie_id':1003,'movie_name':'流浪地球','release_date':'2019-02-05','country':'中国','type':'科幻','year':2019},
        {'movie_id':1004,'movie_name':'复仇者联盟4','release_date':'2019-04-24','country':'美国','type':'科幻','year':2019},
        {'movie_id':1005,'movie_name':'红海行动','release_date':'2018-02-16','country':'中国','type':'战争','year':2018},
        {'movie_id':1006,'movie_name':'唐人街探案2','release_date':'2018-02-16','country':'中国','type':'喜剧','year':2018},
        {'movie_id':1007,'movie_name':'我不是药神','release_date':'2018-07-05','country':'中国','type':'喜剧','year':2018},
        {'movie_id':1008,'movie_name':'中国机长','release_date':'2019-09-30','country':'中国','type':'剧情','year':2019},
        {'movie_id':1009,'movie_name':'速度与激情8','release_date':'2017-04-14','country':'美国','type':'动作','year':2017},
        {'movie_id':1010,'movie_name':'西虹市首富','release_date':'2018-07-27','country':'中国','type':'喜剧','year':2018},
        {'movie_id': 1011, 'movie_name': '复仇者联盟3', 'release_date': '2018-05-11', 'country': '美国', 'type': '科幻','year': 2018},
        {'movie_id': 1012, 'movie_name': '捉妖记2', 'release_date': '2018-02-16', 'country': '中国', 'type': '喜剧','year': 2018},
        {'movie_id': 1013, 'movie_name': '八佰', 'release_date': '2020-08-21', 'country': '中国', 'type': '战争','year': 2020},
        {'movie_id': 1014, 'movie_name': '姜子牙', 'release_date': '2020-10-01', 'country': '中国', 'type': '动画','year': 2020},
        {'movie_id': 1015, 'movie_name': '我和我的家乡', 'release_date': '2020-10-01', 'country': '中国', 'type': '剧情','year': 2020},
        {'movie_id': 1016, 'movie_name': '你好，李焕英', 'release_date': '2021-02-12', 'country': '中国', 'type': '喜剧','year': 2021},
        {'movie_id': 1017, 'movie_name': '长津湖', 'release_date': '2021-09-30', 'country': '中国', 'type': '战争','year': 2021},
        {'movie_id': 1018, 'movie_name': '速度与激情9', 'release_date': '2021-05-21', 'country': '中国', 'type': '动作','year': 2021},
    ]
    actors=[{'actor_id':2001,'actor_name':'吴京','gender':'男','country':'中国'},
            {'actor_id':2002,'actor_name':'饺子','gender':'男','country':'中国'},
            {'actor_id':2003,'actor_name':'屈楚萧','gender':'男','country':'中国'},
            {'actor_id':2004,'actor_name':'郭帆','gender':'男','country':'中国'},
            {'actor_id':2005,'actor_name':'乔罗素','gender':'男','country':'美国'},
            {'actor_id':2006,'actor_name':'小罗伯特·唐尼','gender':'男','country':'美国'},
            {'actor_id':2007,'actor_name':'克里斯·埃文斯','gender':'男','country':'美国'},
            {'actor_id':2008,'actor_name':'林超贤','gender':'男','country':'中国'},
            {'actor_id':2009,'actor_name':'张译','gender':'男','country':'中国'},
            {'actor_id':2010,'actor_name':'黄景瑜','gender':'男','country':'中国'},
            {'actor_id':2011,'actor_name':'陈思诚','gender':'男','country':'中国'},
            {'actor_id':2012,'actor_name':'王宝强','gender':'男','country':'中国'},
            {'actor_id':2013,'actor_name':'刘昊然','gender':'男','country':'中国'},
            {'actor_id':2014,'actor_name':'文牧野','gender':'男','country':'中国'},
            {'actor_id':2015,'actor_name':'徐峥','gender':'男','country':'中国'},
            {'actor_id':2016,'actor_name':'刘伟强','gender':'男','country':'中国'},
            {'actor_id':2017,'actor_name':'张涵予','gender':'男','country':'中国'},
            {'actor_id':2018,'actor_name':'F·加里·格雷','gender':'男','country':'美国'},
            {'actor_id':2019,'actor_name':'范·迪塞尔','gender':'男','country':'美国'},
            {'actor_id':2020,'actor_name':'杰森·斯坦森','gender':'男','country':'美国'},
            {'actor_id':2021,'actor_name':'闫非','gender':'男','country':'中国'},
            {'actor_id':2022,'actor_name':'沈腾','gender':'男','country':'中国'},
            {'actor_id':2023,'actor_name':'安东尼·罗素','gender':'男','country':'美国'},
            {'actor_id':2024,'actor_name':'克里斯·海姆斯沃斯','gender':'男','country':'美国'},
            {'actor_id':2025,'actor_name':'许诚毅','gender':'男','country':'中国'},
            {'actor_id':2026,'actor_name':'梁朝伟','gender':'男','country':'中国'},
            {'actor_id':2027,'actor_name':'白百何','gender':'女','country':'中国'},
            {'actor_id':2028,'actor_name':'井柏然','gender':'男','country':'中国'},
            {'actor_id':2029,'actor_name':'管虎','gender':'男','country':'中国'},
            {'actor_id':2030,'actor_name':'王千源','gender':'男','country':'中国'},
            {'actor_id':2031,'actor_name':'姜武','gender':'男','country':'中国'},
            {'actor_id':2032,'actor_name':'宁浩','gender':'男','country':'中国'},
            {'actor_id':2033,'actor_name':'葛优','gender':'男','country':'中国'},
            {'actor_id':2034,'actor_name':'范伟','gender':'男','country':'中国'},
            {'actor_id':2035,'actor_name':'贾玲','gender':'女','country':'中国'},
            {'actor_id':2036,'actor_name':'张小斐','gender':'女','country':'中国'},
            {'actor_id':2037,'actor_name':'陈凯歌','gender':'男','country':'中国'},
            {'actor_id':2038,'actor_name':'徐克','gender':'男','country':'中国'},
            {'actor_id':2039,'actor_name':'易烊千玺','gender':'男','country':'中国'},
            {'actor_id':2040,'actor_name':'林诣彬','gender':'男','country':'美国'},
            {'actor_id':2041,'actor_name':'米歇尔·罗德里格兹','gender':'女','country':'美国'},
            ]
    movie_box=[{'movie_id':1001,'box':56.84},
               {'movie_id':1002,'box':50.15},
               {'movie_id': 1003, 'box': 46.86},
               {'movie_id': 1004, 'box': 42.5},
               {'movie_id': 1005, 'box': 36.5},
               {'movie_id': 1006, 'box': 33.97},
               {'movie_id': 1007, 'box': 31},
               {'movie_id':1008,'box':29.12},
               {'movie_id': 1009, 'box': 26.7},
               {'movie_id': 1010, 'box': 25.47},
               {'movie_id': 1011, 'box': 23.9},
               {'movie_id': 1012, 'box': 22.37},
               {'movie_id': 1013, 'box': 30.10},
               {'movie_id': 1014, 'box': 16.02},
               {'movie_id': 1015, 'box': 28.29},
               {'movie_id': 1016, 'box': 54.13},
               {'movie_id': 1017, 'box': 53.48},
               {'movie_id': 1018, 'box': 13.92},
               ]
    relation=[{'id':1,'movie_id':1001,'actor_id':2001,'relation_type':'主演'},
              {'id':2, 'movie_id':1001, 'actor_id':2001, 'relation_type':'导演'},
              {'id':3, 'movie_id':1002, 'actor_id':2002, 'relation_type':'导演'},
              {'id':4, 'movie_id':1003, 'actor_id':2001, 'relation_type':'主演'},
              {'id':5, 'movie_id':1003, 'actor_id':2003, 'relation_type':'主演'},
              {'id':6, 'movie_id':1003, 'actor_id':2004, 'relation_type':'导演'},
              {'id':7, 'movie_id':1004, 'actor_id':2005, 'relation_type':'导演'},
              {'id':8, 'movie_id':1004, 'actor_id':2006, 'relation_type':'主演'},
              {'id':9, 'movie_id':1004, 'actor_id':2007, 'relation_type':'主演'},
              {'id':10,'movie_id': 1005,'actor_id':2008, 'relation_type':'导演'},
              {'id':11, 'movie_id':1005,'actor_id':2009, 'relation_type':'主演'},
              {'id':12,'movie_id': 1005,'actor_id':2010, 'relation_type':'主演'},
              {'id':13,'movie_id': 1006,'actor_id':2011, 'relation_type':'导演'},
              {'id':14,'movie_id': 1006, 'actor_id':2012,'relation_type': '主演'},
              {'id':15,'movie_id': 1006, 'actor_id':2013,'relation_type': '主演'},
              {'id':16,'movie_id': 1007, 'actor_id':2014,'relation_type': '导演'},
              {'id':17,'movie_id': 1007, 'actor_id':2015,'relation_type': '主演'},
              {'id':18,'movie_id': 1008, 'actor_id':2016, 'relation_type':'导演'},
              {'id':19,'movie_id': 1008, 'actor_id':2017, 'relation_type':'主演'},
              {'id':20,'movie_id': 1009, 'actor_id':2018, 'relation_type':'导演'},
              {'id':21,'movie_id': 1009, 'actor_id':2019, 'relation_type':'主演'},
              {'id':22,'movie_id': 1009, 'actor_id':2020, 'relation_type':'主演'},
              {'id':23,'movie_id': 1010, 'actor_id':2021, 'relation_type':'导演'},
              {'id':24,'movie_id': 1010, 'actor_id':2022, 'relation_type':'主演'},
              {'id':25,'movie_id': 1011, 'actor_id':2023, 'relation_type':'导演'},
              {'id':26,'movie_id': 1011, 'actor_id':2006, 'relation_type':'主演'},
              {'id':27,'movie_id': 1011, 'actor_id':2024, 'relation_type':'主演'},
              {'id':28,'movie_id': 1012, 'actor_id':2025, 'relation_type':'导演'},
              {'id':29,'movie_id': 1012, 'actor_id':2026, 'relation_type':'主演'},
              {'id':30,'movie_id': 1012, 'actor_id':2027, 'relation_type':'主演'},
              {'id':31,'movie_id': 1012, 'actor_id':2028, 'relation_type':'主演'},
              {'id':32,'movie_id': 1013, 'actor_id':2029, 'relation_type':'导演'},
              {'id':33,'movie_id': 1013, 'actor_id':2030, 'relation_type':'主演'},
              {'id':34,'movie_id': 1013, 'actor_id':2009, 'relation_type':'主演'},
              {'id':35,'movie_id': 1013, 'actor_id':2031, 'relation_type':'主演'},
              {'id':36,'movie_id': 1015, 'actor_id':2032, 'relation_type':'导演'},
              {'id':37,'movie_id': 1015, 'actor_id':2015, 'relation_type':'导演'},
              {'id':38, 'movie_id':1015, 'actor_id':2011, 'relation_type':'导演'},
              {'id':39, 'movie_id':1015, 'actor_id':2015, 'relation_type':'主演'},
              {'id':40, 'movie_id':1015, 'actor_id':2033, 'relation_type':'主演'},
              {'id':41, 'movie_id':1015, 'actor_id':2034, 'relation_type':'主演'},
              {'id':42, 'movie_id':1016, 'actor_id':2035, 'relation_type':'导演'},
              {'id':43, 'movie_id':1016, 'actor_id':2035, 'relation_type':'主演'},
              {'id':44, 'movie_id':1016, 'actor_id':2036, 'relation_type':'主演'},
              {'id':45, 'movie_id':1016, 'actor_id':2022, 'relation_type':'主演'},
              {'id':46, 'movie_id':1017, 'actor_id':2037, 'relation_type':'导演'},
              {'id':47, 'movie_id':1017, 'actor_id':2038, 'relation_type':'导演'},
              {'id':48, 'movie_id':1017, 'actor_id':2008, 'relation_type':'导演'},
              {'id':49, 'movie_id':1017, 'actor_id':2001, 'relation_type':'主演'},
              {'id':50, 'movie_id':1017, 'actor_id':2039, 'relation_type':'主演'},
              {'id':51, 'movie_id':1018, 'actor_id':2040, 'relation_type':'导演'},
              {'id':52, 'movie_id':1018, 'actor_id':2019, 'relation_type':'主演'},
              {'id':53, 'movie_id':1018, 'actor_id':2041, 'relation_type':'主演'},
              ]
    user=User(name=name)
    db.session.add(user)
    for m in movies_information:
        movie_info=Movie_info(movie_id=m['movie_id'],movie_name=m['movie_name'],release_date=m['release_date'],country=m['country'],type=m['type'],year=m['year'])
        db.session.add(movie_info)
    for a in actors:
        actor=Actor_info(actor_id=a['actor_id'],actor_name=a['actor_name'],gender=a['gender'],country=a['country'])
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

@app.route('/')
def index():
    user=User.query.first()
    movies_information=Movie_info.query.all()
    actors=Actor_info.query.all()
    box=Movie_box.query.all()
    relation=Relation.query.all()
    return render_template('index.html',user=user,movies_information=movies_information,actors=actors,box=box,relation=relation)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
