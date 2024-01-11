### Docker Installation on Windows
- Activate virtualization in the BIOS.
- Enable the hypervisor through Windows program features.

```bash
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

```

Then, download and run `wsl_updatex64`.