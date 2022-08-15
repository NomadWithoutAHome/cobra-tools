from generated.formats.base.basic import Float
from generated.formats.habitatboundary.structs.HbPhysicsOffsets import HbPhysicsOffsets
from generated.formats.ovl_base.compounds.MemStruct import MemStruct


class HbOffsets(MemStruct):

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.physics = HbPhysicsOffsets(self.context, 0, None)

		# Vertical offset of visible post above wall. Post height = wall_height + post_height_offset.
		self.post_height_offset = 0.0

		# The starting height of the barrier wall.
		self.wall_height = 0.0
		if set_default:
			self.set_defaults()

	def set_defaults(self):
		super().set_defaults()
		self.physics = HbPhysicsOffsets(self.context, 0, None)
		self.post_height_offset = 0.0
		self.wall_height = 0.0

	@classmethod
	def read_fields(cls, stream, instance):
		super().read_fields(stream, instance)
		instance.physics = HbPhysicsOffsets.from_stream(stream, instance.context, 0, None)
		instance.post_height_offset = Float.from_stream(stream, instance.context, 0, None)
		instance.wall_height = Float.from_stream(stream, instance.context, 0, None)

	@classmethod
	def write_fields(cls, stream, instance):
		super().write_fields(stream, instance)
		HbPhysicsOffsets.to_stream(stream, instance.physics)
		Float.to_stream(stream, instance.post_height_offset)
		Float.to_stream(stream, instance.wall_height)

	@classmethod
	def _get_filtered_attribute_list(cls, instance):
		yield from super()._get_filtered_attribute_list(instance)
		yield 'physics', HbPhysicsOffsets, (0, None)
		yield 'post_height_offset', Float, (0, None)
		yield 'wall_height', Float, (0, None)

	def get_info_str(self, indent=0):
		return f'HbOffsets [Size: {self.io_size}, Address: {self.io_start}] {self.name}'

	def get_fields_str(self, indent=0):
		s = ''
		s += super().get_fields_str()
		s += f'\n	* physics = {self.fmt_member(self.physics, indent+1)}'
		s += f'\n	* post_height_offset = {self.fmt_member(self.post_height_offset, indent+1)}'
		s += f'\n	* wall_height = {self.fmt_member(self.wall_height, indent+1)}'
		return s

	def __repr__(self, indent=0):
		s = self.get_info_str(indent)
		s += self.get_fields_str(indent)
		s += '\n'
		return s