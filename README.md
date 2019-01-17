# DataExploration
## Using pre-collected data (RECOMMENDED)
In case you want to run the project using already collected data DO NOT RUN the `download.ipynb` notebook.
The purpose of this notebook is to download data from twitter, store them in csv files and load them to a database.
If you want to focus on the analytical part of the project, please use an already existing database file (`twitter.db`).
## Using new custom data (NOT RECOMMENDED)
If you plan to collect new data and use them for the project (NOT RECOMMENDED in this case, as the database structure and analysis is strongly customized), run the `download.ipynb` using adjusted parameters and your own twitter application key.
## Package requirements
##### To run all the notebooks you will have to install the following packages:
`tweepy`, `sqlalchemy`, `vaderSentiment`, `networkx`, `matplotlib`, `pprint`, `collections`, `beautifultable`, `pandas`, `csv`

##### You may install all the required packages using the pip* command:
(* or conda or any other package manager that you use)
```pip install tweepy
pip install sqlalchemy
pip install vaderSentiment
pip install networkx
pip install matplotlib
pip install pprint
pip install collections
pip install beautifultable
pip install pandas
pip install csv
```

In case there are any other missing dependencies ("`ModuleNotFoundError`"), install the required packages via pip command as well.

## Running notebooks
Once you complete installation of the required packages, run the notebooks in the following order:
* `analyse.ipynb`
* `vader_analys.ipynb`
* `network_analysis.ipynb` (depends on `vader_analys.ipynb`)

For each notebook, run the cells in the original order, otherwise, results may get corrupted.