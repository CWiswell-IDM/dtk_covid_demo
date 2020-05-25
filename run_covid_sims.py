import emod_api
import emodpy_covid
from idmtools.assets import Asset
from idmtools.core.platform_factory import Platform
from idmtools.entities.experiment import Experiment
from emodpy.emod_task import EMODTask

schema_filename = "schema.json"
Eradication_filename = "Eradication.exe"

def build_emod_assets(schema_filename):
    covid_config_filename = emodpy_covid.build_covid_config(schema_filename)
    covid_demographics_filename = emodpy_covid.covid.get_demographics_json()
    seed_campaign_filename = emodpy_covid.covid.get_seed_campaign()
    dtk_pre_process_filename = emodpy_covid.write_pre_process_py()
    dtk_in_process_filename = emodpy_covid.write_in_process_py()
    local_assets_dict = {
        'config': covid_config_filename,
        'demog': covid_demographics_filename,
        'campaign': seed_campaign_filename,
        'pre_proc': dtk_pre_process_filename,
        'in_proc': dtk_in_process_filename
    }

if __name__ == "__main__":
    local_assets = build_emod_assets(schema_filename)
    platform = Platform('COMPS2')

    contact_tracing_task = EMODTask.from_files(
        eradication_path=Eradication_filename,
        config_path=local_assets['config'],
        campaign_path=local_assets['campaign'],
        demographics_paths=[
            local_assets['demog']
        ]
    )

    dtk_in_process_asset = Asset(local_assets['in_proc'],
                                 relative_path='python')
    contact_tracing_task.common_assets.add_asset(dtk_in_process_asset)

    dtk_pre_process_asset = Asset(local_assets['pre_proc'],
                                  relative_path='python')
    contact_tracing_task.common_assets.add_asset(dtk_pre_process_asset)

    contact_tracing_task.use_embedded_python = True

    experiment = Experiment.from_task(task=contact_tracing_task,
                                      name="DTK-COVID demo run from emodpy_covid")

    platform.run_items(experiment)
    platform.wait_till_done(experiment)


    