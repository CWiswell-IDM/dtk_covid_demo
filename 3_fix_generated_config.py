import json
import os
config_path = os.path.join("assets", "covid_config_stage1.json")
with open(config_path) as infile:
    config_json = json.load(infile)
config_json['parameters'].pop('Serialized_Population_Filenames')
with open(config_path, 'w') as outfile:
    json.dump(config_json, outfile, indent=4, sort_keys=True)

