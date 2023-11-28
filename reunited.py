# run script with: python reunited.py <folder>
import argparse
import os
import random
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips, concatenate_audioclips

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("dir", help="Directory containing the audio/video files")
args = parser.parse_args()

# Get a list of all files in the directory
files = os.listdir(args.dir)

# Filter the list to include only audio or video files
video_files = [file for file in files if file.lower().endswith(('.mp4', '.avi', '.mov', '.mkv'))]
audio_files = [file for file in files if file.lower().endswith(('.mp3', '.wav', '.flac', '.aac'))]

if video_files:
    # Load each video file
    clips = [VideoFileClip(os.path.join(args.dir, file)) for file in video_files]

    # Shuffle the list of clips
    random.shuffle(clips)

    # Concatenate the clips
    final_clip = concatenate_videoclips(clips)

    # Write the output file
    final_clip.write_videofile(os.path.join(args.dir, "output.mp4"))

elif audio_files:
    # Load each audio file
    clips = [AudioFileClip(os.path.join(args.dir, file)) for file in audio_files]

    # Shuffle the list of clips
    random.shuffle(clips)

    # Concatenate the clips
    final_clip = concatenate_audioclips(clips)

    # Write the output file
    final_clip.write_audiofile(os.path.join(args.dir, "output.mp3"))