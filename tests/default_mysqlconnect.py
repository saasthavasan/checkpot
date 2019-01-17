from .test import *
from honeypots.honeypot import ScanFailure
import mysql.connector
from mysql.connector import Error
class DefaultMysqlConnect(Test):
	name = "Default Mysql Connection"
	description = "Tests for the connection of mysql server"
	karma_value = 100
	def run(self):

	"""Check if content matches any known content"""
		
		known_banners = { 
				b'Access denied for user': "mysqlhoneypotd",
				}

		targetport =  self.target_honeypot.get_service_ports('smtp', 'tcp')
		targetip = self.target_honeypot.ip
		if not target_port:
			self.set_result(TestResult.NOT_APPLICABLE, "No open ports found!")
			return
			
		username = ['admin', 'daemon', 'root', 'nobody', 'authorize','username','db2admin', 'sql','pos','owner' ]
		passwd = ['Password', 'St@rt123', 'qwerty','bl4ck4ndwhite','letmein', 'master', 'hello','freedom','whatever','qazwsx']
		
		for i in range(len(passwd)):

			try:
				connection = mysql.connector.connect(host= targetip, port = targetport, user = username[i], password=passwd[i])
			except Error as e :
				self.set_result(TestResult.UNKNOWN, e)
				continue
			if banner in known_banners:
				self.set_result(TestResult.WARNING, "Default", known_banners[banner], "banner used")
				return
			else:
				self.set_result(TestResult.OK, "No default banners")

