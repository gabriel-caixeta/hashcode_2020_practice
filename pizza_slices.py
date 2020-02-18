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
        self.reverse_flag = False
        self.min_diff=[[], self.M]
        self.skip = []
        self.skip_flag = True
        self.counter = 0
        self.n = -1
        self.previous_diff = self.M

    def reverse_S(self):
        self.S.reverse()

    def find_n(self,):
        for i in range(1,len(self.S)):
            # print(i,sum(self.S[len(self.S)-i:]),self.M)
            if sum(self.S[len(self.S)-i:])<self.M:
                continue
            else:
                self.n = i
                break

        if self.M - sum(self.S[:self.n]) > sum(self.S[len(self.S)-self.n:]) - self.M:
            print('Reversing string')
            self.S.reverse()
            self.reverse_flag = True
            self.skip_flag = False

    def get_combinations(self):
        self.skip = []
        for i in combinations(self.S, self.n):
            if self.skip_flag:
                if i[:-1]== self.skip:
                    continue
            else:
                if i[:-1]==self.skip:
                    continue

            self.get_min(i,sum(i))
            # print(i,self.skip_flag,self.min_diff)
            if self.min_diff[1]==0:
                return
        return

    def get_min(self,items,sum):
        self.counter += 1
        # print(items, self.M - sum)
        current_diff = self.M - sum
        if current_diff < self.min_diff[1] and self.M >= sum:
            if self.previous_diff < 0 and current_diff > 0:
                self.skip = items[:-1]
                # continue
            else:
                self.min_diff = [items, current_diff]
                self.previous_diff=self.M - sum

        elif self.M < sum and self.skip_flag:
            self.skip = items[:-1]
        self.previous_diff = current_diff

    def get_slices(self):
        self.find_n()
        self.get_combinations()


def get_indexes(all_list,elements):
    last_index = -1
    index_list = []
    tmp_list = list(elements)
    # print()
    # for element in elements:
    #     for i in range(last_index+1,len(all_list)):
    #         if element == all_list[i]:
    #             index_list.append(i)
    #             last_index = i
    #             break
    for index, element in enumerate(all_list):
        if element in tmp_list:
            index_list.append(index)
            tmp_list.remove(element)
    return index_list


if __name__ == '__main__':
    inputs = ['a_example.in','b_small.in','c_medium.in','d_quite_big.in','e_also_big.in']
    # inputs = ['a_example.in']
    for input_filename in inputs:
        print(input_filename)
        input_file = 'input/'+ input_filename
        # input_file = 'input/c_medium.in'

        pizza_slices = PizzaSlices(input_file)
        pizza_slices.get_slices()

        # print()
        print('number of calls:', pizza_slices.counter)
        print(pizza_slices.min_diff[1],sum(pizza_slices.min_diff[0])-pizza_slices.M)

        output = ""
        if pizza_slices.reverse_flag:
            pizza_slices.reverse_S()
        for ind in get_indexes(pizza_slices.S,pizza_slices.min_diff[0]):
            output += str(ind)+' '
        # for pizza in pizza_slices.min_diff[0]:
        #     output+=str(pizza_slices.S.index(pizza))+' '

        output_file = input_filename.replace('.in','') + '_output_2.txt'
        with open(output_file,'w',encoding='utf8') as f_out:
            f_out.write(str(len(pizza_slices.min_diff[0]))+'\n')
            f_out.write(output)
