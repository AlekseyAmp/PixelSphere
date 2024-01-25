import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

import { register_user } from '../../services/auth'
import { access_token } from '../../constants/token'

import ErrorBox from '../../components/ErrorBox/ErrorBox';
import Form from '../../components/Forms/Form/Form';
import styles from './Register.module.scss';

function Register() {
    const navigate = useNavigate();
    const isAuthorize = access_token
    const [error, setError] = useState(null);
    const [showError, setShowError] = useState(false);

    const inputConfigs = [
        { title: "Придумайте имя пользователя", type: 'text', name: 'login' },
        { title: "Придумайте пароль", type: 'password', name: 'password' },
    ]

    const handleRegisterUser = async (e) => {
        e.preventDefault();
        const login = e.target.login.value;
        const password = e.target.password.value;
        await register_user(login, password, setError, setShowError, navigate)
    };

    return (
        <div className={styles.login}>
            {isAuthorize ? (
                null
            ) : (
                <div className={`content`}>
                    <div className={`title center`}>Регистрация</div>
                    <div className={`center mt50px`}>
                        <Form
                            inputConfigs={inputConfigs}
                            buttonTitle='Зарегистрироваться'
                            onSubmit={handleRegisterUser}
                        />
                    </div>
                </div>
            )}
            {showError && <ErrorBox error={error} />}
        </div>
    )
}

export default Register;