from api.crud.src.generator.SQL.SQL_generator_factory import SQLGeneratorFactory
from api.crud.src.generator.languages.dao_generator import DaoGenerator
from api.crud.src.parsing.components.table_model import TableModel
from api.crud.src.parsing.constants.allowed_dbms import AllowedDBMS
from api.crud.src.parsing.constants.allowed_languages import AllowedLanguages
from api.crud.src.parsing.constants.types.factory.type_mapper_factory import TypeMapperFactory


class JavaDaoGenerator(DaoGenerator):
    """
    Generador de clases DAO en Java basadas en los metadatos de la tabla y las consultas SQL generadas.
    """

    # Plantilla base para las clases DAO en Java
    TEMPLATE = """
import java.sql.*;

public class {ClassName}DAO {{
    private Connection connection;
    public {ClassName}DAO(Connection connection) {{
        this.connection = connection;
    }}
    
    // Create
    public void create({FieldParameters}) throws SQLException {{
        String sql = "{InsertQuery}";
        try (PreparedStatement statement = connection.prepareStatement(sql)) {{
            {SetInsertParameters}
            statement.executeUpdate();
        }}
    }}
    
    // Read
    public ResultSet read(int id) throws SQLException {{
        String sql = "{SelectQuery}";
        PreparedStatement statement = connection.prepareStatement(sql);
        statement.setInt(1, id);
        return statement.executeQuery();
    }}
    
    // Update
    public void update(int id, {FieldParameters}) throws SQLException {{
        String sql = "{UpdateQuery}";
        try (PreparedStatement statement = connection.prepareStatement(sql)) {{
            {SetUpdateParameters}
            statement.setInt({ParamIndex}, id);
            statement.executeUpdate();
        }}
    }}
                                
    // Delete
    public void delete(int id) throws SQLException {{
        String sql = "{DeleteQuery}";
        try (PreparedStatement statement = connection.prepareStatement(sql)) {{
            statement.setInt(1, id);
            statement.executeUpdate();
        }}
    }}
}}
    """

    @staticmethod
    def generate(dbms: AllowedDBMS, table: TableModel) -> str:
        """
        Genera el código de una clase DAO en Java basada en los metadatos de la tabla y el DBMS.
        """
        # Obtener el generador SQL correspondiente al DBMS
        sql_generator = SQLGeneratorFactory.get(dbms, table)

        # Generar consultas SQL
        insert_query = sql_generator.generate_insert()
        select_query = sql_generator.generate_select()
        update_query = sql_generator.generate_update()
        delete_query = sql_generator.generate_delete()

        sql_mapper = TypeMapperFactory.get_dbms_mapper(dbms)
        java_mapper = TypeMapperFactory.get_language_mapper(AllowedLanguages.java)
        # Generar parámetros y configuración de PreparedStatement
        field_parameters = ", ".join(
            f"{java_mapper.get_mapping(field.type)} {field.name}"
            for field in table.fields if not field.autoIncrement
        )
        set_insert_parameters = "\n                ".join(
            f"statement.set{java_mapper.get_mapping(field.type)}({index}, {field.name});"
            for index, field in enumerate(table.fields, start=1) if not field.autoIncrement
        )
        set_update_parameters = "\n                ".join(
            f"statement.set{java_mapper.get_mapping(field.type)}({index}, {field.name});"
            for index, field in enumerate(table.fields, start=1) if not field.primaryKey
        )

        # Rellenar la plantilla con los valores generados
        java_code = JavaDaoGenerator.TEMPLATE.format(
            ClassName=table.name.capitalize(),
            FieldParameters=field_parameters,
            InsertQuery=insert_query,
            SelectQuery=select_query,
            UpdateQuery=update_query,
            DeleteQuery=delete_query,
            SetInsertParameters=set_insert_parameters,
            SetUpdateParameters=set_update_parameters,
            ParamIndex=len(table.fields) + 1  # Índice del ID en la consulta UPDATE
        )

        return java_code
