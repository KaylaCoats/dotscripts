# dotscripts

To install, type these commands in your home directory:
```
git clone https://github.com/kaylacoats/dotscripts ~/.scripts
cd .scripts 
```

To run, type:
```
make (link|unlink)
```

make link will remove any files with the same name and create a symbolic link in your bin directory of the files listed in the Makefile

make unlink will copy the files into the bin directory and then remove the symbolic link
