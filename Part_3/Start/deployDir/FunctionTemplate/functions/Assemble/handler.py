import json

from .cloud_function import cloud_function

# Wrapper for OpenFaaS
def handle(event):
  req_json = json.loads(event)

  return cloud_function(req_json)
