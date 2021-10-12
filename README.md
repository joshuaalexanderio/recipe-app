# Recipe App
### Simple website using CSS grid to display a list of recipes I make often with a button to add all ingredients to a todoist project.

## Getting started:
* Run "pip install flask".
* Run "pip install bs4".
### In "main" directory
* In server.py, edit all instances of "Authorization" key values to "Bearer [your API token]". This can be obtained by going to https://todoist.com/app/settings/integrations>Issue a new API token>Copy to clipboard.
* Open todoist.py and change Authorization key value to "Bearer [your API token]".
* Run "python todoist.py" to obtain project_id for your todoist projects.
* In server.py, edit all instances of "project_id" keys to contain the project ID for the todoist list you would like to import ingredients to.
* Run "python server.py" to host site on localhost:5000.



## TO-DO:

* Add feature: add/remove recipe cards with custom titles
* Add feature: add/remove ingredients
