from itertools import combinations
from math import ceil

SKIP = False

class PizzaSlices():
    def __init__(self,input_file):
        f_in = open(input_file, 'r')
        f_lines = f_in.readlines()

        [M,N] = f_lines[0].split()
        S = [int(k) for k in f_lines[1].split()]

        self.M, self.N, self.S = int(M),int(N),S
        self.min_diff=[[], self.M]
        self.skip = []
        self.skip_flag = True
        self.counter = 0
        self.n = -1
        self.previous_diff = M

    def find_n(self,):
        for i in range(1,len(self.S)):
            print(i,sum(self.S[len(self.S)-i:]),self.M)
            if sum(self.S[len(self.S)-i:])<self.M:
                continue
            else:
                self.n = i
                break
        if self.M - sum(self.S[:self.n]) > sum(self.S[len(self.S)-self.n:]) - self.M:
            print('Reversing string')
            self.S.reverse()
            self.skip_flag = False

    def get_combinations(self):
        self.skip = []
        for i in combinations(self.S, self.n):
            if self.skip_flag:
                if i[:-1]== self.skip:
                    continue
                if previous_diff[0] < 0 and previous_diff[1] > 0:
                    self.skip = [self.i[:-1]]
                    continue
            else:
                if i[:-1]==self.skip:
                    continue

            self.get_min(i,sum(i))
            if self.min_diff[1]==0:
                print('Done',self.min_diff)
                return
        return

    def get_min(self,items,sum):
        self.counter += 1
        print(items, self.M - sum)
        if self.M - sum < self.min_diff[1] and self.M >= sum:
            self.min_diff = [items, self.M - sum]
        elif self.M < sum and self.skip_flag:
            self.skip = items[:-1]
        self.previous_diff = [self.previous_diff[1], self.M - sum]

    def get_slices(self):
        self.find_n()
        self.get_combinations()


if __name__ == '__main__':
    input_file = 'input/c_medium.in'
    # input_file = 'input/c_medium.in'

    pizza_slices = PizzaSlices(input_file)
    pizza_slices.get_slices()

    print('number of calls:', pizza_slices.counter)
    print(pizza_slices.min_diff)
