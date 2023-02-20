# AuctionServe
Software to facilitate Auctions the Easy Way

## Dependencies
Below is a List of Dependencies that this project requires. None of these are needed if you are going to run this as a client since the installation of these dependencies will be handled by the installer.

 * Python Flask Library

## Structure of the Project
The Main Flask File `index.py` needs to be in the root dir of the project.
The subdirectories, static and templates are specifically named so that Flask can see the files under there.
If the file you are referencing is in one of those directories you shouldn't need to prefix it.
```commandline
AuctionServe        # Project Root
 |
 -- index.py        # Main Python file
 |
 -- static          # Directory for all CSS and images
 |
 -- Templates       # Directory for all html Templates
```