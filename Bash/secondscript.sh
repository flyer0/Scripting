#!/usr/bin/bash

#Funktionstest


chkfile(){
    echo "File $1 is"
    [ -r $1 ] && echo "readable"
    [ -x $1 ] && echo "executable"
}

chkfile /ur/bin/emacs

#Test der Variablen
#echo "Das Arbeitsverzeichnis der $SHELL ist $(pwd)"
exit