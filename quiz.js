const quizData = {
    "plastik": {
        title: "Plastik ifloslanish bo'yicha test",
        questions: [
            {
                question: "Plastik butilkalar to'liq parchalanishi uchun qancha vaqt ketadi?",
                options: ["100 yil", "450 yil", "50 yil", "10 yil"],
                correct: 1
            },
            {
                question: "Har yili okeanga qancha plastik chiqindi tashlanadi?",
                options: ["1 million tonna", "8 million tonna", "100 ming tonna", "500 million tonna"],
                correct: 1
            },
            {
                question: "Plastik nima uchun dengiz hayvonlari uchun xavfli?",
                options: ["Ular uni oziq-ovqat deb o'ylashadi", "U suvni isitadi", "U juda og'ir", "U rangsiz"],
                correct: 0
            },
            {
                question: "Mikroplastiklar nima?",
                options: ["Katta plastik bo'laklari", "5 mm dan kichik plastik zarralari", "Qayta ishlangan plastik", "Plastik zavodlari"],
                correct: 1
            },
            {
                question: "Plastik ifloslanishni kamaytirishning eng yaxshi usuli qaysi?",
                options: ["Plastikni yoqish", "Bir martalik plastikdan voz kechish", "Plastikni ko'mish", "Dengizga tashlash"],
                correct: 1
            }
        ]
    },
    "ormonlar": {
        title: "O'rmonlar yo'qolishi bo'yicha test",
        questions: [
            {
                question: "O'rmonlar kesilishi nimaga olib keladi?",
                options: ["Havo tozalanishiga", "Tuproq eroziyasiga", "Yomg'ir ko'payishiga", "Daraxtlar o'sishiga"],
                correct: 1
            },
            {
                question: "Daraxtlar bizga nima beradi?",
                options: ["Zaharli gaz", "Kislorod", "Plastik", "Chang"],
                correct: 1
            },
            {
                question: "Dunyodagi eng katta tropik o'rmon qaysi?",
                options: ["Amazonka", "Tayga", "Sibir", "Kongo"],
                correct: 0
            },
            {
                question: "Daraxtlar nimani yutadi?",
                options: ["Kislorod", "Karbonat angidrid", "Azot", "Geliy"],
                correct: 1
            },
            {
                question: "O'rmonlarni saqlash uchun nima qilishimiz kerak?",
                options: ["Ko'proq qog'oz ishlatish", "Daraxt ekish", "O'rmonda olov yoqish", "Daraxtlarni kesish"],
                correct: 1
            }
        ]
    },
    "havo": {
        title: "Havo ifloslanishi bo'yicha test",
        questions: [
            {
                question: "Havoni eng ko'p nima ifloslantiradi?",
                options: ["Daraxtlar", "Avtomobillar va zavodlar", "Yomg'ir", "Quyosh nuri"],
                correct: 1
            },
            {
                question: "Smog nima?",
                options: ["Toza havo", "Tutun va tuman aralashmasi", "Yomg'irli bulut", "Kuchli shamol"],
                correct: 1
            },
            {
                question: "Havo ifloslanishi qaysi kasalliklarni keltirib chiqaradi?",
                options: ["Nafas yo'llari kasalliklari", "Oshqozon og'rig'i", "Tish og'rig'i", "Soch to'kilishi"],
                correct: 0
            },
            {
                question: "Ozon qatlami nimadan himoya qiladi?",
                options: ["Yomg'irdan", "Ultrabinafsha nurlardan", "Sovuqdan", "Shamoldan"],
                correct: 1
            },
            {
                question: "Havoni tozalashga nima yordam beradi?",
                options: ["Zavodlar", "Daraxtlar va o'simliklar", "Avtomobillar", "Binolar"],
                correct: 1
            }
        ]
    },
    "suv": {
        title: "Suv ifloslanishi bo'yicha test",
        questions: [
            {
                question: "Suvni ifloslantiruvchi asosiy manba nima?",
                options: ["Yomg'ir suvi", "Sanoat chiqindilari", "Tog' jinslari", "Baliqlar"],
                correct: 1
            },
            {
                question: "Ichimlik suvining atigi necha foizi yerda mavjud?",
                options: ["1%", "10%", "50%", "70%"],
                correct: 0
            },
            {
                question: "Suvni tejash uchun nima qilish kerak?",
                options: ["Kranni ochiq qoldirish", "Keraksiz vaqtda suvni o'chirish", "Suvni ko'p ishlatish", "Daryolarni ifloslantirish"],
                correct: 1
            },
            {
                question: "Ifloslangan suv nimaga olib keladi?",
                options: ["Salomatlik", "Yuqumli kasalliklar", "Toza havo", "Boylik"],
                correct: 1
            },
            {
                question: "Suvni filtrlaydigan tabiiy vosita nima?",
                options: ["Tuproq va o'simliklar", "Plastik", "Temir", "Asfalt"],
                correct: 0
            }
        ]
    },
    "yovvyi": {
        title: "Yovvoyi tabiat bo'yicha test",
        questions: [
            {
                question: "Qizil kitob nima uchun kerak?",
                options: ["Kitob o'qish uchun", "Yo'qolib borayotgan turlarni himoya qilish uchun", "Rasm chizish uchun", "Sotish uchun"],
                correct: 1
            },
            {
                question: "Ekotizim nima?",
                options: ["Faqat hayvonlar", "Faqat o'simliklar", "Tirik organizm va ularning muhiti", "Shaharlar"],
                correct: 2
            },
            {
                question: "Biologik xilma-xillik nega muhim?",
                options: ["Muhim emas", "Tabiat muvozanati uchun", "Faqat hayvonot bog'i uchun", "Uy hayvonlari uchun"],
                correct: 1
            },
            {
                question: "Qaysi hayvon yo'qolib ketish xavfi ostida?",
                options: ["Qor barsi", "Mushuk", "Tovuq", "Ot"],
                correct: 0
            },
            {
                question: "Biz tabiatga qanday yordam bera olamiz?",
                options: ["Unga zarar yetkazib", "Uni asrab-avaylab", "Ov qilib", "Daraxtlarni kesib"],
                correct: 1
            }
        ]
    }
};

document.addEventListener('DOMContentLoaded', () => {
    // Robust detection: Check if URL contains any of our keys
    const currentUrl = window.location.href.toLowerCase();
    let currentKey = null;

    // Find matching key
    for (const key of Object.keys(quizData)) {
        if (currentUrl.includes(key)) {
            currentKey = key;
            break;
        }
    }

    console.log("Detected Quiz Key:", currentKey);

    // Get quiz data for current page
    const currentQuiz = currentKey ? quizData[currentKey] : null;

    if (!currentQuiz) {
        console.error("No quiz data found for URL:", currentUrl);
        return;
    }

    // Quiz Elements
    const quizModal = document.getElementById('quiz-modal');
    const quizTitle = document.querySelector('.quiz-title');
    const quizContent = document.querySelector('.quiz-content');
    const quizProgress = document.querySelector('.progress-fill');
    const questionCounter = document.querySelector('.question-counter');
    const btnNext = document.querySelector('.quiz-btn-next');
    const btnClose = document.querySelector('.quiz-close');
    const quizBtn = document.querySelector('.quiz-button');

    let currentQuestionIndex = 0;
    let score = 0;
    let selectedOptionIndex = null;

    // Initialize
    if (quizBtn) {
        // Remove old alert listener
        const newBtn = quizBtn.cloneNode(true);
        quizBtn.parentNode.replaceChild(newBtn, quizBtn);

        newBtn.addEventListener('click', openQuiz);
    }

    if (btnClose) {
        btnClose.addEventListener('click', closeQuiz);
    }

    // Also Close on clicking Result Close button or Retry
    document.addEventListener('click', (e) => {
        if (e.target.classList.contains('btn-close')) {
            closeQuiz();
        }
        if (e.target.classList.contains('btn-retry')) {
            resetQuiz();
        }
    });

    function openQuiz() {
        quizModal.classList.add('active');
        document.body.style.overflow = 'hidden';
        quizTitle.textContent = currentQuiz.title;
        resetQuiz();
    }

    function closeQuiz() {
        quizModal.classList.remove('active');
        document.body.style.overflow = '';
    }

    function resetQuiz() {
        currentQuestionIndex = 0;
        score = 0;
        showQuestion();
    }

    function showQuestion() {
        const question = currentQuiz.questions[currentQuestionIndex];
        selectedOptionIndex = null;

        // Update Progress
        const progress = ((currentQuestionIndex) / currentQuiz.questions.length) * 100;
        quizProgress.style.width = `${progress}%`;

        // Update Counter
        questionCounter.textContent = `${currentQuestionIndex + 1}-savol / ${currentQuiz.questions.length}`;

        // Render Options
        let optionsHtml = '';
        question.options.forEach((opt, index) => {
            optionsHtml += `<div class="quiz-option" data-index="${index}">${opt}</div>`;
        });

        const html = `
            <div class="question-text">${question.question}</div>
            <div class="quiz-options">
                ${optionsHtml}
            </div>
            <div class="quiz-footer">
                <span class="question-counter">${currentQuestionIndex + 1}-savol / ${currentQuiz.questions.length}</span>
                <button class="quiz-btn-next" disabled>Keyingi</button>
            </div>
        `;

        quizContent.innerHTML = html;

        // Add Event Listeners
        const options = document.querySelectorAll('.quiz-option');
        const nextBtn = document.querySelector('.quiz-btn-next');

        options.forEach(opt => {
            opt.addEventListener('click', () => {
                if (selectedOptionIndex !== null) return; // Already answered

                const index = parseInt(opt.getAttribute('data-index'));
                selectedOptionIndex = index;

                // Show Correct/Wrong
                if (index === question.correct) {
                    opt.classList.add('correct');
                    score++;
                } else {
                    opt.classList.add('wrong');
                    options[question.correct].classList.add('correct');
                }

                nextBtn.removeAttribute('disabled');

                if (currentQuestionIndex === currentQuiz.questions.length - 1) {
                    nextBtn.textContent = 'Natijani ko\'rish';
                }
            });
        });

        nextBtn.addEventListener('click', () => {
            currentQuestionIndex++;
            if (currentQuestionIndex < currentQuiz.questions.length) {
                showQuestion();
            } else {
                showResults();
            }
        });
    }

    function showResults() {
        // Complete Progress Bar
        quizProgress.style.width = '100%';

        const percentage = Math.round((score / currentQuiz.questions.length) * 100);
        let message = '';
        let icon = '';

        if (percentage >= 80) {
            message = 'Tabriklaymiz! Ajoyib natija! 🎉';
            icon = '🏆';
        } else if (percentage >= 60) {
            message = 'Yaxshi, lekin yanada yaxshiroq bo\'lishi mumkin! 👍';
            icon = '⭐';
        } else {
            message = 'Videoni qayta ko\'rib chiqing va yana urinib ko\'ring. 💪';
            icon = '📚';
        }

        const html = `
            <div class="quiz-results">
                <div class="result-icon">${icon}</div>
                <h2 class="result-score">${score} / ${currentQuiz.questions.length}</h2>
                <div class="result-message">${message} (${percentage}%)</div>
                <div class="result-actions">
                    <button class="btn-retry">Qayta urinish</button>
                    <button class="btn-close">Yopish</button>
                </div>
            </div>
        `;

        quizContent.innerHTML = html;
    }
});
