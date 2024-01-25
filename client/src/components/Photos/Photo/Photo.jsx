import React, { useState } from 'react';
import styles from './Photo.module.scss';

const Photo = ({ photo }) => {
  const [isHovered, setIsHovered] = useState(false);

  const handleMouseEnter = () => {
    setIsHovered(true);
  };

  const handleMouseLeave = () => {
    setIsHovered(false);
  };

  const truncatedTitle = photo.title.length > 6 ? `${photo.title.slice(0, 6)}...` : photo.title;

  return (
    <div className={`${styles.photoContainer} ${isHovered ? styles.hovered : ''}`} onMouseEnter={handleMouseEnter} onMouseLeave={handleMouseLeave}>
      <img
        className={styles.roundedPhoto}
        src={`data:image/jpeg;base64,${photo.image}`}
        alt={photo.title}
      />
      <div className={styles.overlay}>
        <p className={styles.likesComments}>
          <span className={`white-text`}>Лайков: {photo.likes}</span> |  <span className={`white-text`}>Комментариев: {photo.comments.length}</span>
        </p>
      </div>
      <div className={styles.photoContainerInfo}>
        <p className={`title`}>{truncatedTitle}</p>
        <p className={`dark-text ${styles.authorSeparator}`}>|</p>
        <p className={styles.author}>
          <span className={`small-text`}>Автор: {photo.author}</span>
        </p>
      </div>
    </div>
  );
};

export default Photo;
