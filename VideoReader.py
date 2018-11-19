import cv2
import numpy as np


class VideoReader(object):
    def __init__(self,
                 target_size=None, to_gray=True,
                 max_frames=None, required_fps=None, normalize_pixels=None):
        if target_size is None:
            raise RuntimeError("Target size is null, it should not be null")
        if type(target_size) != tuple:
            raise RuntimeError("Target size should be tuple")

        self.target_size = target_size
        self.to_gray = to_gray
        self.max_frames = max_frames
        self.required_fps = required_fps
        self.normalize_pixels = normalize_pixels

    def _read_video(self, path):
        video = cv2.VideoCapture(path)
        print(video.isOpened())
        actual_frames_per_second = video.get(cv2.CAP_PROP_FPS)
        actual_number_of_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

        # validations
        if self.max_frames >= actual_number_of_frames:
            err_message = "Number of given frames {%s} is greater than actual number of frames {%s}" % self.max_frames % actual_number_of_frames
            raise RuntimeError(err_message)
        if self.required_fps >= actual_frames_per_second:
            err_message = "Given fps {%s} is greater than actual fps {%s}" % self.required_fps % actual_frames_per_second
            raise RuntimeError(err_message)

        list_of_frames = []
        local_count_of_frames = 0
        while video.isOpened():
            if local_count_of_frames == self.max_frames:
                break
            current_frame_number = video.get(1)
            success, image = video.read()
            if success:
                if current_frame_number % self.required_fps == 0:
                    image = cv2.resize(image, self.target_size, interpolation=cv2.INTER_AREA)
                    if self.to_gray:
                        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                    local_count_of_frames += 1
                    list_of_frames.append(image)

        image_tensor = np.stack(list_of_frames)
        # Need to change the number of dimensions for RGB currently only supports GrayScale Dimensions
        return np.expand_dims(image_tensor, axis=image_tensor.ndim)

    def read_videos(self, paths):
        list_of_videos = []
        for path in paths:
            list_of_videos.append(self._read_video(path))
        return np.stack(list_of_videos)

