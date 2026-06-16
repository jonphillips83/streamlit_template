import math

class RsaEngine:

    "Engine for calculating the variables required to implement RSA"

    def __init__(self):
        self.prime_list = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        self.prime_factor_p = 3
        self.prime_factor_q = 11
        self.totient = 0
        self.public_exponent_candidates = []
        self.public_exponent = None
        self.private_exponent = None

        self.calculate_prime_totient()


    def update_prime_p(self, prime):
        
        self.prime_factor_p = prime
        self.calculate_prime_totient()


    def update_prime_q(self, prime):

        self.prime_factor_q = prime
        self.calculate_prime_totient()


    def update_public_key(self, key):

        if key not in self.public_exponent_candidates:
            raise ValueError(f"{key} is not a valid public exponent for totient {self.totient}.")
        self.public_exponent = key
        self.private_exponent = self.get_private_exponent()


    def calculate_prime_totient(self):

        totient = (self.prime_factor_p - 1) * (self.prime_factor_q - 1)
        self.totient = totient
        self.get_public_exponent_candidates()

        if self.public_exponent not in self.public_exponent_candidates:
            self.public_exponent = self.public_exponent_candidates[0]

        self.private_exponent = self.get_private_exponent()

        return totient
    
    @staticmethod
    def is_prime(n):
        if n < 2:
            return False
        # Cap range at SQRT + 1
        for i in range(2, int(math.isqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    
    def get_public_exponent_candidates(self):

        candidates = []
        # Loop through odd numbers starting at 3 (even numbers share a factor of 2)
        for i in range(3, self.totient, 2):
            # i must be coprime to totient
            if math.gcd(i, self.totient) == 1 and self.is_prime(i):
                candidates.append(i)

        self.public_exponent_candidates = candidates       
        return candidates
    

    def get_private_exponent(self):
        """
        Calculates the smallest valid positive private exponent (d) for RSA encryption
        """
        try:
            # pow(e, -1, totient) computes the Extended Euclidean Algorithm
            return pow(self.public_exponent, -1, self.totient)
            
        except ValueError:
            raise ValueError("The public exponent and totient are not coprime. No private key exists!")
    

    def encrypt_message(self):
        pass


    def decrypt_message(self):
        pass
    
    def __repr__(self):

        return (f"p: {self.prime_factor_p}, q: {self.prime_factor_q}, m: {self.totient}\n"
               f"candidates for e: {self.public_exponent_candidates}\n"
               f"e: {self.public_exponent}, d: {self.private_exponent}")
    

