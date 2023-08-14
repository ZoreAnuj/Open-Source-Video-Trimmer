import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.video.fx.resize import resize
import csv

dict = {}

class VideoTrimmer:
    def __init__(self, root):

        self.root = root
        self.root.title("Video Trimmer")

        self.video_path = ""
        self.cap = None
        self.current_frame = 0
        self.total_frames = 0

        self.start_frame = 0
        self.end_frame = 0

        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.root, width=360, height=540)
        self.canvas.pack()

        self.slider = tk.Scale(self.root, from_=0, to=0, orient="horizontal", length=600, command=self.set_frame)
        self.slider.pack()

        self.load_button = tk.Button(self.root, text="Load Video", command=self.load_video)
        self.load_button.pack()

        self.set_start_button = tk.Button(self.root, text="Set Start", command=self.set_start)
        self.set_start_button.pack()

        self.set_end_button = tk.Button(self.root, text="Set End", command=self.set_end)
        self.set_end_button.pack()

        self.trim_button = tk.Button(self.root, text="Trim Video", command=self.trim_video)
        self.trim_button.pack()

    def choose_start(self, event):
        self.choosing_start = True
        self.choosing_end = False

    def choose_end(self, event):
        self.choosing_start = False
        self.choosing_end = True

    def load_video(self):
        self.video_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4 *.avi *.mkv *.MOV")])
        if self.video_path:
            self.cap = cv2.VideoCapture(self.video_path)
            
            self.total_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
            self.slider.config(to=self.total_frames - 1)
            self.set_frame(0)


    def set_frame(self, frame_num):
        self.current_frame = int(frame_num)
        if self.cap is not None:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, self.current_frame)
            ret, frame = self.cap.read()
            # print(frame.shape())
            if ret:
                self.display_frame(frame)

    def display_frame(self, frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(frame)
        pil_image = pil_image.resize((360, 540), Image.ANTIALIAS) 
        self.photo = ImageTk.PhotoImage(master=self.canvas, image=pil_image)
        self.canvas.create_image(0, 0, anchor="nw", image=self.photo)

    def set_start(self):
        self.start_frame = self.current_frame
        print("Start frame set:", self.start_frame)

    def set_end(self):
        self.end_frame = self.current_frame
        print("End frame set:", self.end_frame)

    def trim_video(self):
        video_clip = VideoFileClip(self.video_path)
        frame_rate = video_clip.fps
        
        start_time = self.start_frame / frame_rate
        end_time = self.end_frame / frame_rate

        

        trimmed_video_path = f'EventVisionTransformer/output_video/Trimmed_Video_{self.video_path[50:]}_{self.start_frame}To{self.end_frame}.mkv'
        
        dict[self.video_path[50:]] = [self.start_frame,self.end_frame]

        # print(self.video_path[50:])
        
        trimmed_clip = video_clip.subclip(start_time, end_time)

        trimmed_clip =resize(trimmed_clip,(720,1080))

        trimmed_clip.write_videofile(trimmed_video_path, codec="libx264")


        video_clip.close()
        trimmed_clip.close()
        self.cap.release()
        self.cap = None
        self.canvas.delete("all")
        self.slider.config(to=0)
        self.start_frame = 0
        self.end_frame = 0

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoTrimmer(root)
    root.mainloop()
    w = csv.writer(open("output.csv", "w"))

    for key, val in dict.items():

    # write every key and value to file
        w.writerow([key, val])
