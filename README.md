# ntnu-gpa-calculator
NTNU grade fetcher and GPA calculator

![Screenshot](http://imgur.com/0pc0B4O.jpg)

# Prerequisites
* Python3
* Chrome v58-60
* Feide NTNU user

# Installation for 64-bit Ubuntu 16.04
```
$ git clone https://github.com/stekern/ntnu-gpa-calculator.git && cd ntnu-gpa-calculator/
$ pip3 install selenium
$ curl -O https://chromedriver.storage.googleapis.com/2.31/chromedriver_linux64.zip
$ unzip chromedriver_linux64.zip && rm chromedriver_linux64.zip
$ chmod +x chromedriver && sudo mv -f chromedriver /usr/local/bin/chromedriver
```

# Usage
`$ python3 gpa_fetcher.py`
