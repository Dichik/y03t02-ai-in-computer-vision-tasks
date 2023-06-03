from utils import get_image_paths

class_names = ['Arnold_Schawarzenegger']
image_paths = get_image_paths("dataset", class_names)
print(image_paths)