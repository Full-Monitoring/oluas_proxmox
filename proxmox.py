###### Inicio do script python
from proxmoxer import ProxmoxAPI
import json
proxmox = ProxmoxAPI('172.33.255.2', user='root@pam', password='10l15p130A@', verify_ssl=False)
### Troque o type abaixo pelos tipos suportados: vm|storage|node|sdn
#vm = proxmox.cluster.resources.get(type='vm')
vm = proxmox.cluster.resources.get()
s1 = json.dumps(vm, indent=2)
print(s1)