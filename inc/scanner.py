import requests
from urllib3.exceptions import InsecureRequestWarning
import pdb

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


def get_stats(url, user_agent=None, virtualhost=None):

    if user_agent:
        headers = {f"User-Agent": user_agent}

    else:
        headers = {}

    if virtualhost:
        headers["Host"] = virtualhost
    pdb.set_trace()
    res = requests.get(url, allow_redirects=False, headers=headers, verify=False)
    status_code = res.status_code
    words = len(res.text.split(" "))

    return status_code, words
