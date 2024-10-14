# -*- coding: utf-8 -*-
"""frame_extraction_with_framecount.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19u_Y8a_Z-_iF4OpoqK73q0ryiZnTt7_Z
"""

!pip install opencv-python

import cv2
import os

def extract_frames(video_path, output_folder, frame_rate=1):

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)


    video = cv2.VideoCapture(video_path)

    if not video.isOpened():
        print(f"Error: Could not open video {video_path}")
        return

    fps = video.get(cv2.CAP_PROP_FPS)

    interval = int(fps // frame_rate)

    frame_count = 0
    saved_count = 0

    while True:
        ret, frame = video.read()

        if not ret:
            break

        if frame_count % interval == 0:
            frame_name = f"{output_folder}/frame_{saved_count:05d}.jpg"
            cv2.imwrite(frame_name, frame)
            saved_count += 1

        frame_count += 1


    video.release()
    print(f"Extracted and saved {saved_count} frames to {output_folder}")

video_path = 'your_video.mp4'
output_folder = 'extracted_frames'
frame_rate = 1

extract_frames(video_path, output_folder, frame_rate)