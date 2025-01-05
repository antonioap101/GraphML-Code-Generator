import {DropDownOption} from "../components/dropDown/DropDownComponent.tsx";
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome'
import {faDatabase} from "@fortawesome/free-solid-svg-icons";


export enum AllowedDBMS {
    MySQL = "MySQL",
    PostgreSQL = "PostgreSQL",
    SQLite = "SQLite",
    Oracle = "Oracle"
}

export const dbmsOptions: DropDownOption[] = Object.values(AllowedDBMS).map((dbms) => ({
    value: dbms,
    label: dbms.toLowerCase(),
    icon: <FontAwesomeIcon icon={faDatabase} />,
}));
