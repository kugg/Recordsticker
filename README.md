# Recordsticker
Recordstore label printer, currently supporting MAC OS X.
## Status
This is work in progress, do not rely on this app until first release.
## Installation
**Dependencies**

`pip install -r requirements.txt`

**Configuration**

```
echo <<'EOF' >> search/api.ini
[user]
user_token = INSERT YOUR TOKEN HERE

[client]
user_agent = Recordsticker/0.1
EOF
```