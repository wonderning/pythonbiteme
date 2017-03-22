# coding utf-8
# !/usr/bin/env python

from PIL import Image
import argparse

myparser = argparse.ArgumentParser()
myparser.add_argument("file")
myparser.add_argument("--output", "-o", default="output.txt")
myparser.add_argument("--width", type=int, default=80)
myparser.add_argument("--height", type=int, default=60)

args = myparser.parse_args()

IMG = args.file
OUTPUT = args.output
WIDTH = args.width
HEIGHT = args.height

charlist = list("abcdefghijklmnopqrstuvwxyz ")
# print charlist


def pixel2char(r, g, b, alpha=255):
    if alpha == 0:
        return ""
    else:
        grey = 0.21 * r + 0.71 * g + 0.08 * b
        length = len(charlist)
        return charlist[int(float(grey) / 256.0 * float(length))]


if __name__ == "__main__":
    im = Image.open(IMG)
    txt = ""
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += pixel2char(*im.getpixel((j, i)))
        txt += "\n"
    with open(OUTPUT, "w") as fh:
        fh.write(txt)
