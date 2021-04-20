from flask import Flask , render_template,request , redirect , url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)




	
    

#app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://postgres:July@2000@localhost/post'
app.config['SQLALCHEMY_DATABASE_URI']="postgres://fwgvstauthdxim:3f02ea8034c81addcd66e961e63a38a4d04facadb120e3ffb281ba0529b92bbc@ec2-35-174-35-242.compute-1.amazonaws.com:5432/d3dfmgieu67eo0"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False





db=SQLAlchemy(app)

class Favposts(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	image=db.Column(db.String(500))
	heading=db.Column(db.String(30))
	paragraph=db.Column(db.String(2000))


@app.route('/')
def index():
	result=Favposts.query.all()
	
	return render_template("index.html", result=result)


@app.route('/quotes')
def quote():
	return render_template("quotes.html")


@app.route('/process', methods=['POST'])
def process():
	image=request.form['image']

	heading=request.form['heading']
	paragraph=request.form['paragraph']
	postdata=Favposts(image=image ,heading=heading, paragraph=paragraph)
	db.session.add(postdata)
	db.session.commit()
	return redirect(url_for("index"))





if __name__ == '__main__':
	app.run()

