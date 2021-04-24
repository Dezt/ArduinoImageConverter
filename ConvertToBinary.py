#converts a .png into a hardcoded array that the SSD1306 monochrome monitor can load and use

#this uses a Python image library called Pillow to work.
#if Pillow is not installed run the following in the Windows console:
#    python3 -m pip install --upgrade pip
#    python3 -m pip install --upgrade Pillow
#for more info see:  https://pillow.readthedocs.io/en/stable/installation.html
#created using help from https://stackoverflow.com/questions/11064786/get-pixels-rgb-using-pil

from PIL import Image

def convertToBinary(imageNames):

    outstring = "//These hardcoded values are intented to be used in the Arduino code for the SSD1306 monochrome monitor\n\n";
    for imageName in imageNames:
        im = Image.open(imageName)
        baseName = imageName[0:-4]
        macroName = baseName.upper()
        width, height = im.size
        rgb_im = im.convert('RGB')

        textColumns = int(width / 8) #dividing it like this will make the text data appear in a somewhat visual way

        outstring += "#define " + macroName + "_WIDTH " + str(width) + "\n"
        outstring += "#define " + macroName + "_HEIGHT " +  str(height) + "\n"
        outstring += "static const unsigned char PROGMEM " + baseName + "[] = \n{ B"

        byteItr = 0
        newLineItr = 0
        for y in range(height):
            for x in range(width):
                if byteItr == 8:
                    newLineItr += 1
                    if newLineItr == textColumns:
                        outstring += ",\n  B"
                        newLineItr = 0
                    else:
                        outstring += ", B"
                    byteItr = 0

                r, g, b = rgb_im.getpixel((x, y))
                if r > 128:
                    outstring += "1"
                else:
                    outstring += "0"
                byteItr += 1
               # print(byteItr)  #debug

        outstring += "};\n\n"

    #write the out put to the file
    f = open("HARDCODED_IMAGE.txt", "w")
    f.write(outstring)
    f.close()

#exectution is here:
convertToBinary(['test01.png','test02.png','test03.png','test04.png'])


