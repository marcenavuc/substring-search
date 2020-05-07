import os


class BigIO:
    def __init__(self, filename):
        self.descriptor = None
        self.length = os.stat(filename).st_size
        self.filename = filename

    def __getitem__(self, index):
        if isinstance(index, slice):
            if index.step is not None:
                raise IOError("Step in indexing is not provide")
            if index.start >= index.stop:
                raise ValueError("Start must be lover than stop")
            self.descriptor.seek(index.start)
            return self.descriptor.read(index.stop - index.start).decode("utf-8")

        self.descriptor.seek(index)
        return self.descriptor.read(1).decode("utf-8")

    def __len__(self):
        return self.length

    def __enter__(self):
        self.read()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def read(self):
        # self.length = 0
        self.descriptor = open(self.filename, 'rb')
#         while self.descriptor.read(1):
#             self.length += 1
# #            self.descriptor.seek(self.length)
#         self.descriptor.seek(0)
        self.length = os.stat(self.filename).st_size

    def close(self):
        self.descriptor.close()
