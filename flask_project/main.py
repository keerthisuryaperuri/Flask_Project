from flask import Flask,redirect,url_for,render_template,request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from project_database import Register,Base

engine=create_engine('sqlite:///bvc.db',connect_args={'check_same_thread':False},echo=True)
Base.metadata.bind=engine
DBSession=sessionmaker(bind=engine)
session=DBSession()

app=Flask('__name__')
@app.route("/home")
def hello():
		return"hello keerthi"

@app.route("/keerthi")
def about():
		return"hello welcome"


@app.route("/data/<name1>/<roll_no>")
def data(name1,roll_no):
		name1="keerthi surya"
		roll_no="582"
		return "my name is {} and my roll_no is{}".format(name1,roll_no)

@app.route("/faculty")
def faculty():
			return render_template("sample2.html")

@app.route("/student")
def student():
		return "<font color='red'>hello welcome to student page</font>"

@app.route("/person/<uname>/<roll_no>/<float:marks>")
def person(uname,roll_no,marks):
		return render_template("samp.html",name=uname,roll_no=roll_no,marks=marks)

@app.route("/table/<int:num>")
def table(num):
		return render_template("table.html",n=num)

@app.route("/user/<name>")
def user(name):
		if name=='faculty':
				return redirect(url_for('faculty'))
		elif name=='student':
				return redirect(url_for('student'))
		else:
				return "url not found"

dummy_data=[{'name':'shannu','college':'BVC college','rollno':'590'},{'name':'keerthi','college':'BVC college','rollno':'582'}]
@app.route("/show")
def data_show():
		return render_template("show_data.html",d=dummy_data)



@app.route("/file")
def file_upload():
		return render_template("file_upload.html")

@app.route("/success",methods=["POST"])
def success():
		if request.method=='POST':
				f=request.files["file"]
				f.save(f.filename)
				return render_template("display.html",name=f.filename)

@app.route("/register")
def reg():
	return render_template("sample.html")

@app.route("/show_data")
def showData():
	register=session.query(Register).all()
	return render_template('show.html',register=register)



@app.route("/add",methods=["POST","GET"])
def addData():
	if request.method=='POST':
		newData=Register(name=request.form['name'],surname=request.form['surname'],roll_no=request.form['roll_no'],mobile=request.form['mobile'],branch=request.form['branch'])
		session.add(newData)
		session.commit()
		return redirect(url_for('showData'))
	else:
		return render_template('new.html')
@app.route('/<int:register_id>/edit',methods=["POST","GET"])
def editData(register_id):
	editedData=session.query(Register).filter_by(id=register_id).one()
	if request.method=="POST":
		editedData.name=request.form['name']
		editedData.surname=request.form['surname']
		editedData.roll_no=request.form['roll_no']
		editedData.mobile=request.form['mobile']
		editedData.branch=request.form['branch']

		session.add(editedData)
		session.commit()
		return redirect(url_for('showData'))
	else:
		return render_template('edit.html',register=editedData)

@app.route('/<int:register_id>/delete',methods=["POST","GET"])
def deleteData(register_id):
	deletedData=session.query(Register).filter_by(id=register_id).one()
	if request.method=="POST":
		session.delete(deletedData)
		session.commit()
		return redirect(url_for('showData',register_id=register_id))
	else:
		return render_template('delete.html',register=deletedData)

if __name__=='__main__':
		app.run(debug=True)
