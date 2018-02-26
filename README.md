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

- Python 3.5
- See `requirements.txt` and `setup.py`

## Authors

[**Kavdi Hodgson**](https://github.com/kavdi)

[**Gabriel Meringolo**](https://github.com/gabrielx52)

[**Chris Closser**](https://github.com/ChristopherSClosser)

[**Matt Favoino**](https://github.com/famavott)

[**Bernard Bass**](https://github.com/ZerooCool) - For french translation.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

- Beautiful Soup / Crummy
- Requests library
- [Pypwned](https://github.com/kernelmachine/haveibeenpwned)
- [Inteltechniques.com](https://inteltechniques.com/menu.html)


# French translation

## Social Recon

### Sous Debian Stretch et Kali Linux 2018
git clone https://github.com/famavott/osint-scraper.git<br/>
cd osint-scraper

# Pour Debian Stretch
apt-get install python-pip<br/>
apt-get install python3<br/>
apt-get install python3-pip

# Pour Kali Linux
apt-get install python3-venv

Créer un environnement virtuel en python3 et activer le avant d'installer les éléments nécessaires.<br/>
Passer en root<br/>
python3 -m venv ENV<br/>
source ENV/bin/activate<br/>
pip install -r requirements.txt<br/>
pip install -e .<br/>
pserve development.ini<br/>

Vous pouvez voir les informations suivante dans votre terminal :<br/>
Starting server in PID 2408.<br/>
Serving on http://localhost:6543<br/>
Serving on http://localhost:6543<br/>

Lancer l'outil depuis votre navigateur avec l'adresse http://localhost:6543<br/>

Une fois la machine redémarrée, relancer le service de la façon suivante :<br/>
Se placer dans le dossier de osint-scraper<br/>
python3 -m venv ENV<br/>
source ENV/bin/activate<br/>
pserve development.ini

[[https://github.com/ZerooCool/osint-scraper/blob/patch-1/pictures/social-recon.png|Social-Recon]]
