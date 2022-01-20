from cloudify.mocks import MockCloudifyContext
from testtools import TestCase
from my_blueprint.plugins.my_plugin_folder import tasks


class TestTasks(TestCase):

    def test_task_with_param(self):
        expected = "foo"
        mock_ctx = MockCloudifyContext(node_name="test_node_name",
                                       node_id="test_node_id")
        observed = tasks.taks_with_params(mock_ctx, expected)
        self.assertEqual(expected, observed)

    def test_get_deployment_id(self):
        expected = "dep_id"
        mock_ctx = MockCloudifyContext(deployment_id=expected)
        actual = tasks.get_deployment_id(mock_ctx)
        self.assertEqual(expected, actual)

    def test_get_blueprint_id(self):
        expected = "blueprint_id"
        mock_ctx = MockCloudifyContext(blueprint_id=expected)
        actual = tasks.get_blueprint_id(mock_ctx)
        self.assertEqual(expected, actual)

    def test_task_demo(self):
       expected = "some property test"
       props = {"some_property": expected}
       mock_ctx = MockCloudifyContext(node_id="test_node_id",
                                    node_name="test_node_name",
                                    properties=props)

       actual = tasks.task_demo(mock_ctx)
       self.assertEqual(expected, actual)

    def test_get_runtime_property(self):
        expected = "my expectation"
        mock_ctx = MockCloudifyContext(node_id="test_node_id",
                                       node_name="test_node_name")
        actual = tasks.get_runtime_properties(mock_ctx, expected)
        self.assertEqual(expected, actual)
