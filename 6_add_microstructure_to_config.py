import os
import json

dir_contents = os.listdir("assets")
statefiles = []
for thing in dir_contents:
    if os.path.isfile(os.path.join("assets", thing)) and thing.endswith(".dtk"): # Best I can do now
        statefiles.append(thing)

infile_path = os.path.join("assets", "covid_config.json")
outfile_path = os.path.join("assets", "covid_config_final.json")
if len(statefiles) == 1:  # Found it!
    spop_filename = statefiles[0]
    with open(infile_path) as infile:
        config_json = json.load(infile)
    config_json["parameters"]["Serialized_Population_Filenames"] = [spop_filename]
    config_json["parameters"]["Demographics_Filenames"] = ["demographics_micro.json"] # Make this more robust
    with open(outfile_path,"w") as outfile:
        json.dump(config_json, outfile, indent=4, sort_keys=True)

