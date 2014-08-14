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
            self.p[i] = next_prime(ZZ.random_element(2**eta))
            
        self.x0 = prod(self.p[i] for i in range(N))

        
        
        print "generate crtCoeff_i's: "

        self.crtCoeff = [0 for i in range(N)]
        for i in range(N):
            self.crtCoeff[i] = self.x0/self.p[i]


        print "generate the g_i's: "
        self.g = [0 for i i range(N)]
        for i in range(N):
            self.g[i] = next_prime(ZZ.random_element(2**alpha))

        print "generate z and zinv: "
        while True:
            self.z = ZZ.random_element(self.x0)  
            try
                self.zinv = inverse_mod(z,self.x0)
                break
            except ZeroDivisionError
            

        print "generate y: "
        self.y = self.encrypt_with_sk(1,rho,1)


        print "generate zero tester v: "
        zkappa = 1
        for i in range(kappa):
            zkappa = mod(zkappa*self.z,self.x0)
        
        return 0

    def encrypt(self,m,nSize,level)

    
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


