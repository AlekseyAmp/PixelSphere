import React from 'react';

import styles from './Form.module.scss';

import Input from '../../Inputs/Input/Input';
import BlueButton from '../../Buttons/BlueButton/BlueButton';

function Form({ inputConfigs, buttonTitle, onSubmit }) {
  return (
    <form className={styles.form} onSubmit={onSubmit}>
      {inputConfigs.map((inputConfig, index) => (
        <Input
          key={index}
          title={inputConfig.title}
          type={inputConfig.type}
          name={inputConfig.name}
        />
      ))}
      <BlueButton type='submit' title={buttonTitle}/>
    </form>
  );
};

export default Form;