import pygame
import random
import particle


class Explosion:
    def __init__(self, main, center, color):
        # initialize main settings
        self.settings = main.settings
        self.screen = main.screen
        self.screen_rect = self.screen.get_rect()
        self.t0 = pygame.time.get_ticks()/1000
        self.sound = main.explosion_sound

        # intialize particles
        self.center = center
        self.n_particles = random.randint(100, 500)
        self.color = color

        # particle Array
        self.particle_group = []
        self.create_particles()
        pygame.mixer.Sound.play(self.sound)

    def create_particles(self):
        while len(self.particle_group) < self.n_particles:
            n_particle = particle.Particle(self)
            self.particle_group.append(n_particle)

    def draw_explosion(self):
        for particle in self.particle_group:
            particle.draw_particle()

    def move_explosion(self):
        tf = pygame.time.get_ticks()/1000
        for particle in self.particle_group:
            particle.move_particle(tf)

    def delete_particles(self):
        for particle in self.particle_group:
            if particle.center[1] > self.settings.HEIGHT:
                self.particle_group.remove(particle)
