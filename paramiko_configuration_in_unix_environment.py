#------------------------ PARAMIKO INSTALLATION ----------------------------


asn1crypto
bcrypt
bcrypt-3.1.4
cffi-1.11.4
cryptography-1.7.2
enum34-1.1.6
idna-2.5
ipaddress-1.0.19
paramiko-2.4.0
pyasn1-0.4.2
pycparser-2.18
PyNaCl-1.2.1
setuptools-14.3.1
six-1.11.0
xlutils

#---------------------------------------------------------------------------------


Paramiko - Pre-requisite - 
pyasn1 (>=0.1.7)
pynacl (>=1.0.1)
cryptography (>=1.5)
bcrypt (>=3.1.3)

2 - For installation of Cryptography CFFI required, LIBFFI Unix installation required.

Root Access - sudo yum install gcc libffi-devel python-devel  - Fedora & RHEL

sudo apt-get install build-essential libffi-dev python-dev - Debian/Ubuntu



3 - For OpenSSL connection -

sudo apt-get install libssl-dev ( Debian Ubuntu)

sudo yum install openssl-devel (Fedora, CentOs, RHEL)