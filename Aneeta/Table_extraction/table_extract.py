from img2table.document import Image
from PIL import Image as PILImage
import numpy as np
import cv2

def extract_table(img_path):
    img = Image(src = img_path) #specify image path
    extracted_tables = img.extract_tables()

    return extracted_tables[0]

def extract_cell(table, img):
    my_dict = {}
    cell_list = []
    print(table)
    table_contents = table.content

    if len(table_contents.keys()) == 5 and sum(len(value) for value in table_contents.values()) == 65:
        del table_contents[0], table_contents[4]
        for row in table.content.values():
            for cell in row:
                new_img = img[cell.bbox.y1:cell.bbox.y2, cell.bbox.x1:cell.bbox.x2]
                img_arr = np.array(new_img)
                cell_list.append(img_arr)
        cell_arr = np.array(cell_list, dtype = object)
        reshaped_cell_list = cell_arr.reshape(3,13)
        processed_cell_list = np.delete(reshaped_cell_list, 0, axis = 1)
        
        for i in range(1, 13):
            key_list = []
            for sublist in processed_cell_list:
                key_list.append(sublist[i - 1])
            my_dict[str(i)] = key_list
        
        print(my_dict)

img_path = '2.jpg'
extratced_table = extract_table(img_path)
img = cv2.imread(img_path)
extract_cell(extratced_table, img)


