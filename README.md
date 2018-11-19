# Video-To-NumPy-Tensors

This library is for converting video files to NumPy tensors. It uses open-cv library to do the above conversions.

The tensor has five dimensions: 
1. First dimension gives number of videos, 
2. Second dimension gives total number of frames per video
3 & 4. Third and Fourth dimension gives the width and height of image(i.e. shape of pixels)
5. Gives number of channels of the image(i.e. if the images are in grayscale that number of channels will be 1, else if it is RGB it will be 3)

How to use the video reader:
Step 1. Create a Video Reader Object as follows:
Step 2. Create a list of paths of video files.
Step 3. Use the function read_videos(list_of_videos_files)

Sample code is given below
```
  # Step 1
  reader = VideoReader(target_size=(128,128),
                       to_gray=True,
                       max_frames=40,
                       required_fps=5,
                       normalize_pixels=True)
                       
  # Step 2
  paths = [r"/path/to/video1.mp4", r"/path/to/video2.mp4"]
  
  # Step 3
  video_tensors = reader.read_videos(paths)
  
  # Print shape
  print(video_tensors.shape)
  
  Output: (2, 40, 128, 128, 1)

```
