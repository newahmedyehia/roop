from flask import Flask, request, jsonify
import json
import requests
import random 
import subprocess
from flask_caching import Cache


# app = Flask(__name__)
# cache = Cache(app, config={'CACHE_TYPE': 'simple'})

# # ngrok.set_auth_token("2OjkuOVJ4LFyiVrJTnE7ecCXduo_6YoaMmEtEBoVFin2dTCp5")
# # public_url =  ngrok.connect(port_no).public_url



    

# @app.route('/process_video')
# @cache.cached(timeout=60)
# def process_video():
#     # run the command to generate the face changed video
#     command = "python run.py -f rc.jpg -t my_video.mp4 -o face_changed_video.mp4 --keep-frames --keep-fps --gpu"
#     subprocess.run(command.split())

#     # generate the URL to the processed video
#     video_url = f"{request.url_root}show_video"

#     # return the URL as the response
#     return jsonify(video_url)

# @app.route('/show_video')
# def show_video():
#     # return the processed video file as the response
#     return send_file('face_changed_video.mp4', mimetype='video/mp4', as_attachment=True)

###################################
import streamlit as st
import subprocess
from flask_caching import Cache
from flask import send_file

cache = Cache(config={'CACHE_TYPE': 'simple'})

@cache.memoize(timeout=60)
def process_video(rc_file, video_file):
    # save uploaded files to disk
    with open("rc.jpg", "wb") as f:
        f.write(rc_file.getbuffer())
    with open("my_video.mp4", "wb") as f:
        f.write(video_file.getbuffer())
    
    # run the command to generate the face changed video
    command = "python run.py -f rc.jpg -t my_video.mp4 -o face_changed_video.mp4 --keep-frames --keep-fps --gpu"
    subprocess.run(command.split())

    # generate the URL to the processed video
    video_url = f"{st.request_url()}show_video"

    # return the URL as the response
    return video_url

def show_video():
    # return the processed video file as the response
    return send_file('face_changed_video.mp4', mimetype='video/mp4', as_attachment=True)

# create file uploader widgets for the two files
rc_file = st.file_uploader('Upload rc.jpg file', type=['jpg', 'jpeg'])
video_file = st.file_uploader('Upload my_video.mp4 file', type=['mp4'])

if st.button('Process video') and rc_file is not None and video_file is not None:
    processed_video_url = process_video(rc_file, video_file)
    st.write('Processed video URL:', processed_video_url)

if st.button('Show video'):
    show_video()
