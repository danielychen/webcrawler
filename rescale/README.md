All commands are run in the VSCode terminal

1. Open VSCode
2. in `rescale/` run `source venv/bin/activate`
3. if pip is not found do a `pip3 install virtualenv` then a `pip3 install scrapy`
4. if pip is found do a `pip install scrapy`
5. cd into `webcrawler/webcrawler`
6. run `scrapy crawl rescale -o links.csv` to generate a `.csv` file of all the deep links
7. run `scrapy check` to run an assertion against the return value for all the links that are retured from the previous check. It should pass 3 contracts with no failures.

Main code is found under `webcrawler/webcrawler/spiders/__init__.py`