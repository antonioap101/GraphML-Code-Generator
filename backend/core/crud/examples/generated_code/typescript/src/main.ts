import {ensureTableExists as pgEnsureTableExists, UsersDao as pgUsersDao} from "./typescript_postgres_generated_code";
import {ensureTableExists as sqliteEnsureTableExists, UsersDao as sqliteUsersDao} from "./typescript_sqlite_generated_code";
import {
    ensureTableExists as mysqlEnsureTableExists,
    UsersDao as mysqlUsersDao
} from "./typescript_mysql_generated_code";


console.log("Hello, World!");
const all = [
    mysqlEnsureTableExists,
    mysqlUsersDao,
    pgEnsureTableExists,
    pgUsersDao,
    sqliteEnsureTableExists,
    sqliteUsersDao
]

const ensureTableExists = mysqlEnsureTableExists;
const UsersDao = mysqlUsersDao;

// const ensureTableExists = sqliteEnsureTableExists;
// const UsersDao = sqliteUsersDao;

//const ensureTableExists = sqliteEnsureTableExists;
// const UsersDao = sqliteUsersDao;




(async () => {
    await ensureTableExists();

    // Insert a new user
    const result = await UsersDao.insert('John Doe', 'john@example.com', 30);
    console.log('Inserted user:', result);
    const id = 1;
    console.log('Inserted user with ID:', id);
    // Read the user by ID
    const user = await UsersDao.selectById(Number(id));
    console.log('User:', user);

    // Update the user
    await UsersDao.updateById(id, 'Jane Doe', 'jane@example.com', 25);
    console.log('Updated user with ID:', id);

    // Delete the user
    await UsersDao.deleteById(id);
    console.log('Deleted user with ID:', id);
})();
