import os
import sys
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# # Detecting the videos folder relative to the script's location
# if len(sys.argv) == 2:
#     VIDS_PATH = sys.argv[1]
#     print(VIDS_PATH)
# else:
#     script_dir = os.path.dirname(os.path.abspath(__file__))
#     VIDS_PATH = os.path.join(script_dir, 'videos')

#     if not os.path.exists(VIDS_PATH):
#         print(' - The videos folder does not exist!')
#         sys.exit()

# @app.after_request
# def add_headers(res):
#     res.headers["Cache-Control"] = 'no-cache, no-store, must-revalidate'
#     res.headers["Pragma"] = 'no-cache'
#     res.headers["Expires"] = '0'
#     return res
VIDS_PATH='./videos'
@app.route('/')
def index():
    return 'vid'

@app.route('/video/<vid_name>')
def get_vid(vid_name):
    return send_from_directory(VIDS_PATH, vid_name)

@app.route('/play/<vid_name>')
def play_video(vid_name):
    return render_template('plyr.html', vid_name=vid_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

