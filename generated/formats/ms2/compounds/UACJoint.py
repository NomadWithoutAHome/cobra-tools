from generated.array import Array
from generated.base_struct import BaseStruct
from generated.formats.ms2.imports import name_type_map


class UACJoint(BaseStruct):

	"""
	36 bytes
	"""

	__name__ = 'UACJoint'


	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)

		# variable
		self.unk = Array(self.context, 0, None, (0,), name_type_map['Ushort'])

		# some at least
		self.floats = Array(self.context, 0, None, (0,), name_type_map['Float'])
		if set_default:
			self.set_defaults()

	@classmethod
	def _get_attribute_list(cls):
		yield from super()._get_attribute_list()
		yield 'unk', Array, (0, None, (6,), name_type_map['Ushort']), (False, None), (None, None)
		yield 'floats', Array, (0, None, (6,), name_type_map['Float']), (False, None), (None, None)

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'unk', Array, (0, None, (6,), name_type_map['Ushort']), (False, None)
		yield 'floats', Array, (0, None, (6,), name_type_map['Float']), (False, None)
