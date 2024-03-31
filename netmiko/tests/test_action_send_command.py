from st2tests.base import BaseActionTestCase
from netmiko_automation.send_command import main

import mock

__all__ = ["TestNetmikoAutomation"]


class TestNetmikoAutomation(BaseActionTestCase):
    action_cls = main

    @mock.patch("netmiko_automation.send_command.connect")
    def test_main(self, mock_connect):
        mock_connection = mock.MagicMock()
        mock_connection.send_command.return_value = "Output of the command"
        mock_connect.return_value = mock_connection

        action = self.get_action_instance()
        result = action.run(
            hostname="example.com", device_type="cisco_ios", port="22", command="show version")

        self.assertEqual(result, "Output of the command")
        mock_connect.assert_called_once_with(
            "example.com", "user", "password", device_type="cisco_ios", port="22")
        mock_connection.send_command.assert_called_once_with("show version")


if __name__ == '__main__':
    unittest.main()
