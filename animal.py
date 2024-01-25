
class dog:

    arm_length = 0.0
    leg_length = 0.0
    num_eyes = 0
    have_tail = True
    is_furry = True

    def __init__(self, arm_length, leg_length, num_eyes, have_tail, is_furry):
        self.arm_length = arm_length
        self.leg_length = leg_length
        self.num_eyes = num_eyes
        self.have_tail = have_tail
        self.is_furry = is_furry

    # Sample Method
    def print_characters(self):
        print('Dog has arm length = ' + str(self.arm_length) + "\n");
        print('Dog has leg length = ' + str(self.leg_length) + "\n");
        print('Dog has num eyes = ' + str(self.num_eyes) + "\n");
        print('Dog has have tail = ' + str(self.have_tail) + "\n");
        print('Dog has have fur = ' + str(self.is_furry) + "\n");




if __name__ == "__main__":

    A = dog(4.5,2.4,2,True,True)

    A.print_characters()