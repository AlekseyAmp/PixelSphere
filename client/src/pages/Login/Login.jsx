import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

import { login_user } from '../../services/auth'
import { access_token } from '../../constants/token'

import ErrorBox from '../../components/ErrorBox/ErrorBox';
import Form from '../../components/Forms/Form/Form';
import styles from './Login.module.scss';

function Login() {
    const navigate = useNavigate();
    const isAuthorize = access_token
    const [error, setError] = useState(null);
    const [showError, setShowError] = useState(false);

    const inputConfigs = [
        { title: "Логин", type: 'text', name: 'login' },
        { title: "Введите пароль", type: 'password', name: 'password' },
    ]

    const handleLoginSubmit = async (e) => {
        e.preventDefault();
        const login = e.target.login.value;
        const password = e.target.password.value;
        await login_user(login, password, setError, setShowError, navigate)
    };

    return (
        <div className={styles.login}>
            {isAuthorize ? (
                null
            ) : (
                <div className={`content`}>
                    <div className={`title center`}>Вход</div>
                    <div className={`center mt50px`}>
                        <Form
                            inputConfigs={inputConfigs}
                            buttonTitle='Войти'
                            onSubmit={handleLoginSubmit}
                        />
                    </div>
                </div>
            )}
            {showError && <ErrorBox error={error} />}
        </div>
    )
}

export default Login;