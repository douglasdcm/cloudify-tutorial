from cloudify.mocks import MockCloudifyContext
from testtools import TestCase
from demo.tasks import tasks
from demo.my_classes import Dog, DogOwner

class TestTasks(TestCase):

    def test_my_classes_set_properties(self):
        expected = "foo"
        dog = Dog()
        dog.name = expected
        mock_ctx = MockCloudifyContext(node_id="test_node_id", node_name="test_node_name",
                                       properties = {"dog_names": "fox"})
        observed = tasks.my_classes_set_property(mock_ctx, dog)
        self.assertEqual(expected, observed)

    def test_task_demo(self):
        expected = "bp_id"
        mock_ctx = MockCloudifyContext(blueprint_id=expected)
        observed = tasks.task_demo(mock_ctx)
        self.assertEqual(expected, observed)

    def test_my_classes_dog_name(self):
        dog = Dog()
        dog.name = "foo"
        dog_owner = DogOwner()
        dog_owner.name = "bla"
        self.assertEqual(dog.name, "foo")
        self.assertEqual(dog_owner.name, "bla")