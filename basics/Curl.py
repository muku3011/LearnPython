import pycurl
from io import BytesIO
import json


def curl_post(url, data, iface=None):
    c = pycurl.Curl()
    buffer = BytesIO()
    c.setopt(pycurl.URL, url)
    c.setopt(pycurl.HTTPGET, True)
    c.setopt(pycurl.HTTPHEADER, ['Content-Type: application/json'])
    c.setopt(pycurl.TIMEOUT, 10)
    c.setopt(pycurl.WRITEFUNCTION, buffer.write)
    # c.setopt(pycurl.POSTFIELDS, data)
    if iface:
        c.setopt(pycurl.INTERFACE, iface)
    c.perform()

    # Json response
    resp = buffer.getvalue().decode('UTF-8')

    #  Check response is a JSON if not there was an error
    try:
        resp = json.loads(resp)
    except json.decoder.JSONDecodeError:
        pass

    buffer.close()
    c.close()
    return resp


if __name__ == '__main__':
    dat = {"id": 52, "configuration": [{"eno1": {"address": "192.168.1.5"}}]}
    res = curl_post("http://192.168.1.1/osc/info", json.dumps(dat), "wlan0")
    print(res)
