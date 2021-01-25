import qrcode
import qrcode.image.svg

f = qrcode.image.svg.SvgPathImage


def make_qr(filename, msg):
    img = qrcode.make(msg, image_factory=f)
    img.save(filename)
    img.show()


msg = str(input('Enter the content: '))
filename = str(input('Enter the Filename: '))

make_qr(filename, msg)
