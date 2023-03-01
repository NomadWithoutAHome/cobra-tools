import numpy
from generated.array import Array
from generated.formats.base.basic import Float
from generated.formats.ms2.compounds.Constraint import Constraint


class PushConstraint(Constraint):

	"""
	used in JWE1 Pteranodon
	no longer used in PZ, JWE2
	might be some sort of avoidance
	"""

	__name__ = 'PushConstraint'

	_import_key = 'ms2.compounds.PushConstraint'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.floats = Array(self.context, 0, None, (0,), Float)
		if set_default:
			self.set_defaults()

	_attribute_list = Constraint._attribute_list + [
		('floats', Array, (0, None, (3,), Float), (False, None), None),
		]

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'floats', Array, (0, None, (3,), Float), (False, None)