export const formatComment = (comment) => {
  const maxCommentLength = 30;

  if (comment.length <= maxCommentLength) {
    return comment;
  }

  const truncatedComment = comment.substring(0, maxCommentLength);
  const ellipsis = '...';

  return (
    <span>
      {truncatedComment}
      <span className={`ellipsis`} onClick={() => alert(comment)}>
        {ellipsis}
      </span>
    </span>
  );
};
