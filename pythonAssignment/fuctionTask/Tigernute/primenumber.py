def get_prime_number(number):
    if number < 2:
        for count in range(2, int(number ** 0.5) + 1):
            if number % count == 0:  
                return False
        return True