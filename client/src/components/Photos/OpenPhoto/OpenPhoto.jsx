import React, { useState, useEffect } from 'react';

import styles from './OpenPhoto.module.scss';
import { access_token } from '../../../constants/token';
import { formatDate } from '../../../utils/dateFomat';
import { formatComment } from '../../../utils/commentFormat'
import { addCommentToPhoto, addLikeToPhoto, downloadPhoto } from '../../../services/photo';
import { getUserInfo } from '../../../services/user';

import Input from '../../Inputs/Input/Input';
import BlueButton from '../../Buttons/BlueButton/BlueButton';
import OrangeButton from '../../Buttons/OrangeButton/OrangeButton';
import ErrorBox from '../../ErrorBox/ErrorBox';

const OpenPhoto = ({ photo, onClose }) => {
  const [isOptionsMenuOpen, setIsOptionsMenuOpen] = useState(false);
  const isAuthorized = access_token;
  const [isLiked, setIsLiked] = useState(localStorage.getItem(`liked_${photo.id}`) === 'true');
  const [comment, setComment] = useState('');
  const [error, setError] = useState(null);
  const [showError, setShowError] = useState(false);
  const [username, setUsername] = useState('');


  useEffect(() => {
    if (isAuthorized) {
      getUserInfo()
        .then((data) => {
          setUsername(data.username);
        })
        .catch((error) => console.log(error));
    }
  }, [isAuthorized]);

  useEffect(() => {
    // Обновление состояния лайка при перезагрузке страницы
    setIsLiked(localStorage.getItem(`liked_${photo.id}`) === 'true');
  }, [photo.id]);

  const handleCommentChange = (event) => {
    setComment(event.target.value);
  };

  const handleAddComment = () => {
    if (isAuthorized) {
      const trimmedComment = comment.trim();
      if (trimmedComment !== '') {
        const newComment = { author: username, text: trimmedComment, created_at: Date.now() };
        const updatedComments = [...photo.comments, newComment];
        photo.comments = updatedComments;
        setComment('');
        addCommentToPhoto(photo.id, trimmedComment, setError, setShowError);
      } else {
        setError("Field 'text' cannot be empty");
        setShowError(true);
        setTimeout(() => {
          setShowError(false);
          setError(null);
        }, 2500);
      }
    } else {
      setError("You not authorized");
      setShowError(true);
      setTimeout(() => {
        setShowError(false);
        setError(null);
      }, 2500);
    }
  };

  const handleDownload = () => {
    downloadPhoto(photo.id);
  };

  const toggleOptionsMenu = () => {
    setIsOptionsMenuOpen(!isOptionsMenuOpen);
  };

  const handleAddLike = () => {
    if (isAuthorized) {
      if (!isLiked) {
        addLikeToPhoto(photo.id, setError, setShowError);
        photo.likes += 1;
        setIsLiked(true);
        localStorage.setItem(`liked_${photo.id}`, 'true');
      }
    } else {
      setError("You are not authorized");
      setShowError(true);
      setTimeout(() => {
        setShowError(false);
        setError(null);
      }, 2500);
    }
  };

  return (
    <>
      {showError && <ErrorBox error={error} />}
      <div className={styles.overlay}>
        <div className={styles.photoContainer}>
          <img
            src={`data:image/jpeg;base64,${photo.image}`}
            alt={photo.title}
          />
        </div>
        <div className={styles.photoInfo}>
          <div className={styles.title}>
            <span className={`title`}>{photo.title}</span>
            <span className={`dark-text`}>Автор: {photo.author}</span>
          </div>
          <span className={`small-text`}>Дата публикации: {formatDate(photo.created_at)}</span>
          <span className={`small-text ${styles.description}`}>{photo.description}</span>
          <div className={styles.likes}>
            <img
              src={!isLiked ? "../images/like.svg" : "../images/red_like.svg"}
              alt="like"
              onClick={handleAddLike}
            />
            <p className={`dark-text ${styles.likes}`}>{photo.likes}</p>
          </div>
          <div className={styles.commentsTitle}>
            <img src="../images/comment.svg" alt="Comment" />
            <h3 className={`small-text`}>Комментарии ({photo.comments.length})</h3>
          </div>
          <div className={styles.comments}>
            {photo.comments.slice().reverse().map((comment, index) => (
              <div key={index} className={styles.comment}>
                <strong className={`bold-text`}>{comment.author}</strong> | <span className={`small-text`}>{formatDate(comment.created_at)}</span>
                <p className={`dark-text`}>{formatComment(comment.text)}</p>
              </div>
            ))}
          </div>
          <div className={styles.commentInput}>
            <Input
              type="text"
              name="comment"
              value={comment}
              onChange={handleCommentChange}
            />
            <BlueButton
              title={`Отправить комментарий`}
              onClick={handleAddComment}
            />
          </div>
        </div>
        <div className={styles.optionsMenu}>
          <button className={styles.optionsButton} onClick={toggleOptionsMenu}>
            <img src="../images/ellipsis.svg" alt="Options" />
          </button>
          {isOptionsMenuOpen && (
            <div className={styles.optionsDropdown}>
              <ul>
                <li className={`link-text`} onClick={handleDownload}>Скачать фотографию</li>
              </ul>
            </div>
          )}
          <button className={styles.closeButton} onClick={onClose}>
            <span className={`gray-text`}>Закрыть</span>
          </button>
        </div>
      </div>
    </>
  );
};

export default OpenPhoto;