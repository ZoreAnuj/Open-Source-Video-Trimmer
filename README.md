# Video Trimmer Application

This is a simple video trimming application that allows you to load a video file, select start and end frames, and trim the video based on your selection. The application is built using Python and the Tkinter library for the graphical user interface, along with other libraries like OpenCV and MoviePy for video processing.

## Prerequisites

Before using this application, make sure you have the following libraries installed:

OpenCV (cv2)
Tkinter (tkinter)
Pillow (PIL)
MoviePy (moviepy)
You can install these libraries using the following command:

```bash
pip install opencv-python-headless pillow moviepy
```

## Usage

1] Run the script by executing the code in the provided .py file.

```bash
python3 video_cropper.py
```

2] The application window will open with buttons and controls for video trimming.

![GUI](https://github.com/ZoreAnuj/Open-Source-Video-Trimmer/blob/main/assets/Screenshot%20from%202023-08-14%2017-05-30.png?raw=true)

Load Video:

3] Click the "Load Video" button to select a video file (supported formats: .mp4, .avi, .mkv, .MOV).
The selected video will be displayed in the application window.
Set Start and End Frames:

![Loading Video](https://github.com/ZoreAnuj/Open-Source-Video-Trimmer/blob/main/assets/Screenshot%20from%202023-08-14%2017-05-52.png?raw=true)

4] Use the slider to navigate through the frames of the loaded video.
Click the "Set Start" button to set the start frame for trimming.
Click the "Set End" button to set the end frame for trimming.
Trim Video:

![Setting Start Frame](https://github.com/ZoreAnuj/Open-Source-Video-Trimmer/blob/main/assets/Screenshot%20from%202023-08-14%2017-06-00.png?raw=true)

5] Once the start and end frames are set, click the "Trim Video" button.
The trimmed video will be saved in the "EventVisionTransformer/output_video" directory with a filename indicating the original video's name, start frame, and end frame.
CSV Output:

6] After trimming, the application will generate an "output.csv" file in the current working directory.
The CSV file contains a mapping of trimmed video filenames to their corresponding start and end frames.

![output.csv](https://github.com/ZoreAnuj/Open-Source-Video-Trimmer/blob/main/assets/Screenshot%20from%202023-08-14%2017-13-24.png?raw=true)


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
