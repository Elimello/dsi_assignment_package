# Github API analysis project

This is a Python packaged create for the assignment for Course 3 of the DSI Data Science Certificate.

Below you will find the steps to execute the package as well as other relevant information.

### Install:

Run the below command:

```
# Install the package
!pip install git+https://github.com/Elimello/dsi_assignment_package
# Import the Analysis class from the assignmentpkg package
from assignmentpkg import Analysis

# Initialize the Analysys object with the analysis_config YAML file
# The original path was replaced to accommodate the name change
analysis_obj = Analysis.Analysis('configs/analysis_config.yml')

# Proceed to load the data using the method load_data()
analysis_obj.load_data()

# Proceed to perform the analysis using the method compute_analysis()
analysis_output = analysis_obj.compute_analysis()
print(analysis_output)

# Optionally, plot the outcomes of the analysis
analysis_figure = analysis_obj.plot_data()
```

### Contribute:

If you find any error when running the package contact do not hesitate to contact me.

### Code of Conduct:

See LICENSE.md file to learn more about the code of conduct as well as the license type used.
