import subprocess

def get_dns_records(domain):
    print(f"[*] claiming dns records: {domain}")
    cmd = f"host -a {domain}"
    return subprocess.check_output(cmd, shell=True, text=True)