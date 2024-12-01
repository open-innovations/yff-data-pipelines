import os
import contextlib
from typing import Generator

@contextlib.contextmanager
def set_working_directory(path: str) -> Generator[None, None, None]:
    
    # Context manager to temporarily change the working directory.

    # Args:
    #    path (str): The path to change the working directory to.

    # Yields:
    #    None: This context manager does not return any value.
    
    original_directory = os.getcwd()
    # This could raise an exception, but it's probably
    # best to let it propagate and let the caller
    # deal with it, since they requested x
    try:
        os.chdir(path)
        yield
    except Exception as e:
        print(f"Error changing directory to {path}: {e}")
        raise
    finally:
        # This could also raise an exception, but you *really*
        # aren't equipped to figure out what went wrong if the
        # old working directory can't be restored.
        try:
            os.chdir(original_directory)
        except Exception as e:
            print(f"Error restoring original directory {original_directory}: {e}")
            raise