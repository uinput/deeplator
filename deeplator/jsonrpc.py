import json
import urllib.request as request

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
        data_str = json.dumps(data)
        return data_str.encode("utf-8")

    def send(self, url):
        req = request.Request(url, data=self.dumps(), headers=HEADERS)
        data_str = request.urlopen(req).read()
        resp = json.loads(data_str.decode("utf-8"))
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
