import os
import abc
from .csv import CSVFile
from .docx import DocxFile

class SwiftDoc(metaclass=abc.ABCMeta):
    def __init__(self, args):
        self.filename = args
    
    def read(self):
        self._open()
        self._read_contents()
        self._close()
        
    def write(self, contents):
        self._open()
        self._write_contents(contents)
        self._close()
        
    def handle_file(self):
        filename, extension = os.path.splitext(self.args.file) # input arg /path/to/file.csv
        
        if extension == '.csv':
            file = CSVFile(self.args)
        elif extension == '.docx':
            file = DocxFile(self.args)
        # [ ] TODO: support additional file types
            
        # elif extension == '.txt':
        # elif extension == '.json':
        # elif extension == '.xml': 
        #     file = DocXMLFile(self.args)
        else:
            raise ValueError(f"Unsupported file type: {extension}")
        
        method_name = self.args.subcommand.replace("-", "_")
        method = getattr(file, method_name)
        
        if method is None:
            raise ValueError(f"Invalid subcommand: {self.args.subcommand}")

        method(self.args.contents)
        
    @abc.abstractclassmethod
    def _open(self):
        pass
    
    @abc.abstractclassmethod
    def _read_contents(self):
        pass
    
    @abc.abstractclassmethod
    def _write_contents(self, contents):
        pass
    
    @abc.abstractclassmethod
    def _close(self):
        pass
    
