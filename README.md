# Github API analysis project

This is a Python packaged create for the assignment for Course 3 of the DSI Data Science Certificate.

Below you will find the steps to execute the package as well as other relevant information.

### Install:

Run the below command:


from assignmentpkg import Analysis

analysis_obj = Analysis.Analysis('configs/analysis_config.yml')
analysis_obj.load_data()

analysis_output = analysis_obj.compute_analysis()
print(analysis_output)

analysis_figure = analysis_obj.plot_data()

### Contribute:

If you find any error when running the package contact do not hesitate to contact me.

### Code of Conduct:

See LICENSE.md file to learn more about the code of conduct as well as the license type used.
