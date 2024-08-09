import copy

def class_():
      data_structure = [
            [1, 2, 3],
            {'a': 4, 'b': 5},
            (6, {'cube': 7, 'drum': 8}),
            "Hello",
            ((), [{(2, 'Urban', ('Urban2', 35))}])
      ]
      list_ = []
      for i in (data_structure):
            if i == tuple or list or dict or set:
                  for i in data_structure:
                        if isinstance(i, int):
                              list_.append(i)
                              continue
                        elif isinstance(i, str):
                              list_.append(i)
                              continue
                        elif isinstance(i, list):
                              for k in i:
                                    list_.append(k)
                              continue
                        elif isinstance(i, dict):
                              for j, y in i.items():
                                    list_.append(j)
                                    list_.append(y)
                              continue
                        elif isinstance(i, tuple):
                              for x in i:
                                    list_.append(x)
                              continue
                        elif isinstance(i, set):
                              list_.append(*i)
                        else:
                              list_.append(i)
                  data_structure = copy.deepcopy(list_)
                  # print(data_structure)
                  list_.clear()


      return data_structure


list_of_value = class_()

def summ_of_item():
      summ_ = 0
      for i in (list_of_value):
            if isinstance(i, int):
                  summ_ += i
            else: summ_ += len(i)
      return summ_
summ_ = summ_of_item()
print(summ_)