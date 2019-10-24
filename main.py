import numpy as np

class body:
    def __init__(self, pos, vel, mass, charge):
        self.pos = pos
        self.vel = vel
        self.mass = mass
        self.charge = charge
    
    def __eq__(self, bod):
        return np.all(self.pos == bod.pos)
    
    def __ne__(self, bod):
        return np.any(self.pos != bod.pos)

    def __str__(self):
        return f"pos: {self.pos}, vel: {self.vel}, mass: {self.mass}"

    @staticmethod
    def move(bod, dt, a):
        return bod

    @property
    def speed(self):
        return np.linalg.norm(self.vel)

class world:
    def __init__(self, G=6.67e-11, K=8.99e9, cap=128):
        self.G = G
        self.K = K
        self.bodies = np.empty(cap, dtype=body)
    
    def addBody(self, pos, vel, mass, charge):
        try:
            self.bodies[len(self.bodies) - len(self.bodies[self.bodies == None])] = body(pos, vel, mass, charge)
        except IndexError:
            raise Exception("World capacity exceeded!")

    def __mlt__(self, dt):
        a = 0
        self.bodies = body.move(self.bodies, dt, a)
        return self
