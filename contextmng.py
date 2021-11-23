class ManagedFile:
    def __init__(self,filename):
        print('init')
        self.filename = filename
    def __enter__(self):
        print('enter')
        #allocated resource 
        self.file = open(self.filename,'w')
        #return the allocated resource 
        return self.file
    def __exit__(self, exc_type, exc_value,exc__traceback):
        #check if we correctly close the filename
        if self.file:
            self.file.close()
        print('exit')    

with ManagedFile ('notes.txt') as file:
    print('do something')
    file.write('some todo.....')               