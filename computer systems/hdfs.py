###########################
# Library Imports
###########################
from random import choice, shuffle

###########################
# Class Definitions
###########################
class DiskError(Exception):
    pass


class Disk:
    EMPTY = None

    def __init__(self, numblocks):
        self.__numblocks = numblocks
        self.__data = [Disk.EMPTY] * numblocks
        self.__ok = True

    @property
    def numblocks(self):
        return self.__numblocks

    @property
    def ok(self):
        return self.__ok

    def fail(self):
        self.__ok = False

    def write(self, block, data):
        if not self.ok:
            raise DiskError
        self.__data[block] = data

    def read(self, block):
        if not self.ok:
            raise DiskError
        return self.__data[block]

    # Returns how many empty blocks
    def space(self):
        return self.__data.count(Disk.EMPTY)

    # Returns a list of empty blocks
    def free(self):
        return [block for block, data in enumerate(self.__data) if data is Disk.EMPTY]


class Server:
    DISKBLOCKS = 10

    def __init__(self, numdisks):
        self.__numdisks = numdisks
        self.__disks = [Disk(Server.DISKBLOCKS) for _ in range(numdisks)]

    @property
    def numdisks(self):
        return self.__numdisks

    def write(self, disk, block, data):
        self.__disks[disk].write(block, data)

    def read(self, disk, block):
        return self.__disks[disk].read(block)

    def space(self):
        return sum(d.space() for d in self.__disks)

    # Returns a list of empty blocks for a given disk
    def free(self, disk):
        return self.__disks[disk].free()


class FileSystem:
    NUMDISKS = 10

    def __init__(self, numservers):
        self.__numservers = numservers
        self.__servers = [Server(FileSystem.NUMDISKS) for _ in range(numservers)]
        self.__fat = {
            "example.txt": [
                [(1, 3, 2), (2, 4, 5), (6, 3, 1)],  # Word 1 (Server, Disk, Block) * 3
                [(4, 2, 7), (8, 4, 4), (9, 5, 6)],  # Word 2 (Server, Disk, Block) * 3
            ]
        }

    @property
    def numservers(self):
        return self.__numservers

    def write(self, fname, fdata):
        blocks = fdata.split()  # Each 'block' of data is a word
        locations = []
        for b in blocks:
            pos = []
            space = [
                (server.space(), snum) for snum, server in enumerate(self.__servers)
            ]
            space.sort()
            # Write to the 3 servers with the most space
            for _, snum in space[-3:]:
                # Write block to disk and record it in the pos list
                # pos = [s,d,b]
                server = self.__servers[snum]
                for dnum in range(server.numdisks):
                    free = server.free(dnum)
                    if len(free) > 0:
                        block = choice(free)
                        try:
                            # write block to disk
                            self.__servers[snum].write(dnum, block, b)
                            # one line to build pos list
                            pos.append([snum, dnum, block])
                            break
                        # use free method of the server wish the disknum to find a free
                        except DiskError:
                            pass
                        # print(pos)

            locations.append(pos)
        self.__fat[fname] = locations

    def read(self, fname):
        fdata = []
        for x in self.__fat[fname]:
            for data in x:
                # print(data)
                try:
                    r = self.__servers[data[0]].read(data[1], data[2])
                    fdata.append(r)
                    break
                except DiskError:
                    pass
        return " ".join(fdata)


###########################
# Main Program
###########################

NUMSERVERS = 10
hdfs = FileSystem(NUMSERVERS)

filename = "hello.txt"
file = "The quick brown fox jumps over the lazy dog"

hdfs.write(filename, file)

print(hdfs.read(filename))
