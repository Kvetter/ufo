import subprocess

def ping_return_code(hostname):
    """Use the ping utility to attempt to reach the host. We send 5 packets
    ('-c 5') and wait 3 milliseconds ('-W 3') for a response. The function
    returns the return code from the ping utility.
    """
    amount_to_be_run = 20
    output = subprocess.check_output(['ping', '-c', str(amount_to_be_run), hostname]).decode("utf-8")
    codes = output.split("\n")
    avg = 0
    for code in codes:
        if "time=" in code:
            idx = code.find('time')
            avg += float(code[idx+5:-3])
    return round((avg/amount_to_be_run),2)

def verify_hosts(host_list):
    """For each hostname in the list, attempt to reach it using ping. Returns a
    dict in which the keys are the hostnames, and the values are the average return time.
    Assumes that the hostnames are valid.
    """
    return_codes = dict()
    for hostname in host_list:
        return_codes[hostname] = ping_return_code(hostname)

    return return_codes

def main():
    hosts_to_test = [
        '128.199.144.199',
        '167.99.51.33',
        '46.101.253.149'
    ]

    print (verify_hosts(hosts_to_test))

if __name__ == '__main__':
    main()
