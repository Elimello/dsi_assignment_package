from typing import Any, Optional
import matplotlib
import matplotlib as plt
import yaml
import requests
import json
from pprint import pprint
from google.colab import userdata

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
    pprint(r_json)

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

  def get_user_data(self) -> dict:

    """ Get the authenticated user data object from GitHub.
    Connect to the GitHub API and retrieve the authenticated users' data as Python dictionary.
    The token is retrieved from the colab userdata system.

    Parameters
    ----------
    None

    Returns
    -------
    user_obj : dict
      User data retrieved from GitHub

    Examples
    --------
    user_obj = get_user_data()
    pprint(user_obj)

    {
      'name': 'Simeon Wong',
      'login': 'dtxe',
      ...
    }
    """

    token = userdata.get('ghtoken')

    main_api = 'https://aasdsasadaapi.com'
    backup_api = 'https://api.github.com'

    try:
      # get response from first API
      response = requests.get(url=main_api+'/user',
                            headers={'Authorization': 'Bearer ' + token})
      print('success from first API')

    except requests.exceptions.ConnectionError:
      print('Error with 1st API, trying 2nd')
      # connection error to first API, let's try backup
      response = requests.get(url=backup_api+'/user',
                            headers={'Authorization': 'Bearer ' + token})
      print('Success from 2nd API')

    # parse json
    # response_json = json.loads(response.text)

    return response.json()

  user_obj = get_user_data()

  pprint(user_obj)

  pass

