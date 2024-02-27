from collections.abc import Generator

import pytest
from pyflink.datastream import StreamExecutionEnvironment


@pytest.fixture(scope='session')
def environment() -> Generator[StreamExecutionEnvironment]:
    """Create a stream execution environment and close it after tests are completed."""
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(1)

    yield env

    env.close()
