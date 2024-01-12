from typing import Any, Optional
import matplotlib
import matplotlib as plt
import yaml
import requests
import json
from pprint import pprint

# get secret from colab
from google.colab import userdata
token = userdata.get('ghtoken')

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
    
    # initialize request parameters
    url = 'https://api.github.com/search/repositories?q=stars:>1&sort=stars&per_page=20'
    headers = {'Authorization': 'Bearer ' + token}

    # send request to GitHub
    r = requests.get(url, headers=headers)

    r_json = json.loads(r.text)

    pass

  def plot_data(self, save_path:Optional[str] = None):
    
    # initialize request parameters
    url = 'https://api.github.com/search/repositories?q=stars:>1&sort=stars&per_page=20'
    headers = {'Authorization': 'Bearer ' + token}

    # send request to GitHub
    r = requests.get(url, headers=headers)

    r_json = json.loads(r.text)
    # plot
    items = r_json['items']
    print(items[0])

    repo_name = []
    repo_stars = []
    for item in items:
      repo_name.append(item['name'])
      repo_stars.append(item['stargazers_count'])

    plt.barh(repo_name, repo_stars)
    
    pass

