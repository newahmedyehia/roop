# from flask import Flask, request, jsonify , send_file 
# import requests
# import random 
# import subprocess
# from flask_caching import Cache


# app = Flask(__name__)
# cache = Cache(app, config={'CACHE_TYPE': 'simple'})

# # ngrok.set_auth_token("2OjkuOVJ4LFyiVrJTnE7ecCXduo_6YoaMmEtEBoVFin2dTCp5")
# # public_url =  ngrok.connect(port_no).public_url



    

# @app.route('/process_video')
# @cache.cached(timeout=60)
# def process_video():
#     # run the command to generate the face changed video
#     command = "python run.py -f rc.png -t my_video.mp4 -o face_changed_video.mp4 --keep-frames --keep-fps "
#     subprocess.run(command.split())

#     # generate the URL to the processed video
#     video_url = f"{request.url_root}show_video"

#     # return the URL as the response
#     return jsonify(video_url)

# @app.route('/show_video')
# def show_video():
#     # return the processed video file as the response
#     return send_file('face_changed_video.mp4', mimetype='video/mp4', as_attachment=True)

######################
from flask import Flask
from pyngrok import ngrok

port_no = 5000

from flask import Flask, request, jsonify , send_file 
import requests
import random 
import subprocess
from flask_caching import Cache


app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

ngrok.set_auth_token("2OjkuOVJ4LFyiVrJTnE7ecCXduo_6YoaMmEtEBoVFin2dTCp5")
public_url =  ngrok.connect(port_no).public_url



    

@app.route('/process_video')
@cache.cached(timeout=60)
def process_video():
    # run the command to generate the face changed video
    command = "python run.py -f rc.png -t my_video.mp4 -o face_changed_video.mp4 --keep-frames --keep-fps"
    subprocess.run(command.split())

    # generate the URL to the processed video
    video_url = f"{request.url_root}show_video"

    # return the URL as the response
    return jsonify(video_url)

@app.route('/show_video')
def show_video():
    # return the processed video file as the response
    return send_file('face_changed_video.mp4', mimetype='video/mp4', as_attachment=True)


print(f"To acces the Gloable link please click {public_url}")

app.run(port=port_no )

