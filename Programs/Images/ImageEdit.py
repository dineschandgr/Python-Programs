from PIL import Image

def main():
    try:

        #width, height
        filename = "download.jpeg"
        with Image.open(filename) as image:
            width, height = image.size
            print(width, height)

        # Rotate imge
        img = Image.open("download.jpeg")

        # Angle given
        img = img.rotate(180)

        # Saved in the same relative location
        img.save("rotated_picture.jpg")

        #cropped image
        width, height = img.size

        area = (0, 0, width / 2, height / 2)
        img = img.crop(area)

        img.save("cropped_picture.jpg")

        #resize image
        img = Image.open("download.jpeg")
        img2 = Image.open("download1.jpeg")
        img.paste(img2, (50, 50))

        # Saved in the same relative location
        img.save("pasted_picture.jpg")

        # Getting histogram of image
        print(img.histogram())

        # transposing image
        transposed_img = img.transpose(Image.FLIP_LEFT_RIGHT)

        # Save transposed image
        transposed_img.save("transposed.jpg")

        #split image
        print(img.split())

        #thumbnail
        img.thumbnail((200, 200))

        img.save("thumb.jpg")
    except IOError:
        pass


if __name__ == "__main__":
    main()