from math import pow

class FiniteQueue():
    def __init__(self, arrival_rate: int, service_rate: int) -> None:
        self._arrival_rate = arrival_rate
        self._service_rate = service_rate
        self._pho = self._arrival_rate/self._service_rate

    def get_prob_zero(self):
        return 1 - self._pho

    def get_prob_n(self, n: int):
        return pow(self._pho, n) * self.get_prob_zero()

    def get_system_length(self):
        return self._pho/(1 - self._pho)

    def get_queue_length(self):
        return self.get_system_length() - self._pho

    def get_system_wait_time(self):
        return self.get_system_length()/self.arrival_rate

    def get_queue_wait_time(self):
        return self.get_queue_length()/self.arrival_rate

    def get_prob_at_least(self, n: int):
        if n == 0: return self.get_prob_zero()

        return self.get_prob_n(n) + self.get_prob_at_least(n - 1)
    
    def get_prob_at_most(self, n: int):
        return 1 - self.get_prob_at_least(n)
    
if __name__ == '__main__':
    while True:
        print("Infinite Queue Simulation System (q to quit)")
        try:
            arrival_rate = int(input("Enter the system's arrival rate: "))
            service_rate = int(input("Enter the system's service rate: "))
        except ValueError:
            print("Exiting Simulation...")
            break
        q = FiniteQueue(arrival_rate, service_rate)
        while True:
            print("""what would you like to know about the system?
                0. Home
                1. System length
                2. Queue length
                3. System wait time
                4. Queue wait time
                5. Probability of zero people in the system
                6. Probability of N people in the system
                7. Probability of at least N people in the system
                8. Probability of at most N people in the system
                """)
            try:
                user_option = int(input("Enter choice (0 to quit): "))
            except ValueError:
                print('Option does not exist')
                break
            if user_option == 0:
                break
            if user_option == 1:
                val = q.get_system_length()
                print(f"The length of the system at any given time is {format(val, '.2f')}")
            if user_option == 2:
                val = q.get_queue_length()
                print(f"The length of the queue at any given time is {format(val, '.2f')}")
            if user_option == 3:
                val = q.get_system_length()
                print(f"The system wait time is {format(val, '.2f')}")
            if user_option == 4:
                val = q.get_queue_length()
                print(f"The queue wait time is {format(val, '.2f')}")
            if user_option == 5:
                val = q.get_prob_zero()
                print(f"The probability of zero people in the system is {format(val, '.2f')} or {format(val * 100, '.2f')}%")
            if user_option == 6:
                n = int(input("Enter 'N': "))
                val = q.get_prob_n(n)
                print(f"The probability of {n} people in the system is {format(val, '.2f')} or {format(val * 100, '.2f')}%")
            if user_option == 7:
                n = int(input("Enter 'N': "))
                val = q.get_prob_at_least(n)
                print(f"The probability of at least {n} people being in the system is {format(val, '.2f')} or {format(val * 100, '.2f')}%")
            if user_option == 8:
                n = int(input("Enter 'N': "))
                val = q.get_prob_at_most(n)
                print(f"The probability of at most {n} people being in the system is {format(val, '.2f')} or {format(val * 100, '.2f')}%")

            
