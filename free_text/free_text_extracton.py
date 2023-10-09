import pytesseract
import json
import cv2
import PIL

class Extract_text:
    def __init__(self, path_of_json):
        self.path_of_json = path_of_json
    
    def read_json(self):
        with open(self.path_of_json) as f:
            data = json.load(f)
            f.close()
            data_regions = data['regions']
            return data_regions
    
    def read_image(self, path_of_image):
        image = cv2.imread(path_of_image, cv2.IMREAD_GRAYSCALE)
        return image

    def extract_coordinates(self, image, data):
        crop_image_list = []
        for bb in data:
            height = int(bb['boundingBox']['height'])
            width = int(bb['boundingBox']['width'])
            left = int(bb['boundingBox']['left'])
            top = int(bb['boundingBox']['top'])
            crop_image = image[top : (top + height) , left: (left + width)]
            # cv2.imwrite("abc.jpg", crop_image )
            crop_image_list.append(crop_image)
        
        return crop_image_list
        
    def apply_tesseract(self, cropped_images):
        get_text_list = []
        for text in cropped_images:
            get_text = pytesseract.image_to_string(text)
            get_text_list.append(get_text)
        
        return get_text_list


c = Extract_text('/home/venkateshiyer/Documents/oo/2fdd8658bbb2d1b1125ccbbd8ad29a88-asset.json')    
roi = c.read_json()
img = c.read_image('/home/venkateshiyer/Downloads/invoice_0.jpg')
crp = c.extract_coordinates(img, roi)
txt = c.apply_tesseract(crp)
print(txt)
