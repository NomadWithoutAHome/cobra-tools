from generated.base_struct import BaseStruct
from generated.formats.base.basic import Ubyte
from generated.formats.base.basic import Uint
from generated.formats.base.basic import Ushort
from generated.formats.ms2.compounds.Matrix33 import Matrix33
from generated.formats.ms2.compounds.RotationRange import RotationRange


class IKEntry(BaseStruct):

	"""
	60 bytes
	"""

	__name__ = 'IKEntry'

	_import_key = 'ms2.compounds.IKEntry'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)

		# index into bone list
		self.child = 0

		# index into bone list
		self.parent = 0
		self.unk_0 = 0

		# no clue what space this is in, defines the orientation for the ranges
		self.matrix = Matrix33(self.context, 0, None)
		self.yaw = RotationRange(self.context, 0, None)
		self.pitch = RotationRange(self.context, 0, None)
		self.unk_1 = 1
		if set_default:
			self.set_defaults()

	_attribute_list = BaseStruct._attribute_list + [
		('child', Ubyte, (0, None), (False, None), None),
		('parent', Ubyte, (0, None), (False, None), None),
		('unk_0', Ushort, (0, None), (False, 0), None),
		('matrix', Matrix33, (0, None), (False, None), None),
		('yaw', RotationRange, (0, None), (False, None), None),
		('pitch', RotationRange, (0, None), (False, None), None),
		('unk_1', Uint, (0, None), (False, 1), None),
		]

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'child', Ubyte, (0, None), (False, None)
		yield 'parent', Ubyte, (0, None), (False, None)
		yield 'unk_0', Ushort, (0, None), (False, 0)
		yield 'matrix', Matrix33, (0, None), (False, None)
		yield 'yaw', RotationRange, (0, None), (False, None)
		yield 'pitch', RotationRange, (0, None), (False, None)
		yield 'unk_1', Uint, (0, None), (False, 1)