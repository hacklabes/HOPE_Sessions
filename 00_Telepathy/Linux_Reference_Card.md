##Linux Command-Line Reference

###General
<kbd>tab</kbd>: **THE** most useful thing. Ever. Use tab to auto-complete filenames and command names when using the command line. Left pinky FTW!  

<kbd>:arrow_up:</kbd>, <kbd>:arrow_down:</kbd>: Navigate command-line history back and forth, using the up- and down- arrow keys respectively.  

<kbd>ctrl</kbd>+<kbd>r</kbd>: Search through your command-line history.  

``man``: Very useful command; shows manual pages for other commands, e.g.: ``man ls``, gives you information about the ``ls`` command.  

``*``: Used as a wildcard to expand filenames in the command-line. e.g.: ``ls *.jpg``, shows all jpg image files in the current directory.  

###Navigation
``cd``: Change directory; this command is used to navigate through directories in the command-line. e.g.: `` cd some-directory/``, goes into a directory called ``some -directory``.  

``ls``: List; this command is used to list all files and directories inside a directory. e.g.: ``ls *.jpg``, lists all jpg image files in the current directory.  

``pwd``: Print Working Directory; this command prints the absolute path of the directory where the user is.  

``find``: Finds files starting from a specified directory. e.g.: ``find some-directory -name *.jpg``, finds all jpg image files inside ``some-directory`` and inside every directory inside ``some-directory``.  

``locate``: Finds files in computer without starting at current directory. e.g.: ``locate *.jpg``, finds all jpg image files in the filesystem.  

``..``: The double period is used to represent previous (parent) directory. e.g.: ``cd ..``, goes out from the current directory, and up to the directory that contains the current directory.  

###File operations
``cp``: Copy; this command copies files. If there's already a file with the name given, that file is overwritten (deleted). e.g.: ``cp image.jpg copy.jpg``, makes a copy of the file ``image.jpg``, and names the copy ``copy.jpg``.  

``mv``: Move; this command moves/renames files. e.g.: ``mv image.jpg new-name.jpg``, renames the file ``image.jpg`` to ``new-name.jpg``.  

``rm``: Remove; this command deletes files. e.g.: ``rm image.jpg``, removes the file named ``image.jpg``. ``rm -f *.jpg`` removes every jpg image file in current directory.  

``mkdir``: Make Directory; this command is used to create new directories within the current directory. e.g.: ``mkdir new-directory``, makes a new directory named ``new-directory``.  

``file``: This command is used to determine the type of a file. e.g.: ``file image.jpg``, prints out ``image.jpg: JPEG image data, JFIF standard 1.01``.  

###Text viewing/editing
``cat``: From conCATenating; this command displays a (text) file on the terminal. e.g.: ``cat poems.txt``, prints the text in ``poems.txt`` to the terminal, line by line.  ``cat poems.txt names.txt``, prints the text on both files ``poems.txt`` and ``names.txt`` to the terminal, line by line, one after the other.  

``more``: This commands also displays text files on the terminal, but waits for user input before moving to the next page. e.g.: ``more poems.txt``.  

``grep``: This command searches for words in text files and displays the entire line where they're found. e.g.: ``grep love poems.txt``, searches for the word *love* in the file ``poems.txt`` and prints out the lines where *love* is found.  

``nano``: Command line text editor. e.g.: ``nano poems.txt``, opens or creates a text file named ``poems.txt` to be edited on the command-line.  

###Disk space
``du``: Disk Usage; displays how much disk space is being used by the current directory, and any directory inside the current directory. e.g.: ``du -h``, prints out disk usage information; the ``-h`` option makes it "human-readable" (using bytes instead of disk "blocks").  

``df``: Disk Free; displays the ammount of space available in the whole system, and any other hard drives attached to it (USB, SD, etc). e.g.: ``df -h``, prints out available space information; the ``-h`` option, again, makes it "human-readable".  

###Networking
``ping``:  
``ifconfig``:  
``ssh``:  
``wget``:  
``lynx``:  
``nc``:  
``wall``:  

###Camera/Images
``raspistill``:  
``raspivid``:  
``fbi``:  
``gpicview``:  
``xview``:  
``omxplayer``:  
