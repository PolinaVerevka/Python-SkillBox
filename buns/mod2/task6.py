domain = input()
current_domain = ""

while 1:
    if len(domain) > 0:
        char = domain[0]
        if char!= '.':
            current_domain += char
            domain = domain[1::]
        else:
            print(current_domain)
            domain = domain[1::]
            current_domain = ''
    else:
        print(current_domain)
        break
