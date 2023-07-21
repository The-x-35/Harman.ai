from flask import Flask, render_template, request, jsonify
from Bard import Chatbot
import os
from src.BingImageCreator import ImageGen 
image_generator = ImageGen(os.environ['img'])
chatbot = Chatbot(os.environ['key'])


app = Flask('app')

@app.route("/")
def index():
    return render_template('chat.html')



@app.route("/get")
def get_bot_response():
    input = request.args.get('msg')
    print("Input: ",input)
    if(input.startswith('.generate')):
      input = input[10:]
      print("Prompt: ", input)
      try:
        images=image_generator.get_images(input)
      except Exception as e:
        return "Can't generate the images with this prompt, please try again with a different command."
      
      if(len(images)>0):
        output="img:"+images[0]+','+images[1]+','+images[2]+','+images[3]
        print("Output: ", output)
        return output

      else:
        return "Can't generate the images with this prompt, please try again with a different command."
      
      
    else:
      input= "Behave as if your name is Harman.ai and you are made by Arpit Singh,Please do not include any images in answer, Answer this questions: "+input
      output= chatbot.ask(input)['content']
      print("Output: ", output)
      return output

app.run(host ='0.0.0.0', port = 8080)




