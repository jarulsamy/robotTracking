

class KaicongOutput():
<<<<<<< HEAD

    def __init__(self, domain, uri_format, user="admin", pwd="123456"):
        """ domain:   Camera IP address or web domain
=======
    
    def __init__(self, domain, uri_format, user="admin", pwd="123456"):
        """ domain:   Camera IP address or web domain 
>>>>>>> de51deeff1b49a937f529426b83e43fed5e52816
                      (e.g. 385345.kaicong.info)
        """
        self.running = False
        self.uri = uri_format.format(domain, user, pwd)
<<<<<<< HEAD
=======
        
        
>>>>>>> de51deeff1b49a937f529426b83e43fed5e52816
