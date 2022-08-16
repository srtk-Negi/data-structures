from logging import exception


class Node:
        def __init__(self, data=None, nxt=None):
                self.data = data
                self.nxt = nxt

class LinkedList:
        def __init__(self):
                self.head = None
        
        def insert_start(self,data):
                node = Node(data,self.head)
                self.head = node

        def insert_end(self,data):
                node = Node(data, None)

                if self.head is None:
                        self.head = node
                        return

                itr = self.head
                while itr.nxt:
                        itr = itr.nxt
                itr.nxt = node

        def insert_list(self, data_list):
                self.head = None
                for data in data_list:
                        self.insert_end(data)

        def insert(self, pos, data):
                if pos < 0 or pos >= self.get_length():
                        raise Exception ("Invalid index")

                if pos == 0:
                        self.insert_start(data)
                        return

                if pos == self.get_length()-1:
                        self.insert_end(data)
                        return

                counter = 0
                itr = self.head
                while itr:
                        if counter == pos-1:
                                node = Node(data, itr.nxt)
                                itr.nxt = node
                                break
                        counter += 1
                        itr = itr.nxt            

        def remove(self,pos):
                if pos < 0 or pos >= self.get_length():
                        raise Exception ("Invalid index")
                if pos == 0:
                        self.head = self.head.nxt
                        return
                counter = 0
                itr = self.head
                while itr:
                        if counter == pos-1:
                                itr.nxt = itr.nxt.nxt
                                break
                        counter += 1
                        itr = itr.nxt

        def print(self):
                if self.head is None:
                        print("LinkedList is empty")
                        return
                
                ll_str = ""
                iterator = self.head

                while iterator:
                        ll_str += str(iterator.data) + " --> "
                        iterator = iterator.nxt

                print(ll_str)

        def get_length(self):
                counter = 0
                itr = self.head
                while itr:
                        counter += 1
                        itr = itr.nxt
                return(counter)

        def insert_after_value(self, data_after, data_to_insert):
                if self.head is None:
                        return
                
                itr = self.head

                for i in range(0, self.get_length()):
                        if itr.data == data_after:
                                node = Node(data_to_insert,itr.nxt)
                                itr.nxt = node
                                return
                        itr = itr.nxt
                raise Exception ("Given number does not exist in list")

        def remove_by_value(self, data):
                if self.head is None:
                        return

                counter = 0
                itr = self.head
                while itr:
                        if itr.data == data:
                                self.remove(counter)
                                break
                        counter += 1
                        itr = itr.nxt
                return


