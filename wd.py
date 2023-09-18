import torch
import torchvision
from torchvision.models.detection import FasterRCNN
from torchvision.transforms import functional as F
from PIL import Image

# Load a pre-trained Faster R-CNN model with COCO weights
model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
model.eval()


def detect_weapon(image_path, confidence_threshold=0.5):
    # Load the input image
    image = Image.open(image_path)
    
    # Preprocess the image
    image_tensor = F.to_tensor(image).unsqueeze(0)
    
    # Perform inference
    with torch.no_grad():
        predictions = model(image_tensor)
    
    # Filter detections with confidence above the threshold
    filtered_predictions = [p for p in predictions[0]['scores'] > confidence_threshold]
    
    # Get bounding boxes and labels for the filtered predictions
    boxes = predictions[0]['boxes'][filtered_predictions]
    labels = predictions[0]['labels'][filtered_predictions]
    
    return boxes, labels


# Specify the path to the image you want to test
image_path = "w1.jpg"

# Detect weapons in the image
boxes, labels = detect_weapon(image_path)

# Display the bounding boxes and labels (you can use OpenCV or other libraries for visualization)
for box, label in zip(boxes, labels):
    print(f"Label: {label.item()}, Bounding Box: {box.tolist()}")
