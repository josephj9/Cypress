from flask import Flask, render_template, url_for, request, flash, redirect

userDatabase = {"username123": "password123"}

app = Flask(__name__)
app.secret_key = "super secret key"

@app.route('/', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirmPassword = request.form['confirmPassword']
        
        if username in userDatabase.keys():
            flash("Username Already Exists", category="error")
            return redirect('/')
        
        if password != confirmPassword:
            flash("Passwords Must Match", category="error")
            return redirect('/')
        
        userDatabase[username] = password
        return render_template('map.html')
    else:
        return render_template('register.html')

@app.route('/login.html', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == "admin123" and password == "admin123":
            return "ADMIN"
            # return redirect()
        
        if username not in userDatabase.keys():
            flash("Username not Found")
            return redirect('/login.html')
        
        if userDatabase[username] != password:
            flash("Password is Incorrect")
            return redirect('/login.html')
        
        return render_template('map.html')
        
    return render_template('login.html')

@app.route('/forgotPassword.html', methods=['GET','POST'])
def forgotPassword():
    if request.method == 'POST':
        username = request.form['username']
        newPassword = request.form['password']
        confirmNewPassword = request.form['confirmPassword']
        
        if username not in userDatabase.keys():
            flash("Username Not Found", category="error")
            return redirect('/forgotPassword.html')
        
        if newPassword != confirmNewPassword:
            flash("New Passwords Must Match", category="error")
            return redirect('/forgotPassword.html')
        
        userDatabase[username] = newPassword
        return redirect('login.html')
    else:
        return render_template('/forgotPassword.html')

if __name__ == "__main__":
    app.run(debug=True)