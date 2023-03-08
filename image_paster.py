from PIL import Image, ImageOps


class ImagePaster:
    def __init__(self, background_path, paste_path, paste_location):
        self.background_image = Image.open(background_path).convert('RGBA')
        self.paste_image = Image.open(paste_path).convert('RGBA')
        self.paste_location = paste_location

    def resize_template(self):
        bg = self.background_image.size
        ratio = 0.5
        print(int(self.paste_image.size[0] * ratio),
              int(self.paste_image.size[1] * ratio))
        self.paste_image = self.paste_image.resize(
            (int(self.paste_image.size[0] * ratio), int(self.paste_image.size[1] * ratio)))

    def resize_background(self):
        new_size = (max(self.background_image.size[0], self.paste_image.size[0]), max(
            self.background_image.size[1], self.paste_image.size[1]))
        self.background_image = ImageOps.expand(self.background_image, ((
            new_size[0] - self.background_image.size[0]) // 2, (new_size[1] - self.background_image.size[1]) // 2))
        self.paste_location = (
            (new_size[0] - self.paste_image.size[0]) // 2, (new_size[1] - self.paste_image.size[1]) // 2)

    def paste(self):
        self.background_image.paste(
            self.paste_image, self.paste_location, self.paste_image)

    def save(self, path):
        self.background_image.convert('RGB').save(path)
