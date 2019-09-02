import sys
if len(sys.argv) < 3:
   print('You must give two command line arguments.')
   exit(1)
else
   print('You have provided', len(sys.argv) - 1, 'command line arguments.')
   print('They are: ',sys.argv[1:])
