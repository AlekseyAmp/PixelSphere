export const formatDate = (dateString) => {
  const options = {
    day: '2-digit',
    month: '2-digit',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit',
    timeZone: 'UTC',
  };

  const formattedDate = new Intl.DateTimeFormat('default', options).format(new Date(dateString));
  return formattedDate;
};
