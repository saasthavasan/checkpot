from .test import *
from honeypots.honeypot import ScanFailure
import mysql.connector
from mysql.connector import Error
class DefaultMysqlConnect(Test):
	name = "Default Mysql Connection"
	description = "Tests for the connection of mysql server"
	karma_value = 100

	def run(self):
		known_banner = "Access denied for user"
		flag = 0
		targetport =  self.target_honeypot.get_service_ports('smtp', 'tcp')
		targetip = self.target_honeypot.ip
		username = ['admin', 'daemon', 'root', 'nobody', 'authorize','username','db2admin', 'sql','pos','owner' ]
		passwd = ['Password', 'St@rt123', 'qwerty','bl4ck4ndwhite','letmein', 'master', 'hello','freedom','whatever','qazwsx']

		for i in range(len(passwd)):

			try:
				connection = mysql.connector.connect(host= targetip, port = 3306, user = username[i], password=passwd[i])
			except Error as e :
				message = str(e)
			if known_banner in message:
					flag = flag + 1
			else:
				self.set_result(TestResult.WARNING, "No default banners")
		if flag == 10:
			self.set_result(TestResult.OK, "Default", known_banner, "banner used")
			return
