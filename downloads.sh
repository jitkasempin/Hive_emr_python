#!/bin/bash
set -e -x 
wget https://pypi.python.org/packages/source/s/scipy/scipy-0.11.0.tar.gz --no-check-certificate
wget https://pypi.python.org/packages/source/n/numpy/numpy-1.7.0.tar.gz --no-check-certificate
wget https://pypi.python.org/packages/source/s/simplejson/simplejson-3.1.2.tar.gz --no-check-certificate
wget https://pypi.python.org/packages/source/u/urlparse2/urlparse2-1.1.1.tar.gz --no-check-certificate
 
 
sudo tar xvzf numpy-1.7.0.tar.gz
sudo tar xvzf urlparse2-1.1.1.tar.gz
sudo tar xvzf scipy-0.11.0.tar.gz
sudo tar xvzf simplejson-3.1.2.tar.gz
 
cd urlparse2-1.1.1
sudo python setup.py install
 
cd ..
cd numpy-1.7.0
sudo python setup.py install
 
cd ..
cd scipy-0.11.0
sudo python setup.py install
 
cd ..
cd simplejson-3.1.2
sudo python setup.py install