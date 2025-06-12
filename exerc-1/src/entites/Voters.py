import math


class Voters():

    def __init__(self, total_voters:int,valid_voters:int,white_votes:int, null_votes:int):
        self.total_voters = total_voters
        self.valid_voters = valid_voters
        self.white_votes = white_votes
        self.null_votes = null_votes

    def percent_valid_votes(self):
        return (self.valid_voters / self.total_voters  ) * 100
    
    def percent_white_votes(self):
        return (self.white_votes / self.total_voters) * 100
    
    def percent_null_votes(self):
        return (self.null_votes / self.total_voters ) * 100
    

def main():
    voters = Voters(total_voters=1000,valid_voters=800,white_votes=150,null_votes=50)
    print(voters.percent_valid_votes())
    print(voters.percent_white_votes())
    print(voters.percent_null_votes())

main()