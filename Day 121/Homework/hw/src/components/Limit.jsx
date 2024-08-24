import React, { useState } from 'react';

export default function Limit() {
    const [text, setText] = useState('');
    const characterLimit = 100;

    const handleChange = (e) => {
    setText(e.target.value);
    };

    const warningMessage = text.length >= characterLimit - 10 ? `Warning: ${characterLimit - text.length} characters remaining`: '';

    return (
        <div>
            <textarea
                value={text}
                onChange={handleChange}
                maxLength={characterLimit}
                placeholder="Type here..."
            />
            <p>{warningMessage}</p>
            <p>{text.length}/{characterLimit} characters</p>
        </div>
    );
}