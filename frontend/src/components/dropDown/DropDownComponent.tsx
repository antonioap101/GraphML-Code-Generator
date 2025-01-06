import React, {useEffect, useRef, useState} from "react";
import "./DropDownComponent.css";


export interface DropDownOption {
    value: string; // Identificador único
    label: string; // Texto a mostrar
    icon: React.ReactNode; // Icono asociado
}

interface DropdownProps {
    selectedOption?: DropDownOption;
    options: DropDownOption[];
    onSelect: (option: DropDownOption) => void;
    placeholder?: string;
}

const DropdownComponent: React.FC<DropdownProps> = ({
                                                        selectedOption,
                                                        options,
                                                        onSelect,
                                                        placeholder = "Select an option",
                                                    }) => {
    const [isOpen, setIsOpen] = useState(false);
    const dropdownRef = useRef<HTMLDivElement>(null);

    useEffect(() => {
        const handleClickOutside = (event: MouseEvent) => {
            if (dropdownRef.current && !dropdownRef.current.contains(event.target as Node)) {
                setIsOpen(false);
            }
        };

        document.addEventListener("mousedown", handleClickOutside);
        return () => {
            document.removeEventListener("mousedown", handleClickOutside);
        };
    }, []);

    const handleSelect = (option: DropDownOption) => {
        setIsOpen(false);
        onSelect(option);
    };

    return (
        <div ref={dropdownRef} className="dropdown-container">
            <div className="dropdown-header" onClick={() => setIsOpen(!isOpen)}>
                <span
                    className="dropdown-selected"
                    style={{
                        display: "flex",
                        alignItems: "center",
                        gap: "0.5rem",
                    }}
                >
                {selectedOption?.icon && (
                    <span className="dropdown-icon">{selectedOption.icon}</span>
                )}
                        <span>{selectedOption?.label || placeholder}</span>
                </span>
                <span className={`dropdown-arrow ${isOpen ? "open" : ""}`}>&#9662;</span>
            </div>

            {isOpen && (
                <ul className="dropdown-list">
                    {options.map((option, index) => (
                        <li
                            key={index}
                            className="dropdown-item"
                            onClick={() => handleSelect(option)}
                        >
                            <span className="dropdown-icon">{option.icon}</span>
                            <span>{option.label}</span>
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );
};

export default DropdownComponent;
