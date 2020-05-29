"""study / entertainment -> ds python / lipstick.mp3/Movies - batman , superman """
class File:
	def __init__(self , name , type):
		self.name = name
		self.type = type
		
class Folder:
	def __init__(self , name , type):
		self.name = name
		self.file_list = []
		self.folder_list = []
		self.type = type

	def add_file(self , file):
		self.file_list.append(file)
	def add_folder(self , folder):
		self.folder_list.append(folder)
	def show_files_folder(self):
		for item in self.folder_list:
			print(item.name + "--->" + item.type)
		for item in self.file_list:
			print(item.name + "--->" + item.type)
		
		



study = Folder("Study" , "folder")
entertainment = Folder("Entertainment" , "folder")
movies = Folder("Movie" , "folder")
ds = File("data_structure", ".txt file")
python = File("python" , ".py file")
lipstick = File("Lipstick" , "mp3 file")
batman = File("Batman" , ".mp4 file")
superman = File("Superman" , ".mp4 file")
study.add_file(ds)
study.add_file(python)
entertainment.add_folder(movies)
entertainment.add_file(lipstick)
movies.add_file(batman)
movies.add_file(superman)
study.show_files_folder()
entertainment.show_files_folder()
movies.show_files_folder()
# your code goes here