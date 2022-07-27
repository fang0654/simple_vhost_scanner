import json
import requests
import argparse

import logging
from inc.scanner import get_stats

args = argparse.ArgumentParser()

args.add_argument("-w", "--wordlist", help="Wordlist of virtualhosts to use")

args.add_argument("-u", "--url", help="URL to test")
args.add_argument("-o", "--output", help="Output path")

opts = args.parse_args()
domains = [d for d in open(opts.wordlist).read().split("\n") if d]

success = []
initial_status, initial_words = get_stats(opts.url)

for w in domains:
    status, words = get_stats(opts.url, virtualhost=w)

    if status != initial_status or words != initial_words:
        success.append(w)

if opts.output:
    open(opts.output, "w").write(json.dumps({"valid": success}))
print(success)
