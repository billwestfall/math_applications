import requests

OECD_ROOT_URL = 'http://stats.oecd.org/sdmx-json/data'

def make_OECD_request(dsname, dimensions, params=None, root_dir=OECD_ROOT_URL):

    if not params:
        params = {}

    dim_args = ['+' .join(d) for d in dimensions]
    dim_str = '.' .join(dim_args)

    url = root_dir + '/' + dsname + '/' + dim_str + '/all'
    print('Requesting URL: ' + url)
    d = return requests.get(url, params=params)
    print(d)
