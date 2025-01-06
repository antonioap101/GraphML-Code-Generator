import {DropDownOption} from "../components/dropDown/DropDownComponent.tsx";
import MySQLIcon from "@/assets/icons/devicon_mysql.svg";
import PostgreSQLIcon from "@/assets/icons/devicon_postgresql.svg";
import SQLiteIcon from "@/assets/icons/devicon_sqlite.svg";
import OracleIcon from "@/assets/icons/devicon_oracle.svg";


export enum AllowedDBMS {
    MySQL = "MySQL",
    PostgreSQL = "PostgreSQL",
    SQLite = "SQLite",
    Oracle = "Oracle"
}

// Mapeo de íconos para DBMS
const dbmsIcons = {
    [AllowedDBMS.MySQL]: MySQLIcon,
    [AllowedDBMS.PostgreSQL]: PostgreSQLIcon,
    [AllowedDBMS.SQLite]: SQLiteIcon,
    [AllowedDBMS.Oracle]: OracleIcon,
};

export const dbmsOptions: DropDownOption[] = Object.values(AllowedDBMS).map((dbms) => ({
    value: dbms.toLowerCase(),
    label: dbms,
    icon: <img src={dbmsIcons[dbms]} alt={`${dbms} icon`} style={{width: 24, height: 24}}/>,
}));
