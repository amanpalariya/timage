from PIL import Image, ImageEnhance


class Timage:
    __ASCII_PIXELS_IN_INCREASING_ORDER_OF_LUMINOSITY = """ .,-~=*>:;!?([{0&%$#@"""
    __MAX_VALUE = 255
    __ascii_image = None

    def __init__(self, image: Image, contrast: float = 1):
        """
        Initializes the engine with PIL Image.
        """
        self.__image = ImageEnhance.Contrast(
            image.convert("L")).enhance(contrast)

    def get_ascii_image(self):
        """
        Returns a 2D array of characters that can be printed in monospaced font.
        """
        if self.__ascii_image == None:
            self.__build_ascii_image()
        return self.__ascii_image

    def pretty_print(self, width_factor=2):
        """
        Prints the image on console.
        Argument: width_factor (default 2)
                  Stretches the image horizontally to account for aspect ratio of typeface
        """
        assert type(width_factor) is int, "width_factor must be an integer"
        if self.__ascii_image == None:
            self.__build_ascii_image()
        width = len(self.__ascii_image)
        height = len(self.__ascii_image[0])
        for y in range(height):
            for x in range(width):
                print(self.__ascii_image[x][y] * width_factor, end="")
            print()

    def __build_ascii_image(self):
        width, height = self.__image.size
        ascii_image = [[None for i in range(height)] for j in range(width)]
        for x in range(width):
            for y in range(height):
                ascii_image[x][y] = self.__get_ascii_pixel((x, y))
        self.__ascii_image = ascii_image

    def __get_ascii_pixel(self, coordinate):
        intensity = self.__get_percentage_intensity_of_pixel(coordinate)
        return self.__get_ascii_pixel_with_intensity(intensity)

    def __get_percentage_intensity_of_pixel(self, coordinate):
        return self.__image.getpixel(coordinate) / self.__MAX_VALUE

    def __get_ascii_pixel_with_intensity(self, intensity):
        assert 0 <= intensity <= 1
        n = len(self.__ASCII_PIXELS_IN_INCREASING_ORDER_OF_LUMINOSITY)
        index = int((n - 1) * intensity)
        return self.__ASCII_PIXELS_IN_INCREASING_ORDER_OF_LUMINOSITY[index]
