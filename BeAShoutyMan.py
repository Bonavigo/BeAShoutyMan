import sys
from g_python.gextension import Extension
from g_python.hmessage import Direction, HMessage

extension_info = {
	"title": "Be a Shouty Man",
	"description": "A simple extension to shout all the time. And yes, the name is a joke with Horrible Histories.",
	"version": "1.0",
	"author": "BrunoBonamigo"
}

ext = Extension(extension_info, sys.argv)
ext.start()

def forceShout(message):
	(text, color, index) = message.packet.read('sii')
	message.is_blocked = True
	color = str(color)
	index = str(index)
	ext.send_to_server('{out:Shout}{s:"'+text+'"}{i:'+color+'}{i:'+index+'}')

ext.intercept(Direction.TO_SERVER, forceShout, 'Chat')
