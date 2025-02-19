import os

# Check all environment variables
for key, value in os.environ.items():
    print(f"{key}: {value}")

# Check a specific variable
server_host = os.getenv('SERVER_HOST')
server_port = os.getenv('SERVER_PORT')

print(f"SERVER_HOST: {server_host}")
print(f"SERVER_PORT: {server_port}")