from flask import Flask,redirect,url_for,render_template
app=Flask(__name__)

@app.route("/hello")
def show_hello():
	return "<h1>HI.....Welcome to home page</h1>"

@app.route("/admin")
def admin():
	return render_template("sample.html")

@app.route("/student")
def student():
	return "<font colour='red'>I am from computer science branch</font>"

@app.route("/faculty")
def faculty():
	return "Welcome to faculty data"

@app.route("/person/<uname>/<age>/<village>/<num>")
def person(uname,age,village,num):
	return render_template("samp.html",uname=uname,age=age,village=village,num=num)

@app.route("/user/<name>")
def user(name):
	if name=='hello':
		return redirect(url_for('show_hello'))
	elif name=='admin':
		return redirect(url_for('admin'))
	elif name=='student':
		return redirect(url_for('student'))
	elif name=='faculty':
		return redirect(url_for('faculty'))
	else:
		return "URL not existed"


@app.route("/table/<int:num>")
def table(num):
	return render_template("table.html",n=num) 

dummy_data=[{
	'name':'keerthi surya',
	'org':'BVC',
	'DOB':'29 dec 2001'},

	{'name':'shanmukhi',
	'org':'BVC',
	'DOB':'23 may 2002'
}]
@app.route("/show")
def data_show():
	return render_template("show_data.html",d=dummy_data)


@app.route("/register")
def register():
	return render_template("sample.html")


if __name__ == '__main__':
	app.run(debug=True)


main.py
