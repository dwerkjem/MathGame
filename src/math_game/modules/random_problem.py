class Random_problem:

    def number_of_zeros(self, number: int) -> int:
        length = len(str(number))
        return str(number).zfill(length).count("0")
