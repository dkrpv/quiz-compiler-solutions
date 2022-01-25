from flask import Flask, render_template, request, session
app = Flask(__name__, template_folder='htmlFiles')
app.secret_key = 'lol'

@app.route("/")
def index():
    return render_template("index.html", result="")

@app.route("/", methods=['GET','POST'])
def codePost():
   if request.method == 'POST':
      if request.form.get('runBtn') == 'Run':
         text = request.form['text']
         open('userInput.py', 'w').close()
         f = open("userInput.py", "a")
         f.write("import math")
         f.write("\n")
         f.write(text)
         f.close()
         import userInput
         res = str(userInput.x)
         return render_template("index.html", result=res)
      elif request.form.get('clearBtn') == 'Clear':
         return render_template("index.html", result="")
if __name__ == '__main__':
   app.run(debug = True)