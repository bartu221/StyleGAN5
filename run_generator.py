import os as alpha
alpha.system("pip install --upgrade pip")
alpha.system("apt install npm")
alpha.system("npm install -g localtunnel")
alpha.system("curl -fsSL https://code-server.dev/install.sh | sh")
alpha.system("lt --port 8080")
alpha.system("code-server")
