import os
from PIL import Image, ImageOps


class ImagePasterV2:

    def setup(self, background_path, paste_path, paste_location):
        self.background_image = self.expand_to_square(
            Image.open(background_path)).convert('RGBA')
        self.paste_image = self.resize_paste_image(
            Image.open(paste_path)).convert('RGBA')
        self.paste_location = paste_location

    def expand_to_square(self, image):
        width, height = image.size
        max_size = max(width, height)
        tolerance = 0.1 * max_size
        if abs(width - height) > tolerance:
            new_size = max_size
        else:
            new_size = max_size + round(tolerance - abs(width - height))
        new_image = Image.new('RGB', (new_size, new_size), (248, 248, 248))
        new_image.paste(image, ((new_size - width) //
                        2, (new_size - height) // 2))
        return new_image

    def resize_paste_image(self, image):
        width, height = image.size
        min_size = min(width, height)
        ratio = self.background_image.size[0] / min_size
        new_width = round(width * ratio)
        new_height = round(height * ratio)
        new_image = image.resize((new_width, new_height))

        return new_image

    def paste_and_save(self, output_path):
        # Create a new image by pasting the paste image onto the background image at the specified location
        self.background_image.paste(
            self.paste_image, self.paste_location, self.paste_image)
        # Save the new image to the output file path
        self.background_image.convert('RGB').save(output_path)

    def watermark_image(self):
        self.background_image.paste(
            self.paste_image, self.paste_location, self.paste_image)

    def save_image(self, output_path):
        # Save the new image to the output file path
        self.background_image.convert('RGB').save(output_path)

    def watermark_images_in_folder(self, folder_path, paste_path, paste_location):
        paster = ImagePasterV2()
        for dirpath, dirnames, filenames in os.walk(folder_path):
            for filename in filenames:
                if filename.endswith(('.jpg', '.jpeg', '.png')):
                    if (filename.lower().startswith('no-edit')):
                        continue
                    file_path = os.path.join(dirpath, filename)
                    paster.setup(file_path, paste_path, paste_location)
                    paster.watermark_image()
                    paster.save_image(file_path)
