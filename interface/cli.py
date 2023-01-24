#command line inter

import argparse
from scanner import scanner

def main():
    parser = argparse.ArgumentParser(
        description="Command line tool to scan a network, identify vulnerabilities, exploit vulnerabilities & generate a report of findings."
    )
    parser.add_argument(
        "ip", type=str,
        help="The IP of the target machine."
    )
    parser.add_argument(
        "--ports", "-p",
        help=("Specify specific ports to scan. If not specified, all ports will be scanned")
    )
    args = parser.parse_args()
    #file_size = download(args.url, dest_path=args.output)
    #print("Download successful! (size: {} B)".format(file_size))
    scanner(args.ip, args.ports)
    

if __name__ == "__main__":
    main()