##Telepathy

Linux: Open-Source, control, ownership, 

1. Power-UP your Raspberypi
2. Login with the unsername ``pi`` and password ``pi``

###Shell

Shell is a program that give you access to the operation system (OS) through keyboard commands. In the early days of computers that was the only way to control and input commands to the computer. Nowadays, we have access to a variety of graphical user interfaces (GUIs) read more [here](https://en.wikipedia.org/wiki/Unix_shell)

The user @ hostname waiting for commands
```bash
pi@hope01 ~ $
```
<img src="https://raw.githubusercontent.com/hacklabes/HOPE_Sessions/master/00_Telepathy/imgs/terminal.png" width="600">


1. Try your first command, type anything
2. Type the command and press ```Enter```

```bash
pi@hope01 ~ $ ls
```

The ``ls`` commmand list all the files in the current directory.

Most commmands accept arguments giving you the possibility to use different features of the same command.

You can try the command ``ls`` adding the paramenters ``-la``, which enable the command to print in list format showing file attributes:

```bash
pi@hope01 ~ $ ls -la
```

Also you can point out different paths from where to list files:

```bash
pi@hope01 ~ $ ls -la /usr/bin
```

###Exercises

####Looking Around

1. Check where you are with ``pwd``
2. Explore file types with the command ```file```
3. Explore file content with the command ``more`` 
4. List files from other directories
5. Try the command ``grep`` to search things inside files

####File Manipulation

1. Create a directory using ``mkdir``
2. Move yourself to the directory you just created using ``cd``
3. Confirm where you are, using ``pwd``
4. Feel free to create other directories inside the new one
5. Remove some of your folders using ``rm``
6. Copy and move directories (DO IT HERE ONLY! BE CAREFUL WITH THE SYSTEM FILES!)
7. Create a text file using the command ``nano``


####Network

1. Let's browse old-school ``lynx http://www.google.com``
3. Try do install a new software using ``sudo apt-get install cowsay``
4. Download a file from the internet using ``wget http://www.fact.co.uk/images/fact/fact-logo-white.gif``
5. Check your file using ``ls`` and ``file``
6. If you downloaded an image you can use ``fbi`` to visualize it

#####Connecting to your neighbor

7. Find your IP Address using ``ifconfig``
8. Find your hostname using ``hostname``
9. Ask neighbor for their IP address or their hostname
10. ``ping IP_ADDRESS`` or ``ping HOSTNAME.local`` to see if they are on the network
11. Start a chat as the Server: ``nc -l PORT``, or as the Client: ``nc IP_ADDRESS PORT``
12. Connect remotely to another computer ``ssh pi@HOSTNAME.local`` or ``ssh pi@IP_ADDRESS``

####Extras

1. Check how much space available you have using ``df -h``


###New Flow

####Simple

1. Check where you are with ``pwd``
2. Find all images on your path ``find . -name "*jpg"``
3. Go inside the folder where you did finde the images ``cd FOLDER_NAME``
4. Open the image ``fbi IMAGE_NAME.jpg``
5. Go back your home directory

#####Connecting to your neighbor

1. Find your IP Address using ``ifconfig``
2. Ask neighbor for their IP address
3. Connect remotely to another computer ``ssh pi@UR_FRIEND_IP_ADDRESS`` type ``yes`` then the ``username``and the ``password``
4. Grab a picture ``raspistill -o image.jpg``
5. Go back to your computer type ``exit```
6. Copy the picture from your friend computer to your computer ``scp pi@UR_FRIEND_IP_ADDRESS:image.jpg .`` 
7. Open the picture ``fbi image.jpg``


####References:
1. [Our Linux Reference card](https://github.com/hacklabes/HOPE_Sessions/blob/master/00_Telepathy/Linux_Reference_Card.md)
2. [Raspberrypi Foundation](https://www.raspberrypi.org/documentation/usage/terminal/)
