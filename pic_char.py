from PIL import Image
#from PIL import ImageFilter
ascii_char = list("@#$%&qwertyuiopasdfghjklzxcvbnm+{}[];<>?,.")
def get_char(r, g, b, alpha=256):
    global ascii_char
    if alpha == 0:
        return " "
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = int(256 / len(ascii_char))
    return ascii_char[gray//unit]

def main():
    im = Image.open(r"d:\Users\Administrator\Desktop\python\11.jpg")
# r, g, b = im.split()
# newr = r.point(lambda x:x<100)
# newg = g.point(lambda x:x*0.9)
# newb = b.point(lambda x:x)
    txt = ""
    for i in range(im.size[1]):
        for j in range(im.size[0]):
            txt += get_char(*im.getpixel((j, i)))
        txt += "\n"
    fo = open("pic_char.txt", "w")
    fo.write(txt)
    fo.close()
main()
om.show("11.jpg")  