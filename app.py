import json, falcon

class ObjRequestClass:
    def on_get(self, req, resp):
        content = {
            'name': "falcon"
        }
        resp.body = json.dumps(content)


api = falcon.API()
api.add_route('/test', ObjRequestClass())
