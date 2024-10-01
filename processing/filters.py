import cv2

class MirrorFilter:
    @staticmethod
    def apply(frame):
        """Applies a mirror filter to the given frame."""
        print("Mirror filter")
        return cv2.flip(frame, 1)


class BlackAndWhiteFilter:
    @staticmethod
    def apply(frame):
        """Applies a black and white filter to the given frame."""
        print("Black and white filter")
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


class ResizeFilter:
    def __init__(self, width=640, height=480):
        self.width = width
        self.height = height

    def apply(self, frame):
        """Applies a resize filter to the given frame."""
        print("Resize filter")
        return cv2.resize(frame, (self.width, self.height))


class Rotate180Filter:
    @staticmethod
    def apply(frame):
        """Applies a 180-degree rotation ilter to the given frame."""
        print("180-degree rotation filter")
        return cv2.rotate(frame, cv2.ROTATE_180)
