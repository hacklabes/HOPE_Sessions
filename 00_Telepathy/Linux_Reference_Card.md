##Linux Command-Line Reference

###General
<kbd>tab</kbd>: **THE** most useful thing. Ever. Use tab to auto-complete filenames and command names when using the command line. Left pinky FTW!  

<kbd>:arrow_up:</kbd>, <kbd>:arrow_down:</kbd>: Navigate command-line history back and forth, using the up- and down- arrow keys respectively.  

<kbd>ctrl</kbd>+<kbd>r</kbd>: Search through your command-line history.  

``man``: Very useful command; shows manual pages for other commands, e.g.: ``man ls``.  

``*``: Used as a wildcard to expand filenames in the command-line. e.g.: ``ls *.jpg``, shows all jpg image files in the current directory.  

###Navigation
``cd``: Change directory; this command is used to navigate through directories in the command-line. e.g.: `` cd someDirectory/``, goes into a directory called ``someDirectory``.  

``ls``: List; this command is used to list all files and directories inside a directory. e.g.: ``ls *.jpg``, lists all jpg image files in the current directory.  

``pwd``: Print Working Directory; this command prints the absolute path of the directory where the user is.  

``find``: Finds files starting from a specified directory. e.g.: ``find someDirectory -name *.jpg``, finds all jpg image files inside ``someDirectory`` and inside every directory inside ``someDirectory``.  

``locate``: Finds files in computer without starting at current directory. e.g.: ``locate *.jpg``, finds all jpg image files in the filesystem.  

``..``: The double period is used to represent previous (parent) directory. e.g.: ``cd ..``, goes out from the current directory, and up to the directory that contains the current directory.  

###File operations
``cp``:  
``mv``:  
``rm``:  
``mkdir``:  
``file``:  

###Text viewing/editing
``cat``:  
``more``:  
``grep``:  
``nano``:  

###Disk space
``du``:  
``df``:  

###Networking
``ping``:  
``ifconfig``:  
``ssh``:  
``wget``:  
``lynx``:  
``nc``:  
``wall``:  

###Running programs
``ps``:  
``kill``:  
``bg``:  
``fg``:  

###Camera/Images
``raspistill``:  
``raspivid``:  
``fbi``:  
``omxplayer``:  
