from prophecy.config import ConfigBase


class SubgraphConfig(ConfigBase):

    def __init__(
            self,
            prophecy_spark=None,
            source_catalog: str="",
            source_schema: str="",
            source_table: str="",
            column: str="",
            logic: str="",
            **kwargs
    ):
        self.source_catalog = source_catalog
        self.source_schema = source_schema
        self.source_table = source_table
        self.column = column
        self.logic = logic
        pass

    def update(self, updated_config):
        self.source_catalog = updated_config.source_catalog
        self.source_schema = updated_config.source_schema
        self.source_table = updated_config.source_table
        self.column = updated_config.column
        self.logic = updated_config.logic
        pass

Config = SubgraphConfig()
