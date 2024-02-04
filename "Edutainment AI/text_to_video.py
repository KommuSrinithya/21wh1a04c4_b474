# text_to_video.py
 
from moviepy.editor import TextClip, CompositeVideoClip
from moviepy.config import change_settings
 
class VideoGenerator:
    def _init_(self):
        # Configure ImageMagick path
        self.image_magick_path = r"C:\Program Files\ImageMagick-7.1.1-Q16\convert.exe"
 
        change_settings({"IMAGEMAGICK_BINARY": self.image_magick_path})
 
    def generate_video(self, text, output_file='example.mp4', duration_per_frame=5):
        txt_clip = TextClip(text, fontsize=70, color='white', bg_color='black')
        txt_clip = txt_clip.set_duration(duration_per_frame)
 
        video_clip = CompositeVideoClip([txt_clip])
 
        video_clip.write_videofile(output_file, codec='libx264', fps=24)
 
# Example usage (you can remove this if not needed)
if _name_ == '_main_':
    # Create an instance of VideoGenerator
    video_generator = VideoGenerator()
 
    # Example text to be converted to a video
    example_text = "Hello, this is a sample text. You can customize it as needed."
    output_path = 'example1.mp4'
    # Generate video using the VideoGenerator instance
    video_generator.generate_video(example_text, output_file=output_path)
