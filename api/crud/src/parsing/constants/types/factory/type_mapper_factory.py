from api.crud.src.parsing.constants.allowed_dbms import AllowedDBMS
from api.crud.src.parsing.constants.allowed_languages import AllowedLanguages
from api.crud.src.parsing.constants.types.language.java_type_mapper import JavaTypeMapper
from api.crud.src.parsing.constants.types.sql.mysql_type_mapper import MySQLTypeMapper
from api.crud.src.parsing.constants.types.sql.postgresql_type_mapper import PostgreSQLTypeMapper
from api.crud.src.parsing.constants.types.type_mapper import TypeMapper


class TypeMapperFactory:
    _dbms_mappers = {
        AllowedDBMS.mysql: MySQLTypeMapper,
        AllowedDBMS.postgresql: PostgreSQLTypeMapper,
    }

    _language_mappers = {
        AllowedLanguages.java: JavaTypeMapper,
    }

    @staticmethod
    def get_dbms_mapper(dbms: AllowedDBMS) -> TypeMapper:
        if dbms not in TypeMapperFactory._dbms_mappers:
            raise ValueError(f"Unsupported DBMS: {dbms}")
        return TypeMapperFactory._dbms_mappers[dbms]()

    @staticmethod
    def get_language_mapper(language: AllowedLanguages) -> TypeMapper:
        if language not in TypeMapperFactory._language_mappers:
            raise ValueError(f"Unsupported Language: {language}")
        return TypeMapperFactory._language_mappers[language]()
