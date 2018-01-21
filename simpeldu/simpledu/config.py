class BaseConfig(object):
	
	SECRET_KEY = 'makesure to set a very secret key'

class DevelopmentConfig(BaseConfig):
	"""Development"""
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root@localhost:3306/simpledu?charset=utf8'

class ProductionConfig(BaseConfig):
	"""production"""
	pass

class TestingConfig(BaseConfig):
	"""test"""
	pass
		

configs = {
	'development': DevelopmentConfig,
	'production': ProductionConfig,
	'testing': TestingConfig
}
