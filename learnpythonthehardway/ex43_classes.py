class Scene(obeject):

	def enter(self):
		pass


class Engine(obeject):

	def __init__(self, scene_map):
		pass

	def play(self):
		pass


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

