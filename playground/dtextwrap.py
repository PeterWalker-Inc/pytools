import textwrap

text = '''
The textwrap module provides some 
convenience functions, as well as TextWrapper,                           the class 
     that does                          
     all the work. If you’re just wrapping or filling one or two text strings, the
                                                convenience functions should be good enough; otherwise, you should use an instance of TextWrapper for efficiency.
'''

real = '''Example:
    netcat.py -t 192.168.1.108 -p 5555 -l -c # command shell
    netcat.py 
    -t 192.168.1.108 -p 5555 -l -u=mytest.txt # upload to file
    netcat.py -t 192.168.1.108 -p 5555 -l -e=\"cat /etc/passwd\" # execute command
    echo 'ABC' | ./netcat.py -t 192.168.1.108 -p 135 # echo text to server port 135
    netcat.py -t 192.168.1.108 -p 5555 # connect to server
'''

print(f"wrap: {textwrap.wrap(text)}")
print(f"shorten: {textwrap.shorten(text, width=40)}")
print(f"dedent: {textwrap.dedent(text)}")
print(f"indent: {textwrap.indent(text, '', lambda line: True)}")
