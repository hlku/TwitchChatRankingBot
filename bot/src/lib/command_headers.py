# -*- coding: utf-8 -*-
from src.config.config import *

commands = {

#	'hi': {
#		'limit': 5,
#		'return': u'ㄤㄤ'
#	},

	'!8ball': {
		'limit': 5,
		'argc': 1,
		'return': 'command'
	}

#	'!randomemote': {
#		'limit': 180,
#		'argc': 0,
#		'return': 'command'
#	},

#	'!wow': {
#		'limit': 30,
#		'argc': 3,
#		'return': 'command'
#	}

}










for channel in config['channels']:
	for command in commands:
		commands[command][channel] = {}
		commands[command][channel]['last_used'] = 0
