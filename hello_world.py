# Activating your virtualEnvironments
# While in the parent directory to our virtual environments (myEnvironments), 
# activate the virtual environment by typing:

# ------------------------------------------------------------------
# | Mac/Linux: | source flaskEnv/bin/activate                   |
# -------------+----------------------------------------------------
# | Windows command prompt :   | call flaskEnv/Scripts/activate |
# ------------------------------------------------------------------
# | Windows git bash :  |  source flaskEnv/Scripts/activate     |
# ------------------------------------------------------------------


#REQUIRED WITH ANY FLASK APPLICATION

#1. Importing Flask enables us to create the variable
# that is our application (i.e. "app" below).
from flask import Flask, render_template
 # 1.(a). Importing "render_template" allows us to return the rendered HTML 
 # that we created above!


#2. Next, create an app variable and set it = to an INSTANCE of the Flask Module
app = Flask(__name__) 
# - The DoubleUnderscore(*dunder*) "__name__" variable is a 
# GLOBAL variable that tells us IF we are calling/running the FILE: 
# 1) directly _OR_ 2) by importing as a MODULE.

#3. Next, create a decorator (the @ sign is a "decorator") for which is 
# going to attach 'a function' (our "hello_world" below) to a 
#'specific route' (our '/' below.)
# WHAT THIS DOES: once we visit the localhost: 5000 , then the 
# default route for our application will run/call the following function
# called 'hello_world()'.
@app.route('/')
def hello_world():
    return render_template('index.html') 
# 3.(a). NOW.. with "render_template", 1) Render the template! ..2) and Return it!
#    (a). I.E. We are handling the *root route* ('/') with the 'hello_world' function,
#              which renders the 'index.html' *template*. 
#    (b). The HTTP verb is "GET" for ALL routes as DEFAULT setting.


# Serves yet another page/template:
@app.route('/success')
def success():
    return render_template('success.html')
# Now create the 'success.html' file in your *templates* folder.

#4. Last line we have to add is:
app.run(debug=True)

# The above line means that we are going to run the application we 
# defined above, and we are going to run it in the *debug* mode (will show
# errors, if any, in our browser).

# So save the file and go back to the terminal, and run this file 
# (i.e. hello_world.py) via 'python hello_world.py'.

#GENERIC ROUTE(S) CREATION FOLLOWS FOLLOWING STRUCTURE:
# @app.route('/some_route')
# def some_function_name():
#   // your code here
