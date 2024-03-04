import re
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home_page.html")

@app.route('/result', methods=['post'])
def regex_fun():
    exp = request.form.get('exp')
    statement = request.form.get('statement')
    ans = re.findall(exp, statement)
    print(f"Regex={exp}  Statement={statement}")
    return render_template("home_page.html", exp=exp, statement=statement, ans=ans)

@app.route('/varifyEmail')
def varify():
    return render_template("email.html")

@app.route('/validateEmail', methods=['post'])
def validate_email():
    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    email = request.form.get('email')
    if re.match(pattern, email):
        return render_template("email.html", ans="Correct Email Format")
    else:
        return render_template("email.html", ans="Wrong Email Format")

if __name__ == '__main__':
    app.run()