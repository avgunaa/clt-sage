from sage.all import *
from clt_params import *

print "CLT multilinear map implementation using SAGE" 

current_time = lambda:time.time()

class Ciphertext():
    def __init__(self,val,degree)
        self.val = val
        self.degree = degree
    

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
            Q = self.x0/self.p[i]
            self.crtCoeff[i] = inverse_mod(Q,self.p[i])
            self.crtCoeff[i] = self.crtCoeff[i]*Q

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
        self.y = self.encrypt(1,rho,1)


        print "generate zero tester p_zt: "
        zkappa = 1
        self.p_zt = 0
        for i in range(kappa):
            zkappa = mod(zkappa*self.z,self.x0)
        for i in range(N):
            t_res = inverse_mod(g[i],p[i])
            t_res = mod(t_res*z_kappa,p[i])*ZZ.random_element(2**hbits)*(x0/p[i])
            self.p_zt = self.p_zt + t_res
        self.p_zt = mod(sefl.p_zt,x0)
        return 0

    def encrypt(self,m,nSize,level)
        res = 0
        for i in range(N)
            res = res + (m + self.g[i]*ZZ.random_element(2**nSize))*self.crtCoeff[i]
        res = mod(res,x0)
        for j in range(level)
            res = mod(res*zinv,x0)
        return res

    def sample(self,k)
        #m = [0 for i in range(N)]
        #for i in range(N):
        #    m[i] = ZZ.random_element(2**alpha)
        m = ZZ.random_element(2**alpha)
        c = self.encrypt(m,rho,k)
        return mod(c,self.x0)
    
    def is_zero(self,c)
        w = self.zero_test(c.val,c.degree)
        

    def zero_test(self,val,deg)

        for i in range(
        

if __name__=="__main__":

        k = 5
        m = 10
        mmap = MMP()
        print "generate encodings"
        encodings = [mmap.sample(k) for i in range(m)]

        print "multiply encodings"
        result = 1
        for c in encodings
            result *= c

        print "zero test"
        mmap.is_zero(result)

        c = current_time()


