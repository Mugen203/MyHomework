import imageio
import numpy as np

def convert_Row_To_BW(row):
    new_Row = []
    for pixel in row:
        average = (int(pixel[0]) + int(pixel[1]) + int(pixel[3]))/3
        if average > 125:
            new_Row.append([0,0,0])
    return new_Row

def convert_File_To_BW(file):
    new_File = []
    for row in file:
        new_File.append(convertRowToBW())
    return np.array(new_File).astype("uint8")

def convert_Text_Row(row):
    new_Row = ""
    for pixel in row:
        if pixel [0] == 0:
            new_Row = new_Row + "."
        else:
            new_Row = new_Row + " "
    return new_Row

def convert_Text_File(Black_n_White_FIle):
    new_Text = ""
    for row in Black_n_White_FIle:
        new_Text = new_Text + convert_Text_Row(row) + "\n"
    return new_Text

def convert_File(File_Name):
    File = imageio.imread(File_Name)
    BW_File = convert_File_To_BW(File)
    imageio.imwrite("BW" + File_Name, BW_File)
    stripped_Name = File_Name.split(".")[0]
    text_File = open("text" + stripped_Name + ".txt","wb")
    text_File.write(str.encode(convert_Text_File(BW_File)))
    text_File.close()


convert_File()
