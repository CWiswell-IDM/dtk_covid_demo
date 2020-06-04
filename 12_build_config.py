from emod_api.config import default_from_schema
import sys

sys.argv = {}
sys.argv[1] = "schema.json"
default_from_schema.write_default_from_schema()
