# FontCrawler

## What is this project?

Almost every website uses custom fonts to enchance text on their webpages.

FontCrawler is a web app that allows you to get those fonts and download them

### Prerequisites (Or use Docker)

- [Python 3.4](https://www.python.org/downloads/) or higher
- [Rabbitmq](https://www.rabbitmq.com/download.html)
- [Postgresql](https://www.postgresql.org/download/)


### Configuration

This project config have been splitted into different files:

general config is placed in [fontcrawler/project_settings/base.py](fontcrawler/project_settings/base.py),
example developement config is in [fontcrawler/project_settings/local.py](fontcrawler/project_settings/local.py)

### Run with docker

Local config is ready to use with docker compose.

```bash
$ docker-compose up
```

### License

This project is licensed under MIT license - see the [LICENSE.md](LICENSE.md) for details

### Author:

Oleksandr Zinkevych [github](https://github.com/olekthunder)
