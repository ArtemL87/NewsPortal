class Asd():
    _asd = 5

    @property
    def like(self):
        return self._asd

    @like.setter
    def like(self, values):
        self._asd += values

a = Asd()
a.like = 10
print(a.like)