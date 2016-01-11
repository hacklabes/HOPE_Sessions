##Telepathy

1. Power-UP your Raspberypi
2. Login with the unsername ``pi`` and password ``pi``

###Shell

Shell is a program that give you access to the operation system (OS) through the keyboard commands, before, in the early days of computers
that was the only way to control and input commands to the computer. Nowdays, we have access to a variety of graphical user interfaces (GUIs)
read more [here](https://en.wikipedia.org/wiki/Unix_shell)

The user @ hostname waiting for commands
```bash
pi@hope01 ~ $
```
<img src="https://raw.githubusercontent.com/hacklabes/HOPE_Sessions/master/00_Telepathy/imgs/terminal.png" width="600">


1. Try your first command , type anything
2. Type the command and press ```Enter```

```bash
pi@hope01 ~ $ ls
```

The ``ls`` commmand list all the files in the current directory 

Mostly commmand accepts arguments given you the possibility to use different features of the same command.

You can try the command ``ls`` adding the paramenters ``-la``, that enables the command to print in the list format showing the files attributes

```bash
pi@hope01 ~ $ ls -la
```

Also you can point out different paths for where to list files

```bash
pi@hope01 ~ $ ls -la /usr/bin
```

###Exercises


####Looking Around

1. Check where you are with ``pwd``
2. Explore files types around with the command ```file```
3. Explore files content with the command ``more`` 
4. List files from other directories
5. Try the command ``grep`` to search things inside files

####File Manipulation

1. Create a directory using ``mkdir``
2. Move yourself to the directory you just created using ``cd``
3. Confirms where you are using ``pwd``
4. Fell free to create other directories inside the new one
5. Remove some of your folders using ``rm``
6. Copy and move directories (DO IT ONLY HERE, BE CAREFUL WITH THE SYSTEM FILES)
7. Create a text file using the command ``nano``


####Network

1.Let's browse old schooll ``lynx WEBSITE``
2. Starting download a file from the internet using ``wget``
3. Check your file, use ``ls``, ``file``
4. If you download an image you can use ``fbi`` to visualize it

Connecting to your neighborhood 

5. Find your IP Address using ``ifconfig``
6. Find your hostname using ``hostname``
7. Ask neighborhood their IP address or their hostname
8. ``ping IP_ADDRESS`` or ``ping HOSTNAME.local`` see if their are alive 
9. Start a chat be the Server: ``nc -l PORT`` or be the Client: ``nc IP_ADDRESS PORT``
10. Connect remotely to another computer ``ssh pi@HOSTNAME.local`` or ``ssh pi@IP_ADDRESS``



####Extras

1. Check how much space available you have using ``df -h```
2. 





####References:
1. [Our Linux Reference card](https://github.com/hacklabes/HOPE_Sessions/blob/master/00_Telepathy/Linux_Reference_Card.md)
2. [Raspberrypi Foundation](https://www.raspberrypi.org/documentation/usage/terminal/)
