from typing import Any, Optional
import matplotlib
import matplotlib as plt
import yaml

class Analysis():
  def __init__(self, analysis_config:str):
    CONFIG_PATHS = ['configs/system_config.yml', 'configs/user_config.yml']
    # add the analysis config to the list of paths to load
    paths = CONFIG_PATHS + [analysis_config]

    # initialize empty dictionary to hold the configuration
    config = {}

    # load each config file and update the config dictionary
    for path in paths:
        with open(path, 'r') as f:
            this_config = yaml.safe_load(f)
        config.update(this_config)
    
    self.config = config

  def load_data(self):
    self.config['data_path']
    pass

  def compute_analysis(self) -> Any:
    pass

  def plot_data(self, save_path:Optional[str] = None):
    pass

