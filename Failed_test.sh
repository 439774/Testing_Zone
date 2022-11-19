curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer token_here" -d '{
  "name": "ansible-server",
  "region": "nyc1",
  "size": "s-1vcpu-1gb",
  "image": "centos-stream-8-x64",
  "backups": false,
  "ipv6": false,
  "user_data": null,
  "ssh_keys": [],
  "volumes": null,
  "tags": [
    "This is the ansible server"
  ]
}' "https://api.digitalocean.com/v2/droplets"
