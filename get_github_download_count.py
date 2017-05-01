#!/usr/bin/env python

'''
Get the current and total download
count for your project from the
GitHub API.
'''

import requests
import sys


def get_download_count(url):
    req = requests.get(url)
    resp = req.json()
    dc = resp[0]['assets'][0]['download_count']

    tdc = 0
    for e in resp:
        tdc += e['assets'][0]['download_count']

    return (dc, tdc)


def print_usage():
    print 'Usage: %s organization repository' % sys.argv[0]


def main():
    url = 'https://api.github.com'
    try:
        org = sys.argv[1]
        repo = sys.argv[2]
        dc, tdc = get_download_count(
            url + '/repos/%s/%s/releases' % (org, repo)
        )
        print 'Current: ' + str(dc) + '\n  Total: ' + str(tdc)
    except IndexError:
        print_usage()


if __name__ == '__main__':
    main()
