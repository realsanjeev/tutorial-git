# Steps to Install the NVIDIA Driver on Linux

**Step 1: Remove Existing NVIDIA Driver from Your System** 🖥️
Source: [How can I uninstall a NVIDIA driver completely? - Ask Ubuntu](https://askubuntu.com/questions/206283/how-can-i-uninstall-a-nvidia-driver-completely)

Execute the following commands to fully uninstall the NVIDIA driver from your system:

```bash
sudo apt-get --purge remove nvidia*
sudo apt autoremove
sudo apt-get --purge remove "*cublas*" "cuda*"
sudo apt-get --purge remove "*nvidia*"
sudo reboot
```

**Step 2: Install CUDA from Source** ⚙️
Source: [CUDA Toolkit Downloads | NVIDIA Developer](https://developer.nvidia.com/cuda-downloads)

Refer to the official NVIDIA documentation to install CUDA from source.

* Be sure to install the driver using the instructions provided under the "Driver installation" section of the CUDA toolkit installer.
* You may choose any available driver option, though the proprietary kernel module flavor is recommended.

**Step 3: Set Up the NVIDIA Container Toolkit for Docker GPU Support** 🐳
Source: [Installing the NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html)

1. Add the NVIDIA container toolkit repository:

```bash
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
  && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
```

2. Update the package list:

```bash
sudo apt-get update
```

3. Install the NVIDIA Container Toolkit:

```bash
sudo apt-get install -y nvidia-container-toolkit
```

This toolkit allows Docker containers to utilize the GPU.

**Graphics Card Used:** NVIDIA GeForce RTX 2050 🎮
