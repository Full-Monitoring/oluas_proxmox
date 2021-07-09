###### Inicio do script python
from proxmoxer import ProxmoxAPI
import json
proxmox = ProxmoxAPI('172.33.255.2', user='root@pam', password='10l15p130A@', verify_ssl=False)

#print("########## Exibe todos os dados dos resoruces do tipo 'vm'")
### Troque o type abaixo pelos tipos suportados: vm|storage|node|sdn
vm = proxmox.cluster.resources.get(type='vm')
#s1 = json.dumps(vm)
#d2 = json.loads(s1)
print(vm)