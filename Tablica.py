
import random


class Tablica:
    def __init__(self, n):
        self.n = n
        self.tab = [0] * n

    def wypelnij(self, a, b):
        for i in range(self.n):
            self.tab[i] = random.randint(a, b)

    def minimum(self):
        mini = self.tab[0]
        for i in self.tab:
            if i < mini:
                mini = i
        return mini

    def maksimum(self):
        maks = self.tab[0]
        for i in self.tab:
            if i > maks:
                maks = i
        return maks

    def maksimum2(self):
        if self.tab[0] > self.tab[1]:
            maks = self.tab[0]
            maks2 = self.tab[1]
        else:
            maks = self.tab[1]
            maks2 = self.tab[0]
        for i in self.tab[2:]:
            if i > maks:
                maks2 = maks
                maks = i
            elif i > maks2 and i != maks:
                maks2 = i
        return maks2

    def znajdz(self, a):
        for i in range(len(self.tab)):
            if self.tab[i] == a:
                return i
        return -1

    def __str__(self):
        return str(self.tab)
