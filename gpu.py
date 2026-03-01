import torch

# Check if CUDA (GPU) is available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

if device.type == 'cuda':
    print("Device:", device)
    print("GPU Name:", torch.cuda.get_device_name(0))  # Get the name of the GPU
    print("GPU Memory:", torch.cuda.get_device_properties(0).total_memory)  # Get the total memory of the GPU
else:
    print("Device:", device)
