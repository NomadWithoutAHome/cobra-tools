from generated.base_struct import BaseStruct
from generated.formats.base.basic import Float


class RotationRange(BaseStruct):

	"""
	tentative interpretation
	"""

	__name__ = 'RotationRange'

	_import_key = 'ms2.compounds.RotationRange'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.min = 0.0
		self.max = 0.0
		if set_default:
			self.set_defaults()

	_attribute_list = BaseStruct._attribute_list + [
		('min', Float, (0, None), (False, None), None),
		('max', Float, (0, None), (False, None), None),
		]

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'min', Float, (0, None), (False, None)
		yield 'max', Float, (0, None), (False, None)