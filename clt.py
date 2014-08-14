from sage.all import *
from clt_params import *

print "CLT implementation using SAGE" 

current_time = lambda:time.time()

class MMP():
    def __init__(self, lam, k):

        self.x0 = ZZ(1)
        self.p = [0 for i in range(N)]
        
        print "generate p_i's and x0: "
       
        for i in range(N):
            p[i] = next_prime(ZZ.random_element(2^eta))
            
        x0 = prod(p[i] for i in range(N))

        
        
        print "generate crtCoeff_i's: "

        crtCoeff = [0 for i in range(N)]
        for i in range(N):
            crtCoeff[i] = x0/p[i]


        print "generate the g_i's: "

        print "generate z and zinv: "

        print "generate y: "

        print "generate zero tester v: "
        
        return 0

    def encrypt(self)
        return 0

    def sample(self)
        return 0
    
    def is_zero(self,c)
        return 0

if __name__=="__main__":

        mmap = MMP()

        print "generate encodings"
        encodings = [mmap.sample() for i in range(k)]


        result = 1

        print "multiply encodings"
        for c in encodings
            result *= c

        print "zero test"
        mmap.is_zero(result)

        c = current_time()


