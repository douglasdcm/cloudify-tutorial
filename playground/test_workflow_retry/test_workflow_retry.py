
from os import path
from cloudify.test_utils import workflow_test
import unittest


class TestWorkflowsRetry(unittest.TestCase):

    ROOT_DIR = path.dirname(path.abspath(__file__))

    @workflow_test(f"{ROOT_DIR}/test_blueprint.yaml")
    def test_workflow_retry(self, cfy_local):
        cfy_local.execute("generic_workflow", task_retries=3)

        instance = cfy_local.storage.get_node_instances()[0]
        assert instance["runtime_properties"].get("some_property") is not None
