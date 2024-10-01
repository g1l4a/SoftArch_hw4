from processing import MirrorFilter, BlackAndWhiteFilter, ResizeFilter, Rotate180Filter
from multiprocessing import Process, Queue
import cv2


def apply_filter_process(filter_class, queue):
    """Function to apply a filter in a separate process."""
    while True:
        frame = queue.get()
        if frame is None:
            break
        processed_frame = filter_class.apply(frame)
        queue.put(processed_frame)


def main():
    input_cap = cv2.VideoCapture(0)
    if not input_cap.isOpened():
        print("Error: Could not open video source.")
        return

    queue = Queue()

    ripple_process = Process(target=apply_filter_process, args=(Rotate180Filter, queue))
    mirror_process = Process(target=apply_filter_process, args=(MirrorFilter, queue))
    resize_process = Process(target=apply_filter_process, args=(ResizeFilter(400, 300), queue))
    red_tint_process = Process(target=apply_filter_process, args=(BlackAndWhiteFilter, queue))

    ripple_process.start()
    mirror_process.start()
    resize_process.start()
    red_tint_process.start()

    while True:
        ret, frame = input_cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        cv2.imshow('Original Video', frame)
        queue.put(frame)
        processed_frame = queue.get()
        cv2.imshow('Output', processed_frame)

    queue.put(None)

    ripple_process.join()
    mirror_process.join()
    resize_process.join()
    red_tint_process.join()

    input_cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
