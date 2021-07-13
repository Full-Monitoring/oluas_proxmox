from proxmoxer import ProxmoxAPI
import json, sys
params = sys.argv
proxmox = ProxmoxAPI(params[1], user=params[2], password=params[3], verify_ssl=False)
result = proxmox.cluster.resources.get()
s1 = json.dumps(result)
print(s1)