# To Run > Open Terminal > cd to the folder > python cutcut.py <input_folder> <output_dir> <min_length> <max_length>
# If you want the output on the same folder, the output_dir is just a dot (.)
# Example: python cutcut.py ./test ./test/out 3 5

import argparse
import random
import os
from moviepy.editor import VideoFileClip, AudioFileClip
import uuid
import os


def main():
    parser = argparse.ArgumentParser(description='Cut audio/video files in a folder into random pieces.')
    parser.add_argument('input_folder', help='Input folder containing audio/video files.')
    parser.add_argument('output_dir', help='Output directory.')
    parser.add_argument('min_length', type=int, help='Minimum length of cuts in seconds.')
    parser.add_argument('max_length', type=int, help='Maximum length of cuts in seconds.')
    args = parser.parse_args()

    input_folder = args.input_folder
    output_dir = args.output_dir
    min_length = args.min_length
    max_length = args.max_length

    if not os.path.isdir(input_folder):
        print('Input folder does not exist.')
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    files = os.listdir(input_folder)

    for file in files:
        file_path = os.path.join(input_folder, file)

        if file.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):
            clip = VideoFileClip(file_path)
            is_audio = False
        elif file.lower().endswith(('.mp3', '.wav', '.flac', '.aac')):
            clip = AudioFileClip(file_path)
            is_audio = True
        else:
            print(f'Unsupported file type: {file}')
            continue

        total_duration = clip.duration
        current_duration = 0
        i = 0

        while current_duration < total_duration:
            start = random.uniform(current_duration, total_duration)
            end = start + random.uniform(min_length, max_length)
            if end > total_duration:
                end = total_duration
            subclip = clip.subclip(start, end)
            output_file = f'{output_dir}/cut_{uuid.uuid4().hex}.mp4' if isinstance(clip, VideoFileClip) else f'{output_dir}/cut_{uuid.uuid4().hex}.mp3'
            if is_audio:
                subclip.write_audiofile(output_file)
            else:
                subclip.write_videofile(output_file)
            current_duration = end
            i += 1

if __name__ == '__main__':
    main()
