# This file is part of "Junya's self learning project about digital image processing."
#
# "Junya's self learning project about digital image processing"
# is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# "Junya's self learning project about digital image processing"
# is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
#
# (c) Junya Kaneko <jyuneko@hotmail.com>

from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import cv2


def discriminant_analysis(image):
    _image = image.reshape(image.shape[0] * image.shape[1])
    ave = np.average(_image)
    t = j0 = 0
    for _t in range(np.min(_image) + 1, np.max(_image) + 1):
        blacks = _image[_image < _t]
        whites = _image[_image >= _t]
        sigma_b = len(blacks) * np.power(np.average(blacks) - ave, 2) /len(_image) + len(whites) * np.power((np.average(whites) - ave), 2) / len(_image)
        j1 = sigma_b / (np.var(_image) - sigma_b)
        if j0 < j1:
            t = _t
            j0 = j1
    return t


if __name__ == '__main__':
    image = cv2.imread("ware.png")
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    # image = np.array(Image.open('ware.png').convert('L'), dtype=np.uint8)
    bin_image = np.array(image)
    t = discriminant_analysis(image)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            bin_image[i, j] = 255 if image[i, j] >= t else 0

    plt.subplot(1, 2, 1)
    plt.title('Original')
    plt.imshow(image, cmap='Greys_r')

    plt.subplot(1, 2, 2)
    plt.title('Binary')
    plt.imshow(bin_image, cmap='Greys_r')

    plt.show()
"""
if __name__ == '__main__':
    image = np.array(Image.open('ware.png').convert('L'), dtype=np.uint8)
    bin_image = np.array(image)
    t = discriminant_analysis(image)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            bin_image[i, j] = 255 if image[i, j] >= t else 0

    plt.subplot(1, 2, 1)
    plt.title('Original')
    plt.imshow(image, cmap='Greys_r')

    plt.subplot(1, 2, 2)
    plt.title('Binary')
    plt.imshow(bin_image, cmap='Greys_r')

    plt.show()
    """