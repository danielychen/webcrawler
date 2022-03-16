All commands are run in the VSCode terminal

1. Open VSCode
2. Select the environment `venv` from the `Python: Select Interpreter`
3. run `pip install scrapy`
4. cd into `webcrawler`
5. run `scrapy crawl rescale -o links.csv` to generate a `.csv` file of all the deep links
6. run `scrapy check` to run an assertion against the return value for all the links that are retured from the previous check. It should pass 3 contracts with no failures.

Main code is found under `webcrawler/webcrawler/spiders/__init__.py`