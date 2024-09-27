import torch
from torchvision import models

device = torch.device("cuda")
model = models.resnet18(pretrained=False)
model_name = "resnet18"

batchSize = 8
inputs = torch.rand([batchSize, 3, 224, 224]).cuda()
model = model.to(device)
model.eval()

# Exporting the model to ONNX
onnx_path = f'{model_name}.onnx'

torch.onnx.export(model, inputs, onnx_path,
export_params=True,
do_constant_folding=False,
)
