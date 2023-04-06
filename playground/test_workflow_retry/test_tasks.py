from playground.test_workflow_retry.src.tasks import task_1
from cloudify.mocks import MockCloudifyContext
from pytest import raises


class TestTasksRetry:
    def test_task_1(self):
        arg = 0
        mock_ctx = MockCloudifyContext(
            node_id="any",
            properties={"some_property": "some_property"})
        assert task_1(mock_ctx, arg) is True

    def test_task_1_raises_exception(self):
        arg = 2
        mock_ctx = MockCloudifyContext()

        with raises(Exception):
            task_1(mock_ctx, arg)

    def test_task_1_operation_retry(self):
        arg = 1
        mock_ctx = MockCloudifyContext(
            node_id="any",
            properties={"some_property": "some_property"})
        task_1(mock_ctx, arg) is None
        assert mock_ctx.instance.runtime_properties.get(
            "some_property") == "retry"
