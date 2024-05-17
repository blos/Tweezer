from pathlib import Path

from Tweezer.GhidraBridge.ghidra_bridge import GhidraBridge


class Trainer:

    def __init__(self) -> None:
        pass

    @staticmethod
    def _generate_decompiled_functions_from_binaries(paths_to_binary_folders: list[str], decom_output: str):
        bridge = GhidraBridge()
        for path in paths_to_binary_folders:
            print("Decompiling: {}".format(path))
            bridge.decompile_all_binaries_in_folder(Path(path).resolve(), decom_output)


if __name__ == '__main__':
    raise Exception("This is not an entrypoint!")
