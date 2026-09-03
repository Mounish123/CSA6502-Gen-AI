import json
import torch
import torch.nn as nn
from PIL import Image
from torchvision import models, transforms


MODEL_PATH = "models/crop_disease_model.pth"
CLASSES_PATH = "models/classes.json"

IMAGE_PATH = "test.jpg"


# -----------------------------
# Load classes
# -----------------------------

with open(CLASSES_PATH, "r", encoding="utf-8") as f:
    classes = json.load(f)


# -----------------------------
# Load model
# -----------------------------

model = models.resnet18(weights=None)

model.fc = nn.Linear(
    model.fc.in_features,
    len(classes)
)

checkpoint = torch.load(
    MODEL_PATH,
    map_location="cpu",
    weights_only=False
)

if isinstance(checkpoint, dict) and "model_state_dict" in checkpoint:
    checkpoint = checkpoint["model_state_dict"]

elif isinstance(checkpoint, dict) and "state_dict" in checkpoint:
    checkpoint = checkpoint["state_dict"]


# Remove DataParallel prefix if present

checkpoint = {
    k.replace("module.", "", 1) if k.startswith("module.") else k: v
    for k, v in checkpoint.items()
}

model.load_state_dict(checkpoint)

model.eval()


# -----------------------------
# Image preprocessing
# -----------------------------

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])


# -----------------------------
# Load image
# -----------------------------

image = Image.open(IMAGE_PATH).convert("RGB")

image = transform(image)

image = image.unsqueeze(0)


# -----------------------------
# Prediction
# -----------------------------

with torch.no_grad():

    output = model(image)

    probabilities = torch.softmax(output, dim=1)[0]

    top_values, top_indices = torch.topk(
        probabilities,
        5
    )


# -----------------------------
# Output
# -----------------------------

print("\n" + "=" * 60)
print("DIRECT MODEL PREDICTION")
print("=" * 60)

for value, index in zip(top_values, top_indices):

    print(
        f"{classes[index.item()]} : "
        f"{value.item() * 100:.2f}%"
    )

print("=" * 60)