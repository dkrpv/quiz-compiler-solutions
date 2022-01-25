#not used because ajax
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