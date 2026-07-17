"""
rf_receiver.py

RF Hardware Receiver.

Responsibilities:
- Receive live RF data.
- Support RTL-SDR.
- Support GNU Radio.
- Support future SDR hardware.
"""

from typing import Dict, List


class RFReceiver:
    """
    Hardware RF Receiver.
    """

    SUPPORTED_DEVICES = {
        "RTL-SDR",
        "HackRF",
        "USRP"
    }

    def __init__(self) -> None:

        self.receiver_connected = False
        self.receiver_type = None

    def connect(
        self,
        receiver_type: str
    ) -> bool:
        """
        Connect RF receiver.
        """

        if (
            receiver_type
            not in self.SUPPORTED_DEVICES
        ):

            raise ValueError(
                f"Unsupported device: {receiver_type}"
            )

        # Future:
        #
        # RTL-SDR initialization.
        # GNU Radio setup.
        # Device validation.

        self.receiver_type = receiver_type
        self.receiver_connected = True

        return True

    def disconnect(
        self
    ) -> None:
        """
        Disconnect RF receiver.
        """

        self.receiver_connected = False
        self.receiver_type = None

    def get_signals(
        self
    ) -> List[Dict]:
        """
        Receive RF signals.

        Returns:
            List[Dict]
        """

        if not self.receiver_connected:

            raise RuntimeError(
                "RF receiver not connected."
            )

        # Future:
        #
        # return rtl_sdr.read_samples(...)
        #
        # return gnu_radio.process(...)
        #
        # return parsed_signals

        return []

    def get_status(
        self
    ) -> Dict:
        """
        Return receiver status.
        """

        return {
            "connected":
                self.receiver_connected,

            "receiver":
                self.receiver_type
        }


# Singleton Instance
rf_receiver = RFReceiver()


# Public APIs

def connect(
    receiver_type: str
) -> bool:

    return rf_receiver.connect(
        receiver_type
    )


def disconnect() -> None:

    rf_receiver.disconnect()


def get_signals():

    return rf_receiver.get_signals()


def get_status():

    return rf_receiver.get_status()