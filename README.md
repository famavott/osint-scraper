[![Build Status](https://travis-ci.org/famavott/osint-scraper.svg?branch=master)](https://travis-ci.org/famavott/osint-scraper)

[![Coverage Status](https://coveralls.io/repos/github/famavott/osint-scraper/badge.svg?branch=master)](https://coveralls.io/github/famavott/osint-scraper?branch=master)

# Social Recon

This application locates and compiles information about online personalities, given a username and/or email address. Use this to investigate your own online presence, summarize the digital footprint of someone you know, or uncover the person behind a specific username.

## Getting Started

- Clone or fork the repo to your machine.
- Once downloaded, `cd` into the `osint-scraper` directory.
- Begin a new virtual environment with Python 3 and activate it.
- `cd` into the next `osint-scraper` directory. It should be at the same level of the `setup.py` file.
- `pip install -e .` on the command line to install all dependencies.
- `$ pserve development.ini --reload` to serve the application on `http://localhost:6543`

### Dependencies

See `requirements.txt` and `setup.py`

## Authors

[**Kavdi Hodgson**](https://github.com/kavdi)

[**Gabriel Meringolo**](https://github.com/gabrielx52)

[**Chris Closser**](https://github.com/ChristopherSClosser)

[**Matt Favoino**](https://github.com/famavott)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

- Beautiful Soup / Crummy
- Requests library
- [Pypwned](https://github.com/kernelmachine/haveibeenpwned)
- [Inteltechniques.com](https://inteltechniques.com/menu.html)

