#encoding:utf-8
from sys import exit
from random import randint

class Scene(obeject):	#制造场景

	def enter(self):
		print "这个场景只是基类，包含所有场景的通用信息，并不会显示哦"
		exit(1)


class Engine(obeject):

	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()

		while True:
			print "\n--------------"
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)


class Death(Scene):

	def enter(self):
		pass


class CentralCorridor(Scene):

	def enter(self):
		pass


class LaserWeaponArmory(Scene):

	def enter(self):
		pass


class TheBrdge(Scene):

	def enter(self):
		pass


class EscapePod(Scene):

	def enter(self):
		pass


class Map(obeject):

	def __inti__(self, start_scene):
		pass

	def next_scene(self, scene_name):
		pass

	def opening_scene(self):
		pass


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

