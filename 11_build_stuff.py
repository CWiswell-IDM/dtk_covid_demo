from emod_api.schema.get_schema import dtk_to_schema
import os

EMOD_path = os.path.join("assets","Eradication.exe")
dtk_to_schema(EMOD_path)
