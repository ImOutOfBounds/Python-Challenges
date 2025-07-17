import socket


def getDomainName(ipAddress):
    try:
        # get host name
        domainName, _, _ = socket.gethostbyaddr(ipAddress)
        return domainName
    
    except socket.herror as e:
        # Show an error message in case the domain is not found
        print(f"Error trying to find ip {ipAddress}: {e}")


ip = input("insert a value ip in formart 8.8.8.8: ")

print(getDomainName(ip))