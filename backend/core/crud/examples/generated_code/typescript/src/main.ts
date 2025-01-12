import {ensureTableExists, UsersDao} from "./typescript_generated_code";


console.log("Hello, World!");


(async () => {
    await ensureTableExists();

    // Insert a new user
    const id = await UsersDao.insert('John Doe', 'john@example.com', 30);
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
