# # https://www.youtube.com/watch?v=6M3LzGmIAso
from flask import Flask, Response, render_template

app = Flask(__name__)
@app.route("/")
def home():
    return "this will render"
  #  render_template('index.html')

# carrots mean we pass whatever value is in endpoint and pass to function below
# we can type anything in the end point and it will render as a result
@app.route("/<name>")
def user(name):
    return f"Hello {name}!"
# # if __name__ == "__controller__":
# #     app.run(host="127.0.0.1", port=8080, debug=True)



# https://www.youtube.com/watch?v=mqhxxeeTbu0




















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

