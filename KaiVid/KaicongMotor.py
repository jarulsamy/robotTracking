from base.KaicongOutput import KaicongOutput
import urllib2

class KaicongMotor(KaicongOutput):
<<<<<<< HEAD

=======
    
>>>>>>> de51deeff1b49a937f529426b83e43fed5e52816
    # These are the original state commands to send to the Kaicong camera.
    CMDLIST = {
        "PTZ_UP": 0,
        "PTZ_UP_STOP": 1,
        "PTZ_DOWN": 2,
        "PTZ_DOWN_STOP": 3,
        "PTZ_LEFT": 4,
        "PTZ_LEFT_STOP": 5,
        "PTZ_RIGHT": 6,
        "PTZ_RIGHT_STOP": 7,
        "PTZ_LEFT_UP": 90,
        "PTZ_RIGHT_UP": 91,
        "PTZ_LEFT_DOWN": 92,
        "PTZ_RIGHT_DOWN": 93,
        "PTZ_STOP": 1,
        "PTZ_CENTER": 25,
        "PTZ_VPATROL": 26,
        "PTZ_VPATROL_STOP": 27,
        "PTZ_HPATROL": 28,
        "PTZ_HPATROL_STOP": 29,
        "IO_ON": 94, # TODO: What does this do?
        "IO_OFF": 95, # and this one?
    }
<<<<<<< HEAD

    # This table converts a vector-style direction to its command
    MOVELIST = {
        "00": "PTZ_STOP",

        "0+": "PTZ_UP",
        "0-": "PTZ_DOWN",

        "+0": "PTZ_RIGHT",
        "-0": "PTZ_LEFT",

=======
    
    # This table converts a vector-style direction to its command
    MOVELIST = {
        "00": "PTZ_STOP",
        
        "0+": "PTZ_UP",
        "0-": "PTZ_DOWN",
        
        "+0": "PTZ_RIGHT",
        "-0": "PTZ_LEFT",
        
>>>>>>> de51deeff1b49a937f529426b83e43fed5e52816
        "++": "PTZ_RIGHT_UP",
        "+-": "PTZ_RIGHT_DOWN",
        "-+": "PTZ_LEFT_UP",
        "--": "PTZ_LEFT_DOWN",
    }
<<<<<<< HEAD

=======
    
>>>>>>> de51deeff1b49a937f529426b83e43fed5e52816
    URI = "http://{0}:81/decoder_control.cgi?loginuse={1}&loginpas={2}&command=%d&onestep=0"

    def __init__(self, domain, user="admin", pwd="123456"):
        KaicongOutput.__init__(
<<<<<<< HEAD
            self
            domain,
            KaicongMotor.URI,
            user,
            pwd
        )

        self.state = '00'

    @classmethod
    def to_symbol(self, v):
=======
            self, 
            domain, 
            KaicongMotor.URI, 
            user, 
            pwd
        )
        
        self.state = '00'
        
    def _to_symbol(self, v):
>>>>>>> de51deeff1b49a937f529426b83e43fed5e52816
        if v > 0:
            return '+'
        if v < 0:
            return '-'
        else:
            return '0'
<<<<<<< HEAD

    def send_command(self, cmdstr):
=======
    
    def send_command(self, cmdstr): 
>>>>>>> de51deeff1b49a937f529426b83e43fed5e52816
        stream = urllib2.urlopen(self.uri % (KaicongMotor.CMDLIST[cmdstr]))
        result = stream.read()
        assert "ok" in result
        stream.close()
<<<<<<< HEAD

    def move(self, xy):
        move_symbol = self.to_symbol(xy[0]) + self.to_symbol(xy[1])
=======
        
    def move(self, xy):
        move_symbol = self._to_symbol(xy[0]) + self._to_symbol(xy[1])
>>>>>>> de51deeff1b49a937f529426b83e43fed5e52816
        cmdstr = KaicongMotor.MOVELIST[move_symbol]
        if cmdstr != self.state:
            self.send_command(cmdstr)
        self.state = cmdstr
<<<<<<< HEAD




if __name__ == "__main__":
    import pygame
    import sys

    if len(sys.argv) != 2:
        print "Usage: %s <ip_address>" % sys.argv[0]
        sys.exit(-1)

    pygame.init()
    screen = pygame.display.set_mode((320, 240))

    motor = KaicongMotor(sys.argv[1])

=======
        
    
        
        
if __name__ == "__main__":
    import pygame
    import sys
    
    if len(sys.argv) != 2:
        print "Usage: %s <ip_address>" % sys.argv[0]
        sys.exit(-1)
    
    pygame.init()
    screen = pygame.display.set_mode((320, 240))
    
    motor = KaicongMotor(sys.argv[1])
    
>>>>>>> de51deeff1b49a937f529426b83e43fed5e52816
    def checkKeys():
        keys = pygame.key.get_pressed()
        x = 0
        y = 0
        if keys [pygame.K_a]:
            x = -1
        if keys [pygame.K_s]:
            y = -1
        if keys [pygame.K_d]:
            x = 1
        if keys [pygame.K_w]:
            y = 1
<<<<<<< HEAD

        motor.move([x, y])

=======
            
        motor.move([x, y])
            
>>>>>>> de51deeff1b49a937f529426b83e43fed5e52816
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 sys.exit()
        checkKeys()
<<<<<<< HEAD
=======
        
        
>>>>>>> de51deeff1b49a937f529426b83e43fed5e52816
