"""
Utility functions to handle message passing between ui and search.
"""

import platform

os = platform.system()
# TODO: Investigate how platform independence is achieved in native python apps between OSX and Linux
if os == "Darwin":
    # Import a Darwin specific msg bus here.
    # TODO: Investigate use of PyObjC for message passing.
    #
    class DarwinBus():
        def __init__(self):
            """Mac os X specific message bus initiator."""
            pass

        def __del__(self):
            """Unregister the DarwinBus from system."""
            pass

    SuperBus = DarwinBus

elif os == "Linux":
    import dbus

    class LinuxBus():
        def __init__(self):
            """Linux specific message bus."""
            session_bus = dbus.SessionBus()

        def __del__(self):
            """Unregister the LinuxBus from system."""
            pass

    SuperBus = LinuxBus

if os == "Java" or os == "Windows":
    raise NotImplementedError("Sorry this software is not supported on this platform yet")


class MessageBus(SuperBus):
    """Generic message bus class for application layer."""

    def __init__(self):
        """Register the message bus"""
        super(MessageBus, self).__init__()
        pass

    def send(self, msg):
        """Send an msg."""
        pass

    def recv(self):
        """Return a received message."""
        pass
