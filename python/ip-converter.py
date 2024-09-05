import sys
import ipaddress

ip = sys.argv[1]

print('org:\t' + ip)
print('dec:\t' + str(int(ipaddress.ip_address(ip))))
print('bin:\t' + '.'.join([bin(int(x)+256)[3:] for x in ip.split('.')]))
print('oct:\t' + '%04o.%04o.%04o.%04o' % tuple(map(int, ip.split('.'))))
print('hex:\t' + '0x{:02X}{:02X}{:02X}{:02X}'.format(*map(int, ip.split('.'))))
