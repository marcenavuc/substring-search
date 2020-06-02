class BigIO:
    def __init__(self, io_object):
        self.descriptor = io_object
        self.descriptor.seek(0, 2)
        self.length = self.descriptor.tell()
        self.descriptor.seek(0)

    def __getitem__(self, index):
        if isinstance(index, slice):
            if index.step is not None:
                raise IOError("Step in indexing is not provide")
            if index.start >= index.stop:
                raise ValueError("Start must be lower than stop")

            self.descriptor.seek(index.start)
            return self.descriptor.read(index.stop - index.start)

        self.descriptor.seek(index)
        return self.descriptor.read(1)

    def __len__(self):
        return self.length

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def readfile(self, filename):
        with open(filename) as file:
            self.descriptor = file
            return self

    def close(self):
        self.descriptor.close()
