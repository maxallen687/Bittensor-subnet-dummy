import argparse
import bittensor as bt


class ComputeArgPaser(argparse.ArgumentParser):
    def __init__(self, description=None, url="ws://127.0.0.1:9944", network="local", wallet_name="miner"):
        super().__init__(description=description)
        self.add_argument(
            "--netuid",
            type=int,
            default=1,
            help="The chain subnet uid.",
        )
        self.add_argument(
            "--subtensor.chain_endpoint",
            action="store_true",
            default=url,
        )
        self.add_argument(
            "--subtensor.network",
            action="store_true",
            default=network,
        )
        self.add_argument(
            "--wallet.name",
            action="store_true",
            default=wallet_name,
        )

        # Adds subtensor specific arguments i.e. --subtensor.chain_endpoint ... --subtensor.network ...
        bt.subtensor.add_args(self)
        # Adds logging specific arguments i.e. --logging.debug ..., --logging.trace .. or --logging.logging_dir ...
        bt.logging.add_args(self)
        # Adds wallet specific arguments i.e. --wallet.name ..., --wallet.hotkey ./. or --wallet.path ...
        bt.wallet.add_args(self)
        # Adds axon specific arguments i.e. --axon.port ...
        bt.axon.add_args(self)

        self.config = bt.config(self)

    @staticmethod
    def parse_list(arg):
        return arg.split(",")
