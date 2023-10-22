# IPV4 -> x1.x2.x3.x4
# 4 set of digits 



def validate_ip(strr):
    ip_trim = strr.split('.')
    if len(ip_trim) != 4:
        return False
    for ip in ip_trim:
        #print(ip)
        if not ip.isdigit():
            return False
        if int(ip) < 0 or int(ip) > 255:
            return False
    else:
        return True
        
valid = '192.168.1.1' 
invalid = '192.168.a.1'
invalid = '256.1.1.1'
print(validate_ip(valid))
print(validate_ip(invalid))
print(validate_ip(invalid))