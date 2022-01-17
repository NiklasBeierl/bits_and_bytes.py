# Bits and bytes in python
Some material I prepared for a short presentation / workshop on handling binary data in python.

## Preparation

Some things to set up **before** the workshop. Get in touch with me if you are experiencing any problems. 

### Python3 on UNIX
Please make sure that you have all the below installed on your system:
- Linux / MacOS, a Linux VM or Windows Subsystem for Linux  

In that Unix environment:
- Python >= 3.3
- Pip
- [Poetry](https://python-poetry.org/docs/) (optional)

### Virtual ENV / Python dependencies

If you have poetry installed:  
Run `poetry config virtualenvs.in-project true` if you want your venv to be in `<project>/.venv`. 
To create the venv and install the dependencies, run: `poetry install`.

If you do not have poetry installed:  
Create a venv: `python3 -m venv .venv`  
Activate it: `source .venv/bin/activate`  
And install the dependencies: `pip install -r ./requirements.txt`

### Data
Download our sample data and place it in `<project>/data/`.  
(Not provided in GitHub.)

### IDE
I highly recommend installing an IDE Like VS Code or PyCharm for the sake of easier debugging.  
If you are using VS Code, you will need the `ms-python` extension.  
If you happen to use VS Code **OSS**, I recommend the `ms-pyright` extension for static type checking and linting.  


For those who love using VIM there are the [vscodevim](https://open-vsx.org/extension/vscodevim/vim) and 
[IdeaVim](https://plugins.jetbrains.com/plugin/164-ideavim) (f. PyCharm) extensions.
