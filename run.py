
import sys
from image_paster_v2 import ImagePasterV2

if __name__ == "__main__":
    if len(sys.argv) == 3:
        folder_path = sys.argv[1]
        paste_path = sys.argv[2]
        paste_location = (0, 0)
        paster = ImagePasterV2()
        paster.watermark_images_in_folder(
            folder_path, paste_path, paste_location)
    else:
        print("Please provide a folder path, paste location as a command line argument.")
