import os as alpha
alpha.system("pip install --upgrade pip")
alpha.system("apt-get update")
alpha.system("apt get update")
alpha.system("apt install npm -y")
alpha.system("npm install -g localtunnel")
alpha.system("curl -fsSL https://code-server.dev/install.sh | sh ")
alpha.system("lt --port 8080")
alpha.system("code-server")
