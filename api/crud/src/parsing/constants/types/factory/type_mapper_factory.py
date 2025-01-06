from api.crud.src.parsing.constants.allowed_dbms import AllowedDBMS
from api.crud.src.parsing.constants.allowed_languages import AllowedLanguages
from api.crud.src.parsing.constants.types.language.csharp_type_mapper import CSharpTypeMapper
from api.crud.src.parsing.constants.types.language.java_type_mapper import JavaTypeMapper
from api.crud.src.parsing.constants.types.language.python_type_mapper import PythonTypeMapper
from api.crud.src.parsing.constants.types.language.typescript_type_mapper import TypeScriptTypeMapper
from api.crud.src.parsing.constants.types.sql.mysql_type_mapper import MySQLTypeMapper
from api.crud.src.parsing.constants.types.sql.oracle_type_mapper import OracleTypeMapper
from api.crud.src.parsing.constants.types.sql.postgresql_type_mapper import PostgreSQLTypeMapper
from api.crud.src.parsing.constants.types.sql.sqlite_type_mapper import SQLiteTypeMapper
from api.crud.src.parsing.constants.types.type_mapper import TypeMapper


class TypeMapperFactory:
    _dbms_mappers = {
        AllowedDBMS.mysql: MySQLTypeMapper,
        AllowedDBMS.postgresql: PostgreSQLTypeMapper,
        AllowedDBMS.sqlite: SQLiteTypeMapper,
        AllowedDBMS.oracle: OracleTypeMapper,
    }

    _language_mappers = {
        AllowedLanguages.java: JavaTypeMapper,
        AllowedLanguages.csharp: CSharpTypeMapper,
        AllowedLanguages.typescript: TypeScriptTypeMapper,
        AllowedLanguages.python: PythonTypeMapper,
    }

    @staticmethod
    def get_dbms_mapper(dbms: AllowedDBMS) -> TypeMapper:
        if dbms not in TypeMapperFactory._dbms_mappers:
            raise ValueError(f"TypeMapperFactory -> Unsupported DBMS: {dbms}")
        return TypeMapperFactory._dbms_mappers[dbms]()

    @staticmethod
    def get_language_mapper(language: AllowedLanguages) -> TypeMapper:
        if language not in TypeMapperFactory._language_mappers:
            raise ValueError(f"TypeMapperFactory -> Unsupported Language: {language}")
        return TypeMapperFactory._language_mappers[language]()
