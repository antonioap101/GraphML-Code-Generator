import React, {useEffect, useRef, useState} from 'react';
import styles from './RegexHighlighterComponent.module.css';
import CopyButton from "../../buttons/copyButton/CopyButton.tsx";
import {Card, CardContent} from "../../card/Card.tsx";

type RegexHighlighterProps = {
    onInputChange: (text: string) => void;
    regex: string;
}

const RegexHighlighter: React.FC<RegexHighlighterProps> = ({onInputChange, regex}) => {
    const textareaRef = useRef<HTMLTextAreaElement | null>(null);
    const canvasRef = useRef<HTMLCanvasElement | null>(null);
    const [text, setText] = useState<string>("");

    useEffect(() => {
        drawHighlights();
    }, [text, regex]);

    const handleInputChange = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
        const currentText = e.target.value;
        setText(currentText);
        onInputChange(currentText);
    };

    const drawHighlights = () => {
        const canvas = canvasRef.current;
        const textarea = textareaRef.current;

        if (!canvas || !textarea) return;

        const ctx = canvas.getContext("2d");
        if (!ctx) return;

        // Adjust canvas size to match the textarea
        canvas.width = textarea.offsetWidth;
        canvas.height = textarea.offsetHeight;
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        if (!regex) return;

        try {
            const re = new RegExp(regex, "g");
            ctx.fillStyle = "rgba(255,220,0,0.6)";
            ctx.font = getComputedStyle(textarea).font;

            const lineHeight = Number(getComputedStyle(textarea).lineHeight.replace("px", ""));
            console.warn("Lineheight:", lineHeight);

            const lines = text.split("\n");

            console.warn("Lines:", lines);
            let yOffset = 0;

            // If there is no regex, return
            if (!re) {
                console.error("No regex or invalid regex provided");
                return;
            }

            lines.forEach((line) => {
                let match;
                while ((match = re.exec(line)) !== null && match[0].length > 0) {
                    console.warn("Match:", match);

                    if (match.index === undefined || match.index === null || match[0] === undefined || match[0] === null || match[0].length === 0) {
                        console.error("No match index");
                        continue;
                    }
                    console.warn("Match:", match);

                    const beforeMatch = line.slice(0, match.index);
                    const xOffset = ctx.measureText(beforeMatch).width;
                    const matchWidth = ctx.measureText(match[0]).width;

                    // Draw the highlight
                    ctx.fillRect(xOffset, yOffset, matchWidth, lineHeight);
                }
                yOffset += lineHeight;
            });
        } catch (e) {
            console.error("Invalid regex:", e);
        }
    };

    return (
        <Card>
            <CardContent>
                <div className={styles.inputGroup + " " + styles.highlightContainer}>
                    <canvas ref={canvasRef} className={styles.highlightCanvas}/>
                    <textarea
                        ref={textareaRef}
                        className={styles.textArea}
                        value={text}
                        onChange={handleInputChange}
                        placeholder="Type your text here..."
                    />
                </div>
                <div className={`${styles.inputGroup} ${styles.regexInput}`}>
                    <label className={styles.label}>Used Regular Expression:</label>
                    <div className={styles.regexInputWrapper}>
                        <input
                            type="text"
                            className={styles.input}
                            value={regex}
                            onChange={() => {
                            }}
                            contentEditable={false}
                            placeholder="Here will display the regular expression used"
                        />
                        <CopyButton content={regex}/>
                    </div>
                </div>
            </CardContent>
        </Card>
    );
};

export default RegexHighlighter;
