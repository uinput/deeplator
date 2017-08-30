import json

JSONRPC_VERSION = "2.0"


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
