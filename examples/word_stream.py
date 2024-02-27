from pyflink.common import Types
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import (
    DataTypes,
    Schema,
    StreamTableEnvironment,
    TableDescriptor,
)
from pyflink.table.expressions import col


if __name__ == "__main__":

    words = [
        "flink",
        "window",
        "timer",
        "event_time",
        "processing_time",
        "state",
        "connector",
        "pyflink",
        "checkpoint",
        "watermark",
        "sideoutput",
        "sql",
        "datastream",
        "broadcast",
        "asyncio",
        "catalog",
        "batch",
        "streaming",
    ]

    max_word_id = len(words) - 1

    def id_to_word(id: int) -> str:
        return words[id]

    env = StreamExecutionEnvironment.get_execution_environment()
    t_env = StreamTableEnvironment.create(stream_execution_environment=env)

    datagen = (
        TableDescriptor.for_connector("datagen")
        .schema(
            Schema.new_builder().column("id", DataTypes.INT(nullable=False)).build()
        )
        .option("fields.id.kind", "random")
        .option("fields.id.min", "0")
        .option("fields.id.max", str(max_word_id))
        .option("rows-per-second", "5")
        .build()
    )

    t_env.create_temporary_table("source", datagen)

    source = t_env.from_path("source").select(col("id"))
    input_stream = t_env.to_data_stream(source)

    word_stream = input_stream.map(lambda row: id_to_word(row[0]), Types.STRING())

    word_stream.print()

    env.execute()
