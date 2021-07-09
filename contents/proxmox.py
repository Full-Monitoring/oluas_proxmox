from proxmoxer import ProxmoxAPI
proxmox = ProxmoxAPI('172.33.255.2', user='root@pam', password='10l15p130A@', verify_ssl=False)
print(proxmox.cluster.resources.get())