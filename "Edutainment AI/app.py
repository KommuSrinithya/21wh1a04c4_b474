# app.py
from flask import Flask, render_template, request, send_from_directory
import os
from text_to_video import VideoGenerator  # Import the VideoGenerator class
app = Flask(_name_, template_folder='templates')
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static', 'videos')
# Use VideoGenerator class for video generation
video_generator = VideoGenerator()
# Dictionary to keep track of generated videos
generated_videos = {}
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/generate_video', methods=['POST'])
def generate_video():
    text_content = request.form.get('text_content')
    script_content = f"Script generated from text: {text_content}"
    video_url = f"/static/videos/{len(generated_videos) + 1}.mp4"
    generated_videos[len(generated_videos) + 1] = video_url
    # Use the VideoGenerator instance to generate the video
    video_generator.generate_video(text_content,     output_file=os.path.join(app.config['UPLOAD_FOLDER'], f"{len(generated_videos)}.mp4"))
    return render_template('result.html', script_content=script_content, video_url=video_url)
# Serve static files from the 'static' folder
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
if _name_ == '_main_':
    app.run(debug=True)
