import os

from emodpy_covid.microstructure.change_ser_pop import change_ser_pop

statefile_path = os.path.join("assets", "output_stage_1", "state-00000.dtk")
demographics_path = os.path.join("assets", "demographics.json")
change_ser_pop(old_statefile_name=statefile_path,
               new_statefile_name="state_micro.dtk",
               old_demographics_filename=demographics_path,
               new_demographics_filename="demographics_micro.json")

# TODO: consider maybe building a demographics overlay instead?
# TODO: should this add the demographics and statefile to the config file?
