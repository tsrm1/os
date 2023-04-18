# https://docs.python.org/3/library/os.html

import os
import sys

img_folder = './img/'
file_name = 'Text Document.txt'

print('os.name                                  ->', os.name)                       # name of the operating system: 'posix', 'nt', 'java'
# print('sys.getfilesystemencoding()              ->', sys.getfilesystemencoding())   # utf-8
# print('sys.getwindowsversion()                  ->', sys.getwindowsversion())       # Return a named tuple describing the Windows version
# print('sys.getwindowsversion().major            ->', sys.getwindowsversion().major) # Return Windows version
# print('sys.getwindowsversion()[0]               ->', sys.getwindowsversion()[0])    # Return Windows version

# print('os.ctermid()                              ->', os.ctermid()) # Return the filename corresponding to the controlling terminal of the process.

print('os.environ                               ->', os.environ)                    # A mapping object where keys and values are strings that represent the process environment

print('__________________________________________________________________________')
print("os.environ['PROCESSOR_ARCHITECTURE']     ->", os.environ['PROCESSOR_ARCHITECTURE'])
print("os.environ['PROCESSOR_IDENTIFIER']       ->", os.environ['PROCESSOR_IDENTIFIER'])
print("os.environ['PROCESSOR_LEVEL']            ->", os.environ['PROCESSOR_LEVEL'])
print("os.environ['NUMBER_OF_PROCESSORS']       ->", os.environ['NUMBER_OF_PROCESSORS'])
print("os.environ['PROCESSOR_REVISION']         ->", os.environ['PROCESSOR_REVISION'])
print("os.environ['COMPUTERNAME']               ->", os.environ['COMPUTERNAME'])  
print("os.environ['OS']                         ->", os.environ['OS'])
print("os.environ['LANG']                       ->", os.environ['LANG'])
print("os.environ['SYSTEMDRIVE']                ->", os.environ['SYSTEMDRIVE'])
print("os.environ['WINDIR']                     ->", os.environ['WINDIR'])
print("os.environ['USERNAME']                   ->", os.environ['USERNAME'])        
print("os.environ['USERPROFILE']                ->", os.environ['USERPROFILE'])
print('__________________________________________________________________________')
print("os.getenv('COMPUTER', default=None)      ->", os.getenv('COMPUTER', default=None)) 
print("os.getenv('COMPUTERNAME', default=None)  ->", os.getenv('PROCESSOR_ARCHITECTURE', default=None)) 
print("os.getenv('COMPUTERNAME', default=None)  ->", os.getenv('PROCESSOR_IDENTIFIER', default=None)) 
print("os.getenv('COMPUTERNAME', default=None)  ->", os.getenv('PROCESSOR_LEVEL', default=None)) 
print("os.getenv('COMPUTERNAME', default=None)  ->", os.getenv('NUMBER_OF_PROCESSORS', default=None)) 
print("os.getenv('COMPUTERNAME', default=None)  ->", os.getenv('PROCESSOR_REVISION', default=None)) 
print("os.getenv('COMPUTERNAME', default=None)  ->", os.getenv('COMPUTERNAME', default=None)) 
print("os.getenv('COMPUTERNAME', default=None)  ->", os.getenv('OS', default=None)) 
print("os.getenv('COMPUTERNAME', default=None)  ->", os.getenv('LANG', default=None)) 
print("os.getenv('COMPUTERNAME', default=None)  ->", os.getenv('SYSTEMDRIVE', default=None)) 
print("os.getenv('COMPUTERNAME', default=None)  ->", os.getenv('WINDIR', default=None)) 
print("os.getenv('COMPUTERNAME', default=None)  ->", os.getenv('USERNAME', default=None)) 
print("os.getenv('COMPUTERNAME', default=None)  ->", os.getenv('USERPROFILE', default=None)) 
print('__________________________________________________________________________')

file_name_binary = os.fsencode(img_folder + file_name)
print('os.fsencode(img_folder + file_name)      ->', file_name_binary)  # Encode path-like filename to the filesystem encoding and error handler; return bytes unchanged.
file_name_sring = os.fsdecode(file_name_binary)
print('os.fsdecode(file_name_binary)            ->', file_name_sring) # is the reverse function

print('os.fspath(file_name_sring)               ->', os.fspath(file_name_sring)) # Return the file system representation of the path

print("os.get_exec_path(env=None)               ->", os.get_exec_path(env=None)) # Returns the list of directories that will be searched for a named executable, similar to a shell, when launching a process. env, when specified, should be an environment variable dictionary to lookup the PATH in

print("os.getlogin()                            ->", os.getlogin()) # Return the name of the user logged in
print("os.getpid()                              ->", os.getpid()) # Return the current process id.
print("os.getppid()                             ->", os.getppid()) # Return the parent’s process id
print("os.putenv('telegram','6008437726')       ->", os.putenv('telegram','6008437726')) # (key, value, /). Set the environment variable named key to the string value
print("os.getenv('telegram', default=None)      ->", os.getenv('telegram', default=None)) 
print("os.unsetenv('telegram')                  ->", os.unsetenv('telegram')) # Unset (delete) the environment variable named key
      

print('__________________________________________________________________________')

