import json
import requests

JSONRPC_VERSION = "2.0"
HEADERS = {"content-type": "application/json"}


class JSONRPCBuilder():
    def __init__(self, method, params):
        self.method = method
        self.params = params

    def dump(self):
        data = {
            "jsonrpc": JSONRPC_VERSION,
            "method": self.method,
            "params": self.params,
            "id": 0
        }
        return data

    def dumps(self):
        data = self.dump()
        return json.dumps(data)

    def send(self, url):
        resp = requests.post(url, data=self.dumps(), headers=HEADERS)
        resp = resp.json()
        if "result" in resp:
            return resp["result"]
        else:
            raise JSONRPCError(resp["error"])


class JSONRPCError(Exception):
    def __init__(self, error_obj):
        self.code = error_obj["code"]
        self.message = error_obj["message"]
        if "data" in error_obj:
            self.data = error_obj["data"]

    def __str__(self):
        return "{}: {}".format(self.code, self.message)
