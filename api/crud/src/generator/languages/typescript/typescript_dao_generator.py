from api.crud.src.generator.SQL.SQL_generator_factory import SQLGeneratorFactory
from api.crud.src.generator.languages.dao_generator import DaoGenerator
from api.crud.src.parsing.components.table_model import TableModel
from api.crud.src.parsing.constants.allowed_dbms import AllowedDBMS


class TypeScriptDaoGenerator(DaoGenerator):
    """
    Generates the Data Access Object (DAO) implementation in TypeScript.
    """

    TEMPLATE = """
import {{ getConnection }} from './connection';
import {{ PoolClient }} from 'pg';

export class {ClassName}Dao {{
  static async insert({paramName}: any): Promise<void> {{
    const client: PoolClient = await getConnection();
    const query = `{InsertQuery}`;
    const values = [{InsertValues}];
    try {{
      await client.query(query, values);
    }} catch (error) {{
      console.error('Error inserting record:', error);
      throw error;
    }} finally {{
      client.release();
    }}
  }}

  static async selectById(id: number): Promise<any> {{
    const client: PoolClient = await getConnection();
    const query = `{SelectQuery}`;
    try {{
      const result = await client.query(query, [id]);
      return result.rows[0];
    }} catch (error) {{
      console.error('Error selecting record:', error);
      throw error;
    }} finally {{
      client.release();
    }}
  }}

  static async updateById(id: number, {paramName}: any): Promise<void> {{
    const client: PoolClient = await getConnection();
    const query = `{UpdateQuery}`;
    const values = [{UpdateValues}, id];
    try {{
      await client.query(query, values);
    }} catch (error) {{
      console.error('Error updating record:', error);
      throw error;
    }} finally {{
      client.release();
    }}
  }}

  static async deleteById(id: number): Promise<void> {{
    const client: PoolClient = await getConnection();
    const query = `{DeleteQuery}`;
    try {{
      await client.query(query, [id]);
    }} catch (error) {{
      console.error('Error deleting record:', error);
      throw error;
    }} finally {{
      client.release();
    }}
  }}
}}
    """

    @staticmethod
    def generate(dbms: AllowedDBMS, table_model: TableModel) -> str:
        """
        Generates the TypeScript code for DAO.
        """
        sql_generator = SQLGeneratorFactory.get(dbms, table_model)
        class_name = table_model.name.capitalize()
        param_name = table_model.name.lower()

        insert_query = sql_generator.generate_insert()
        insert_values = ", ".join(f"{field.name}" for field in table_model.fields if not field.autoIncrement)

        select_query = sql_generator.generate_select()

        update_query = sql_generator.generate_update()
        update_values = ", ".join(f"{field.name}" for field in table_model.fields if not field.primaryKey)

        delete_query = sql_generator.generate_delete()

        ts_code = TypeScriptDaoGenerator.TEMPLATE.format(
            ClassName=class_name,
            paramName=param_name,
            InsertQuery=insert_query,
            InsertValues=insert_values,
            SelectQuery=select_query,
            UpdateQuery=update_query,
            UpdateValues=update_values,
            DeleteQuery=delete_query,
        )

        return ts_code
