
from PIL import Image
 
def make_transparent(unique_filename=""):
    img = Image.open(f"temp_img/process/{unique_filename}")
    img = img.convert("RGBA")
 
    datas = img.getdata()
 
    newData = []
 
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
 
    img.putdata(newData)
    img.save(f"temp_img/process_trans/{unique_filename}", "PNG")
 
