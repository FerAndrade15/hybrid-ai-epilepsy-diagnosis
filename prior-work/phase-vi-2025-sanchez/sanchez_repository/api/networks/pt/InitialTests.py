import torch

checkpoint = torch.load("model_final.pt", map_location="cpu")
state_dict = checkpoint.get("state_dict", checkpoint)

for k in state_dict.keys():
    print(k)