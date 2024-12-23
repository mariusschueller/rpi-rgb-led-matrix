#!/usr/bin/env python3
from samplebase import SampleBase
import marius_video
import marius_site
import time


class Marius(SampleBase):
    def __init__(self, *args, **kwargs):
        super(Marius, self).__init__(*args, **kwargs)

    def run(self):
        # Fetch and preprocess data once
        data = marius_site.get_data()
        restored_data = marius_video.convert_to_ndarray(data)

        # Initialize the canvas
        self.offset_canvas = self.matrix.CreateFrameCanvas()

        count = 0
        # Animation loop
        while count < 500:
            for frame in restored_data:  # Play through each frame
                # Handle the extra nesting by accessing the first level
                for y, row in enumerate(frame[0]):  # Flatten one level of nesting
                    for x, (r, g, b) in enumerate(row):
                        # Set the pixel using RGB values from the frame
                        self.offset_canvas.SetPixel(x, y, r, g, b)

                # Swap the canvas to display the frame
                self.offset_canvas = self.matrix.SwapOnVSync(self.offset_canvas)

                # Add a delay to control frame rate
                time.sleep(0.05)  # Adjust frame delay as needed (e.g., 50ms per frame)
                count += 1


# Main function
if __name__ == "__main__":
    marius = Marius()
    marius.process()  # Parse command-line arguments and set up the matrix
    while True:
        marius.run()  # Start the animation loop
