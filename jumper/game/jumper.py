class Jumper:

    """The jumper is trying to guess the hidden word. 
    
    The responsibility of a Jumper is to watch guess letters and make sure they don't lose their entire parachute
    
    Attributes:
        parachute(list): 
    """
    def __init__(self):
        """Constructs a new Jumper.

        Args:
            self (jumper): An instance of Jumper.
        """
        self.parachute = []
        self.build_parachute()
        self._parachute_level = 0

    def build_parachute(self):
        """builds a new parachute.
        
        Args:
            self (jumper): An instance of Jumper
        """
        self.parachute.append('  ___ ')
        self.parachute.append(' /   \\')
        self.parachute.append('  --- ')
        self.parachute.append(' \\   /')
        self.parachute.append('  \\ / ')
        self.parachute.append('   o  ')
        self.parachute.append('  /|\\')
        self.parachute.append('  / \\ ')
        self.parachute.append('')
        self.parachute.append('^^^^^^^')
                
    def show_jumper(self):
        """returns the current parachute.
        
        Args:
            self (jumper): An instance of Jumper
        """
        return self.parachute


    def remove_next_parachute_part(self):
        """Deletes a level of the parachute

        Args:
            self (Jumper): An instance of Jumper.
        """
        self.parachute.pop(0)
        self._parachute_level += 1
        if self._parachute_level == 5:
            self.parachute[0] = '  x  '

