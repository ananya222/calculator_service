class calculator:
    def add(self,*argv):
        sum=0
        for arg in argv:
            for ag in arg:
                sum=sum+float(ag)
        return sum

    def subtract(self,*argv):
        i=argv[0]
        diff=float(i[0])+float(i[0])
        for arg in argv:
            for ag in arg:
                diff=diff-float(ag)
        return diff

    def multiply(self,*argv):
        product=1
        for arg in argv:
            for ag in arg:
                product=product*float(ag)
        return product

    def divide(self,*argv):
        i=argv[0]
        quotient=float(i[0])*float(i[0])
        for arg in argv:
            for ag in arg:
                quotient=float(quotient)/float(ag)
        return quotient
#c=calculator()
#n1=1
#n2=2
#print_string=c.add(n1,n2)
#print(print_string)
