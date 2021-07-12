# INSTRUÇÕES

## libs python

```sh
1 - proxmoxer
2 - json
3 - sys
```

## Script python

```py
from proxmoxer import ProxmoxAPI
import json, sys
params = sys.argv
proxmox = ProxmoxAPI(params[1], user=params[2], password=params[3], verify_ssl=False)
result = proxmox.cluster.resources.get()
s1 = json.dumps(result)
print(s1)
```

## como execultar o script?

python3 + local do script + ip do servidor + usurario do proxmox + senha do proxmox

Ex: ...

```sh
python3 /home/script/py/proxmox.py 127.0.0.1 root@pam superSenha123
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
