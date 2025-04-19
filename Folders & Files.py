# OS module important methods
os.getcwd()
os.listdir()
os.path.isdir('/Users/yogeshpoola/Downloads/DataVidhya Data')
os.path.isfile('/Users/yogeshpoola/Downloads/DataVidhya Data')
os.walk('/Users/yogeshpoola/Downloads/DataVidhya Data')
os.path.splitext(file)
+ os.getcwd()                                            => get current working directory
+ os.chdir(<path>)                                    => change directory 
+ os.listdir()	                                            => list directory
+ os.mkdir(<dirname>)                           => create a directory
+ os.makedirs(<dirname>)                    => make directories recursively
+ os.rmdir(<dirname>)	                   => remove directory
+ os.removedirs(<dirname>)                => remove directory recursively
+ os.rename(<from>, <to>)                   => rename file
+ os.stat(<filename>)                            => print all info of a file
+ os.walk(<path>)	                          => traverse directory recursively
+ os.environ		                                 => get environment variables
+ os.path.join(<path>, <file>)              => join path without worrying about /
+ os.path.basename(<filename>)     => get basename
+ os.path.dirname(<filename>)         => get dirname
+ os.path.exists(<path-to-file>)         => check if the path exists or not
+ os.path.splitext(<path-to-file>)      => split path and file extension
+ dir(os)			                               => check what methods exists

#Looping through folders and subfolders
path='/Users/yogeshpoola/Downloads/DataVidhya Data'
for directory,folder,files in os.walk('/Users/yogeshpoola/Downloads/DataVidhya Data'):
    print(f'CurrentPath: {directory}')
    print(f'foldersList: {folder}')
    print(f'filesList: {files}')
    print(f'no.of files/folders: {len(files)}')
    print()

#splitext (Split Extension)
for a,b,c in os.walk(newPath):
    print(a)
    print(b)
    print(c)
    for i in c:
        print(os.path.splitext(i))
