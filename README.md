# INSTRUÇÕES

## libs python

```sh
pip3 install proxmoxer
```

## Script python

```py
###### Inicio do script python
from proxmoxer import ProxmoxAPI
import json
proxmox = ProxmoxAPI('SERVER_IP', user='root@pam', password='SENHA', verify_ssl=False)
### Troque o type abaixo pelos tipos suportados: vm|storage|node|sdn
vm = proxmox.cluster.resources.get(type='vm')
s1 = json.dumps(vm, indent=2)
print(s1)
```

## modelo de filtro de contadem de itens correspondentes

```sh
$[?(@.canal== "whatsapp")].length()
```

## macro LLD para armazenar o nome, tipo e id da vm

```md
{#NAME} -> $.name
{#TYPE} -> $.type
{#VMID} -> $.vmid
```

## contador de vms, storages e nodes (total)

```sh
$.[?(@.type == 'qemu')].length()
$.[?(@.type == 'storage')].length()
$.[?(@.type == 'node')].length()
```

## contador de vms (ligadas)

```sh
$.[?(@.status == 'running')].length()
```

## contador de vms (deligadas)

```sh
$.[?(@.status == 'stopped')].length()
```

## filtro de cada item por nome

```sh
$.[?(@.name == '{#NAME}')].cpu.first()
$.[?(@.name == '{#NAME}')].uptime.first()
$.[?(@.name == '{#NAME}')].mem.first()
$.[?(@.name == '{#NAME}')].status.first()
$.[?(@.name == '{#NAME}')].maxcpu.first()
$.[?(@.name == '{#NAME}')].maxmem.first()
$.[?(@.name == '{#NAME}')].netin.first()
$.[?(@.name == '{#NAME}')].netout.first()
```

100*last("vfs.fs.size[/,free]")/last("vfs.fs.size[/,total]")

100*last("vm.mem[{#NAME}]")/last("vm.maxmem[{#NAME}]")

100*last("vm.mem[{#NAME}]")/last("vm.maxmem[{#NAME}]")

