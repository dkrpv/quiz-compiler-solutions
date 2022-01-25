# Using a python compiler for web courses

> This is how I would approach the problem. Not a project

If you have ever done an online python course it is quite possible that you have encoutered the ugly quizzes most web courses have. Some of the largest course providers (Coursera, Sololearn) have either multiple-choice questions, or "fill in the blank" questions with only one right choice. Obviously the solution would be to have a built-in compiler (like Datacamp). But how would one work?

### Server creating docker containers
Almost every answer to my question online makes use of this solution. The plan is simple, make every request from user boot up a docker image where their code would be run on a python compiler. Obviously this solution is costly, and slow.
I found a great solution online, [this blog post](https://www.programiz.com/blog/online-python-compiler-engineering/) discusses the docker approach, and the author ends up using prewarmed docker containers. 
> "Even if creating the image of my node server from a Docker image just took 1 to 2 seconds, that's a lot of time for a user who wants to run his program and get the results. We decided to run a cluster of running docker containers that would be ready to accept programs."

![diagram from he website](https://www.programiz.com/blog/content/images/2020/06/prewarm-docker-container-2.png)

>https://www.programiz.com/blog/content/images/2020/06/prewarm-docker-container-2.png

However, the above mentioned Coursera and Sololearn both have free courses and quizzes, meanwhile Datacamp (which as far as my understanding goes, uses the method described in the blogpost) - is behind a paywall. For the service to be completely free, I would need a different solution. (Below is how I would approach the problem to make a quiz app for a small group of people.)

When I first tried building a simple quiz preset with a built-in compiler, I made this in flask.

```python
text = request.form['text']
open('userInput.py', 'w').close()
f = open("userInput.py", "a")
f.write(text)
f.close()
import userInput
result = str(userInput.output())
```
The code snippet above creates a python file, and empties it if it already existed. Pastes the user code into the file, and imports it.

>Ugly, uncreative and uninspiring - yet did the job.

![screenshot](/first.png)

### Client Side compiler

Python does not run in the browser. Thus I needed to first convert it javascript. Luckily for me, [Brython](https://brython.info/index.html) is a thing. It translates python code to javascript, and they can work alongside. Making use of the fantastic documentation of brython, and replacing the one line input with the Ace web code editor - I made this.

```javascript
var editor = ace.edit("editor");
function getCode() {
    window.code = editor.getValue();
    console.log(code);
}
```
```python
from browser import document, window, html
import sys
import io
import math

old_stdout = sys.stdout
new_stdout = io.StringIO()
sys.stdout = new_stdout

output_elem = document["output"]

def check(x):
    x = float(x)
    if x == math.pi:
        output_elem <= html.B("\nCorrect!")
    elif x != math.pi:
        output_elem <= html.B("\nWrong!")

def click(ev):
    exec(window.code)
    output = new_stdout.getvalue()
    output_elem <= html.B(f"{output}")
    check(output)
    sys.stdout = old_stdout
    
document["run_code"].bind("click", click)
```
![screenshot](/second.png)

This is the implementation I would use if I were to build a massive online course website. This is just conceptual and if you accidentally stumble upon this repo, I would not recommend using any of this.