import React, { useState } from 'react';
import { useDropzone } from 'react-dropzone';
import styled from 'styled-components';

import { uploadPhoto } from '../services/photo';

import ErrorBox from '../components/ErrorBox/ErrorBox';
import SuccessBox from '../components/SuccessBox/SuccessBox';

const InputContainer = styled.div`
    margin-top: 30px;
    display: flex;
    flex-direction: column;
    label {
        font-family: 'Ubuntu';
        font-weight: 400;
        font-size: 16px;
        margin-bottom: 10px;
    }
    input, textarea {
        font-family: 'Ubuntu';
        font-weight: 400;
        font-size: 16px;
        background: #ffffff; /* Update with your color variables */
        border: 3px solid #cccccc; /* Update with your color variables */
        outline: none;
        border-radius: 10px;
        width: 280px;
        height: 34px; /* Adjust as needed */
        padding-left: 15px;
        transition: 0.2s;
        margin-bottom: 10px;
    }

    input:focus, textarea:focus {
        border: 3px solid #d88322; /* Update with your focus color */
    }
`;

const DragAndDropForm = styled.div`
    margin-top: 50px;
    border: 2px dashed #cccccc;
    border-radius: 10px;
    padding: 20px;
    text-align: center;
    cursor: pointer;
`;

const DragAndDropFile = () => {
    const [error, setError] = useState(null);
    const [success, setSuccess] = useState(null);
    const [showSuccessMessage, setShowSuccessMessage] = useState(false);
    const [showErrorMessage, setShowErrorMessage] = useState(false);
    const [title, setTitle] = useState("");
    const [description, setDescription] = useState("");

    const onDrop = async (acceptedFiles) => {
        const file = acceptedFiles[0];

        if (file) {
            uploadPhoto(file, title, description, setSuccess, setError, setShowSuccessMessage, setShowErrorMessage);
        }
    };

    const { getRootProps, getInputProps, isDragActive } = useDropzone({ onDrop });

    return (
        <div>
            {showSuccessMessage || showErrorMessage ? (
                <>
                    {success && <SuccessBox success={success} />}
                    {error && <ErrorBox error={error} />}
                </>
            ) : null}
            
            <InputContainer>
                <label>Заголовок:</label>
                <input type="text" value={title} onChange={(e) => setTitle(e.target.value)} />
            </InputContainer>
            
            <InputContainer>
                <label>Описание:</label>
                <textarea value={description} onChange={(e) => setDescription(e.target.value)} />
            </InputContainer>

            <DragAndDropForm {...getRootProps()} style={dropzoneStyle}>
                <input {...getInputProps()} />
                {isDragActive ? (
                    <p className={`dark-text`}>Перетащите файл сюда...</p>
                ) : (
                    <p className={`dark-text`}>Перетащите файл сюда или кликните, чтобы выбрать файл</p>
                )}
            </DragAndDropForm>
        </div>
    );
};

const dropzoneStyle = {
    border: '2px dashed #cccccc',
    borderRadius: '10px',
    padding: '20px',
    textAlign: 'center',
    cursor: 'pointer',
};

export default DragAndDropFile;
