import React from 'react';

import styles from './Input.module.scss';

function Input({ title, type, name, value, placeholder, onChange }) {
    return (
        <div className={styles.input}>
            <label htmlFor={name} className={`dark-text`}>{title}</label>

            <input
                type={type}
                name={name}
                value={value}
                onChange={onChange}
                placeholder={placeholder}
            />

        </div>
    )
}

export default Input;
