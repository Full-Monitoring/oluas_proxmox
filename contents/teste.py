from proxmoxer import ProxmoxAPI
import json

proxmox = ProxmoxAPI('172.33.255.2', user='root@pam',
                     password='10l15p130A@', verify_ssl=False, service='PMG')

a = proxmox.statistics.sender.get()
c = json_formatted_str = json.dumps(a, indent=2)
print(c)