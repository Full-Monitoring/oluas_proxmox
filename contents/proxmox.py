from proxmoxer import ProxmoxAPI
proxmox = ProxmoxAPI('SERVER_IP', user='root@pam', password='SENHA', verify_ssl=False)
print(proxmox.cluster.resources.get())