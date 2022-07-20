Keylogger:

Main Objective:
1. Record keystrokes on a computer
2. Send report logs back within a time interval (send to an email)

To Add:

On/Off switch - whre attacker can turn keylogger on and off remotely 

Advanced Level: 

Undetectable keylogger through USB or trojan
https://github.com/Veil-Framework/Veil

Designing a keylogger in python
https://www.geeksforgeeks.org/design-a-keylogger-in-python/

Libs 
Pyhook:

a wrapper for global input hooks in windows. 

Pywin32:

extensions for windows: to install pywin32 system files

windows and linux 

how to make a keylogger in python 
https://www.thepythoncode.com/article/write-a-keylogger-python
Best Sample with discussion

SUDO 

classes to be built:
1. EmailCreate - settings to send log to (SMTP setup possibly)
2. KeyboardEvents - register each character with capability to recongize special characters 
3. Timinginterval - loop that starts after first keystroke 
4. FileCreation - creation of txt file to send to email.
