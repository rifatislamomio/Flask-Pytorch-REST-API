import torch
from torchvision import transforms
from PIL import Image
import io

class Classifier:
    def __init__(self,model_path):
        self.model = torch.jit.load(model_path, map_location='cpu')
        self.model.eval()

    def transform_image(self,image):
        transform = transforms.Compose([
        transforms.Resize(224),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485,0.456,0.406], 
                                [0.229,0.224,0.225])])
	
        image = Image.open(io.BytesIO(image))
        return transform(image)

    def predict(self,image):
        img_tensor = self.transform_image(image)
        output = self.model.forward(img_tensor.view(1,3,224,224)).argmax()
        return output.item()