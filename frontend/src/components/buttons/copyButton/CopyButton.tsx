import React, { useState } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faCopy } from "@fortawesome/free-regular-svg-icons";
import styles from "./CopyButton.module.css";

interface CopyButtonProps {
    content: string; // Content to be copied to clipboard
    label?: string;  // Optional label to display next to the icon
    successMessage?: string; // Optional message to show after successful copy
}

const CopyButton: React.FC<CopyButtonProps> = ({ content, label = "Copy", successMessage = "Copied!" }) => {
    const [copied, setCopied] = useState(false);

    const handleCopy = async () => {
        try {
            await navigator.clipboard.writeText(content);
            setCopied(true);
            setTimeout(() => setCopied(false), 2000); // Reset copied state after 2 seconds
        } catch (err) {
            console.error("Failed to copy content: ", err);
        }
    };

    return (
        <button onClick={handleCopy} className={styles.copyButton} aria-label="Copy">
            <FontAwesomeIcon icon={faCopy} className={styles.icon} />
            {copied ? successMessage : label}
        </button>
    );
};

export default CopyButton;
