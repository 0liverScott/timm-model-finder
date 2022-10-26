import timm
import torch
from torchviz import make_dot
from torch.autograd import Variable

model = timm.create_model('vgg16', pretrained=False, num_classes=3)

print(model)

x = Variable(torch.randn(1, 3, 35, 35))

out = model(x)
print(out)
dot = make_dot(model(x), params=dict(model.named_parameters())).render("graph", format='png')
print(dot)
