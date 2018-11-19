# Video-To-NumPy-Tensors

This library is for converting video files to NumPy tensors. It uses open-cv library to do the above conversions.

The tensor has five dimensions: 
1. First dimension gives number of videos, 
2. Second dimension gives total number of frames per video
3 & 4. Third and Fourth dimension gives the width and height of image(i.e. shape of pixels)
5. Gives number of channels of the image(i.e. if the images are in grayscale that number of channels will be 1, else if it is RGB it will be 3)

Uses can be used in the following scenarios:
1. For easy loading of inputs to 3D-CNN (Convolution Neural Networks) models. The ouput of the video_reader.read(paths) can be directly given as input to the 3D CNN model.
2. For easy loading of inputs to RNN (Recurrent Neural Network) models. With little changes in the output the modified output can be given as input to RNN model
3. For extracting features for data mining jobs.

What are inputs of the VideoReader class:
1. target_size - type is tuple - It represents the size of the pixels of the given array
2. to_gray - type is boolen - It represents whether the image pixels should be in gray scale or rgb
3. max_frames - type integer - It represents the total number of frames required
4. required_fps - type integer - It represents the how many frames are required in a given second
5. normalize_pixels - type boolean - It represents whether the pixels are to normalized between 0 to 1 (currently not implemented)

How to use the video reader?
1. Create a Video Reader Object as follows
2. Create a list of paths of video files.
3. Use the function read_videos(list_of_videos_files)

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

Future work:
1. To implement normalization
2. To implement from where the pixels need to be picked up i.e. the current implementation only picks up the frames from first index, need to implement from last, middle and random indexes.
3. To properly handle default modes
4. The last dimension i.e. the channel dimension is not handled for rgb images
5. To create RNN based output
6. To publish as a libarary in pip
