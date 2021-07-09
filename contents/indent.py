###### Inicio do script python
from proxmoxer import ProxmoxAPI
import json
proxmox = ProxmoxAPI('SERVER_IP', user='root@pam', password='SENHA', verify_ssl=False)
### Troque o type abaixo pelos tipos suportados: vm|storage|node|sdn
vm = proxmox.cluster.resources.get(type='vm')
s1 = json.dumps(vm, indent=2)
print(s1)