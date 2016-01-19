#!/bin/bash
git clone https://github.com/zxing/zxing.git
cd zxing
mvn install
cd core
wget http://central.maven.org/maven2/com/google/zxing/core/2.2/core-2.2.jar
mv core-2.2.jar core.jar # Rename
mvn install
cd ../javase
wget http://central.maven.org/maven2/com/google/zxing/javase/2.2/javase-2.2.jar 
mv javase-2.2.jar javase.jar # Rename
mvn install
cd ../
git clone git://github.com/oostendo/python-zxing.git
python setup.py install
