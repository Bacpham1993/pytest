import factory
from polls.models import Person, Group

class GroupFactory(factory.Factory):
	FACTORY_FOR = Group
	name = 'Developers'
	
class PersonFactory(factory.Factory):
	FACTORY_FOR = Person
	first_name = 'John'
	last_name = 'Doe'
	group = factory.SubFactory(GroupFactory)