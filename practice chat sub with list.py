Известно, что в Python мы можем соединять два списка между собой с помощью оператора +:

lst = [1, 2, 3] + [4.5, -3.6, 0.78]
Но нет реализации оператора -, который бы убирал из списка соответствующие значения вычитаемого списка, как это показано в примере:

lst = [1, 2, 3, 4, 5, 6] - [5, 6, 7, 8, 1] # [2, 3, 4] (порядок следования оставшихся элементов списка должен сохраняться)
Давайте это поправим и создадим такой функционал. Для этого нужно объявить класс с именем NewList, объекты которого создаются командами:

lst = NewList() # пустой список
lst = NewList([-1, 0, 7.56, True]) # список с начальными значениями
Реализуйте для этого класса работу с оператором вычитания, чтобы над объектами класса NewList можно было выполнять следующие действия:

lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2 # NewList: [-4, 6, 10, 11, 15, False]
lst1 -= lst2 # NewList: [-4, 6, 10, 11, 15, False]
res_2 = lst2 - [0, True] # NewList: [1, 2, 3]
res_3 = [1, 2, 3, 4.5] - res_2 # NewList: [4.5]
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]
Также в классе NewList необходимо объявить метод:

get_list() - для возвращения результирующего списка объекта класса NewList

Например:

lst = res_2.get_list() # [1, 2, 3]


class NewList:
    def init(self, list_inp=None):
        if list_inp is None:
            list_inp = []
        self._list_inp = list_inp

    def sub(self, other):
        new_list = NewList(self._list_inp)
        data = NewList.get_lst_from(other)
        result = []

        # new_list._list_inp = {item1 for item1 in new_list._list_inp
        #                             for item2 in data
        #                       if item1 != item2}
        for item1 in new_list._list_inp:
            for item2 in data:
                if item1 != item2:
                    result.append(item1)

        return result

    def __isub(self, other):
        data = NewList.get_lst_from(other)
        self._list_inp = [item for item in self._list_inp if item not in data]
        return self

    @staticmethod
    def __get_lst_from(object_inp):
        if isinstance(object_inp, list):
            return object_inp
        elif isinstance(object_inp, NewList):
            return object_inp._list_inp
        else:
            raise TypeError("Must be list or obj NewList")

    def __str(self):
        return f"List is: {self._list_inp}"


lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2  # NewList: [-4, 6, 10, 11, 15, False]
lst1 -= lst2  # NewList: [-4, 6, 10, 11, 15, False]
print(res_1)
print(lst1)
print(lst2)
# res_2 = lst2 - [0, True]  # NewList: [1, 2, 3]
# res_3 = [1, 2, 3, 4.5] - res_2  # NewList: [4.5]
# a = NewList([2, 3])
# res_4 = [1, 2, 2, 3] - a  # NewList: [1, 2]