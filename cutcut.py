# To Run > Open Terminal > cd to the folder > python cutcut.py <fileToCut> <output_dir> <min_length> <max_length>
# If the files are in the same folder as the script, you can just type the file name
# If you want the output on the same folder, the output_dir is just a dot (.)
# Example: python cutcut.py myfile.mp4 out 3 5

import argparse
import random
from moviepy.editor import VideoFileClip, AudioFileClip
import uuid


def main():
    parser = argparse.ArgumentParser(description='Cut audio/video into random pieces.')
    parser.add_argument('input_file', help='Input audio/video file.')
    parser.add_argument('output_dir', help='Output directory.')
    parser.add_argument('min_length', type=int, help='Minimum length of cuts in seconds.')
    parser.add_argument('max_length', type=int, help='Maximum length of cuts in seconds.')
    args = parser.parse_args()
    
    if args.input_file.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):
        clip = VideoFileClip(args.input_file)
        is_audio = False
    elif args.input_file.lower().endswith(('.mp3', '.wav', '.flac', '.aac')):
        clip = AudioFileClip(args.input_file)
        is_audio = True
    else:
        print('Unsupported file type.')
        return

    total_duration = clip.duration
    current_duration = 0
    i = 0

    while current_duration < total_duration:
        start = random.uniform(current_duration, total_duration)
        end = start + random.uniform(args.min_length, args.max_length)
        if end > total_duration:
            end = total_duration
        subclip = clip.subclip(start, end)
        output_file = f'{args.output_dir}/cut_{uuid.uuid4().hex}.mp4' if isinstance(clip, VideoFileClip) else f'{args.output_dir}/cut_{uuid.uuid4().hex}.mp3'
        if is_audio: subclip.write_audiofile(output_file)
        else: subclip.write_videofile(output_file)
        current_duration = end
        i += 1

if __name__ == '__main__':
    main()
