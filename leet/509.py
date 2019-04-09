def fib(self, N):
        return (self.fib(N - 1) + self.fib(N - 2)) if N > 1 else N
        
