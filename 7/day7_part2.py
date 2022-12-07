import numpy as np

#Inspired by code from mscroggs
from abc import ABC, abstractmethod

class FileSystem:
    def __init__(self):
        self.dirs = []
        self.home = None

class Base:
    def __init__(self, name, fs):
        self.name = name
        self.fs = fs
        self.parent = None

    @abstractmethod
    def size(self):
        pass

class File(Base):
    def __init__(self, size, name, fs):
        super().__init__(name, fs)
        self._size = size

    def size(self):
        return self._size

class Dir(Base):
    def __init__(self, name, fs):
        super().__init__(name, fs)
        self.contents = []

    #Count the size of every item in the directory contents
    def size(self):
        return sum(i.size() for i in self.contents)

    def cd(self, fname):

        #Move out a directory
        if fname == '..':
            return self.parent

        #Find the directory with the name matching where we need to move
        for i in self.contents:
            if i.name == fname:
                return i

    #Add a new sub directory to the directory contents
    def mkdir(self, fname):
        d = Dir(fname, self.fs)
        d.parent = self
        self.contents.append(d)
        self.fs.dirs.append(d)

    #Add a new file to the directory contents
    def touch(self, fname, size):
        f = File(size, fname, self.fs)
        self.contents.append(f)

fs = FileSystem()
dirs = []
current_dir = None
with open("7/data.csv") as f:
    for commands in f.read().split("$ ")[1:]:
        commands = commands.strip()
        if commands.startswith("cd "):
            fname = commands[3:]
            if current_dir is None:
                assert fname == "/"
                current_dir = Dir("/", fs)
                fs.home = current_dir
            else:
                current_dir = current_dir.cd(fname)
        else:
            assert commands.startswith("ls")
            for line in commands.split("\n")[1:]:
                size, name = line.split()
                if size == "dir":
                    current_dir.mkdir(name)
                else:
                    current_dir.touch(name, int(size))



d_sizes = np.array(list(d.size() for d in fs.dirs))
home_size = fs.home.size()
print(f"Home size: {home_size}")
free_space = 70000000 - home_size
print(f"Free space: {free_space}")
space_needed = 30000000 - free_space
print(f"Additional space needed: {space_needed}")
print(f"Min deletable file size: {np.amin(d_sizes[d_sizes >= space_needed])}")