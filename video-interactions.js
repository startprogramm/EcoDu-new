// Video interactions JavaScript
document.addEventListener('DOMContentLoaded', function () {
    // Like/Dislike functionality
    const likeBtn = document.getElementById('like-btn');
    const dislikeBtn = document.getElementById('dislike-btn');
    const likeCount = document.getElementById('like-count');
    const dislikeCount = document.getElementById('dislike-count');

    let liked = false;
    let disliked = false;

    if (likeBtn) {
        likeBtn.addEventListener('click', function () {
            if (!liked) {
                likeBtn.classList.add('liked');
                likeCount.textContent = parseInt(likeCount.textContent) + 1;
                liked = true;

                if (disliked) {
                    dislikeBtn.classList.remove('disliked');
                    dislikeCount.textContent = parseInt(dislikeCount.textContent) - 1;
                    disliked = false;
                }
            } else {
                likeBtn.classList.remove('liked');
                likeCount.textContent = parseInt(likeCount.textContent) - 1;
                liked = false;
            }
        });
    }

    if (dislikeBtn) {
        dislikeBtn.addEventListener('click', function () {
            if (!disliked) {
                dislikeBtn.classList.add('disliked');
                dislikeCount.textContent = parseInt(dislikeCount.textContent) + 1;
                disliked = true;

                if (liked) {
                    likeBtn.classList.remove('liked');
                    likeCount.textContent = parseInt(likeCount.textContent) - 1;
                    liked = false;
                }
            } else {
                dislikeBtn.classList.remove('disliked');
                dislikeCount.textContent = parseInt(dislikeCount.textContent) - 1;
                disliked = false;
            }
        });
    }

    // Comment submission
    const commentSubmit = document.querySelector('.comment-submit');
    const commentInput = document.querySelector('.comment-input');
    const commentsList = document.querySelector('.comments-list');

    if (commentSubmit && commentInput) {
        commentSubmit.addEventListener('click', function () {
            const commentText = commentInput.value.trim();

            if (commentText) {
                const newComment = document.createElement('div');
                newComment.className = 'comment-item';
                newComment.innerHTML = `
                    <div class="comment-header">
                        <div class="comment-avatar">S</div>
                        <span class="comment-author">Siz</span>
                        <span class="comment-date">Hozir</span>
                    </div>
                    <p class="comment-text">${commentText}</p>
                `;

                commentsList.insertBefore(newComment, commentsList.firstChild);
                commentInput.value = '';

                // Update comment count
                const commentsHeader = document.querySelector('.comments-header');
                const currentCount = parseInt(commentsHeader.textContent.match(/\d+/)[0]);
                commentsHeader.textContent = `Izohlar (${currentCount + 1})`;
            }
        });
    }

    // Quiz button
    const quizButton = document.querySelector('.quiz-button');
    if (quizButton) {
        quizButton.addEventListener('click', function () {
            alert('Test tez orada qo\'shiladi! Soon you will be able to take quizzes.');
        });
    }
});
