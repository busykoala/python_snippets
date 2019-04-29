class Plop(list):
    def __init__(self, *args, **kwargs):
        super(Plop, self).__init__(args[0])

    def plop(self, index):
        return super(Plop, self).pop(index)

    def pop(self, *args, **kwarts):
        return super(Plop, self).pop(len(self) - 1)


hugo = Plop([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(hugo.plop(4))
print(hugo.pop())
