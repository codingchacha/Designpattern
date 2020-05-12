class Singleton:
	__instance = None
	@staticmethod
	def get_obj():
		if __instance == None:
			Singleton()
		return __instance
	def __init__(self):
		if Singleton.__instance != None:
			raise Exception("object cannot be created for Singleton class")
		else:
			Singleton.__instance = self
			
		
		