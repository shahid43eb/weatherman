# weatherman
Completed Guide to setup project from scratch.
* Covered OS
    * Ubuntu
## Table of Contents
* [Environment Setup](#environment-setup)
    * [Python3.7](#python37)
    * [PIP](#pip)
* [Project Setup](#project-setup)
    * [Install, Create and Activate Virtual Environment](#install-create-and-activate-virtual-environment)
* [Project Execution](#project-execution)
## Environment Setup
> For this project, we need to install following technologies and tools:
### Python3.7
```
$ sudo apt-get install build-essential checkinstall
$ sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
$ cd /usr/src
$ sudo wget https://www.python.org/ftp/python/3.7.6/Python-3.7.6.tgz
$ sudo tar xzf Python-3.7.6.tgz
$ cd Python-3.7.6/
$ sudo ./configure
$ sudo make altinstall
$ python3.7 -V
```
For details, you can see [link](https://askubuntu.com/questions/682869/how-do-i-install-a-erent-python-version-using-apt-get)
### PIP
```
$ sudo apt-get install python3-pip
```
## Project Setup
```
$ git clone https://github.com/xhahid43eb/weatherman.git
```
### Install, Create and Activate Virtual Environment
```
$ pip3 install virtualenv
```
Create new python virtual environment with default python version set to 3.7
```
$ virtualenv --python=`which python3.7` ./venv
$ source venv/bin/activate
```
### Installing dependencies
```
$ pip install -e .
```

### Project Execution
>For a given year display the ​ highest temperature​ , ​ lowest
temperature​ and ​ humidity​ .
```
$ python weatherman.py /path/to/files-dir -e 2002
```
>For a given month display the ​ average highest temperature​ ,
average lowest temperature​ , ​ average mean humidity​ .
```
$ python weatherman.py /path/to/files-dir -a 2005/6
```
>For a given month draw one horizontal bar chart on
the console for the highest and lowest temperature on each day.
Highest in red and lowest in blue.
```
$ python weatherman.py /path/to/files-dir -c 2005/6
```

[Back to top](#weatherman)
