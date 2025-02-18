import torch  
from diffusers import StableDiffusionInpaintPipeline  

class MapDoctor:  
    def __init__(self):  
        self.model = torch.hub.load('facebook/detr', 'detr_resnet50', pretrained=True)  
        self.inpainter = StableDiffusionInpaintPipeline.from_pretrained('stabilityai/stable-diffusion-2-inpainting')  

    def heal_discrepancy(self, drone_img, user_report):  
        # Detect anomalies  
        anomalies = self.model(drone_img)  
        # Generate mask  
        mask = self._create_mask(anomalies)  
        # Inpaint  
        healed = self.inpainter(  
            prompt=user_report.text,  
            image=drone_img,  
            mask_image=mask  
        ).images[0]  
        return healed  