# !/bin/sh

# Пакеты необходимые для работы проектов на Python:
# Тестирование проводилось на Ubuntu 16.04.LTS

# Модули ОС
apt-cache show smbfs-utils | grep Package
apt-cache show smbfs-utils | grep Version
sudo apt-get install smbfs-utils

apt-cache show cifs-utils | grep Package
apt-cache show cifs-utils | grep Version
sudo apt-get install cifs-utils

apt-cache show smbclient | grep Package
apt-cache show smbclient | grep Version
sudo apt-get install smbclient

apt-cache show indicator-applet-complete | grep Package
apt-cache show indicator-applet-complete | grep Version
sudo apt-get install indicator-applet-complete

apt-cache show ttf-mscorefonts-installer | grep Package
apt-cache show ttf-mscorefonts-installer | grep Version
sudo apt-get install ttf-mscorefonts-installer

apt-cache show python-apt | grep Package
apt-cache show python-apt | grep Version
sudo apt-get install python-apt

# Работа с консолью
apt-cache show python-dialog | grep Package
apt-cache show python-dialog | grep Version
sudo apt-get install python-dialog

apt-cache show python-urwid | grep Package
apt-cache show python-urwid | grep Version
sudo apt-get install python-urwid

apt-cache show curl | grep Package
apt-cache show curl | grep Version
sudo apt-get install curl

# wxPython
apt-cache show python-wxgtk3.0 | grep Package
apt-cache show python-wxgtk3.0 | grep Version
sudo apt-get install python-wxgtk3.0

apt-cache show python-six | grep Package
apt-cache show python-six | grep Version
sudo apt-get install python-six

apt-cache show python-matplotlib | grep Package
apt-cache show python-matplotlib | grep Version
sudo apt-get install python-matplotlib

# БД
apt-cache show python-psycopg2 | grep Package
apt-cache show python-psycopg2 | grep Version
sudo apt-get install python-psycopg2

apt-cache show python-sqlalchemy | grep Package
apt-cache show python-sqlalchemy | grep Version
sudo apt-get install python-sqlalchemy

apt-cache show python-pyodbc | grep Package
apt-cache show python-pyodbc | grep Version
sudo apt-get install unixodbc unixodbc-dev freetds-bin freetds-dev tdsodbc python-pyodbc

# Office
apt-cache show unococnv | grep Package
apt-cache show unococnv | grep Version
sudo apt-get install unoconv

apt-cache show python-sane | grep Package
apt-cache show python-sane | grep Version
sudo apt-get install python-sane

apt-cache show python-reportlab | grep Package
apt-cache show python-reportlab | grep Version
sudo apt-get install python-reportlab

apt-cache show python-odf | grep Package
apt-cache show python-odf | grep Version
sudo apt-get install python-odf python-odf-doc

apt-cache show libreoffice-java-common | grep Package
apt-cache show libreoffice-java-common | grep Version
sudo apt-get install libreoffice-java-common

# В конце отобразим список установленных пакетов

echo
echo ============================
echo Установлены следующие пакеты
echo ============================
echo
echo Модули ОС
echo
apt-cache show smbfs-utils | grep Package
apt-cache show smbfs-utils | grep Version

apt-cache show cifs-utils | grep Package
apt-cache show cifs-utils | grep Version

apt-cache show smbclient | grep Package
apt-cache show smbclient | grep Version

apt-cache show indicator-applet-complete | grep Package
apt-cache show indicator-applet-complete | grep Version

apt-cache show ttf-mscorefonts-installer | grep Package
apt-cache show ttf-mscorefonts-installer | grep Version

apt-cache show python-apt | grep Package
apt-cache show python-apt | grep Version


echo
echo Работа с консолью
echo
apt-cache show python-dialog | grep Package
apt-cache show python-dialog | grep Version

apt-cache show python-urwid | grep Package
apt-cache show python-urwid | grep Version

apt-cache show curl | grep Package
apt-cache show curl | grep Version

echo
echo wxPython
echo
apt-cache show python-wxgtk3.0 | grep Package
apt-cache show python-wxgtk3.0 | grep Version

apt-cache show python-six | grep Package
apt-cache show python-six | grep Version

apt-cache show python-matplotlib | grep Package
apt-cache show python-matplotlib | grep Version

echo
echo БД
echo
apt-cache show python-psycopg2 | grep Package
apt-cache show python-psycopg2 | grep Version

apt-cache show python-sqlalchemy | grep Package
apt-cache show python-sqlalchemy | grep Version

apt-cache show python-pyodbc | grep Package
apt-cache show python-pyodbc | grep Version

echo
echo Office
echo
apt-cache show unococnv | grep Package
apt-cache show unococnv | grep Version

apt-cache show python-sane | grep Package
apt-cache show python-sane | grep Version

apt-cache show python-reportlab | grep Package
apt-cache show python-reportlab | grep Version

apt-cache show python-odf | grep Package
apt-cache show python-odf | grep Version

apt-cache show libreoffice-java-common | grep Package
apt-cache show libreoffice-java-common | grep Version

# Установка ic.pth
sudo cp ./ic.pth /usr/lib/python2.7/dist-packages
echo +++++++++++++++++++++++++++++++
echo |   Проект DEFIS установлен   |
echo +++++++++++++++++++++++++++++++
