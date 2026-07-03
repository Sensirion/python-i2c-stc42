import struct
import sensirion_driver_adapters.mocks.response_provider as rp


class Stc42ResponseProvider(rp.ResponseProvider):

    RESPONSE_MAP = {0x365b: struct.pack('>4B8s', *rp.random_bytes(4), rp.random_ascii_string(8))}

    def get_id(self) -> str:
        return 'Stc42ResponseProvider'

    def handle_command(self, cmd_id: int, data: bytes, response_length: int) -> bytes:
        return self.RESPONSE_MAP.get(cmd_id, rp.random_bytes(response_length))
