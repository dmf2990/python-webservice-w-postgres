# # https://www.youtube.com/watch?v=6M3LzGmIAso
from flask import Flask, Response, jsonify, render_template, redirect, url_for
import requests

app = Flask(__name__)
@app.route("/")
def home():
   return render_template("index.html")

# carrots mean we pass whatever value is in endpoint and pass to function below
# we can type anything in the end point and it will render as a result
# @app.route("/<name>")
# def user(name):
#     return f"Hello {name}!"

#to redirect someone to a diferent page
# import "redirect" and "url_for" these allow
# us to return a redirect from a function
# admin login page example
@app.route("/admin")
def adminRedirectExample():
    return redirect(url_for("home"))


#GET request 
@app.route('/joke')
def get_data():
    resp = requests.get('https://icanhazdadjoke.com/').content
    print(resp)
    return resp

#Function 5: pass variable from endpoint to html this way
@app.route("/<inputThis>")
def passVarThruEndpointToHtml(inputThis):
   return render_template("index.html", htmlVariable=inputThis)


#Function 6 show a list of items in html
@app.route("/asdf/<enterWhatever>")
def passListToHtml(enterWhatever):
   return render_template("index.html", htmlList=["Loanstar", "barf", "lord helmet"])




# https://www.youtube.com/watch?v=9MHYHgh4jYc

# TODO: rig up postgres, pass a value from front to db. https://www.youtube.com/watch?v=M2NzvnfS-hI
# TODO: grab field from db, show to user
# TODO: parse out json from crazy html payload









# # @app.route("https://icanhazdadjoke.com/",methods="GET")
# # def home ():
# #     resp = request.json
# #     return resp


# # https://www.youtube.com/watch?v=cWOpkTWg2vE







# #-------------------------

# # import os
# # from flask import request, jsonify
# # from app import app, mongo
# # import logger
# # ROOT_PATH = os.environ.get('ROOT_PATH')
# # @app.route('/get/questions/', methods=['GET', 'POST','DELETE', 'PATCH'])
# # def question():
# # # request.args is to get urls arguments 


# #     if request.method == 'GET':
# #         start = request.args.get('start', default=0, type=int)
# #         limit_url = request.args.get('limit', default=20, type=int)
# #         questions = mongo.db.questions.find().limit(limit_url).skip(start);
# #         data = [doc for doc in questions]
# #         return jsonify(isError= False,
# #                     message= "Success",
# #                     statusCode= 200,
# #                     data= data), 200

# #     # request.form to get form parameter

# #     if request.method == 'POST':
# #         average_time = request.form.get('average_time')
# #         choices = request.form.get('choices')
# #         created_by = request.form.get('created_by')
# #         difficulty_level = request.form.get('difficulty_level')
# #         question = request.form.get('question')
# #         topics = request.form.get('topics')

# #         ##Do something like insert in DB or Render somewhere etc. it's up to you....... :)

