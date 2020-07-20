class stack:
    def __init__(self):
        self.my_list=[]

    def get_stack(self):
        return self.my_list

    def pop(self):
        if(len(self.my_list)==0):
            return 0
        l=self.my_list[len(self.my_list)-1]
        self.my_list.remove(self.my_list[len(self.my_list)-1])
        return l

    def push(self,word):
       self.my_list.append(word)
       return self.my_list

    def is_empty(self):
        if(len(self.my_list)==0):
            return True
        return False

    def length(self):
        return len(self.my_list)
#s=stack()

#print('initial:'+str(s.get_stack()))

#word='-10'
#my_stack=s.push(word)
#print('after pushing \''+str(word)+'\' :'+str(my_stack))

#l,my_stack=s.pop()
#word=''
#print('after poping \''+str(l)+'\' :'+str(my_stack))

#print('after popping \''+str(l)+'\' :'+str(my_stack))
