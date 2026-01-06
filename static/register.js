// Password visibility toggle
const pwToggle = document.querySelector('.pw-toggle');
if (pwToggle) {
  pwToggle.addEventListener('click', () => {
    const pw = document.getElementById('id_password');
    const icon = pwToggle.querySelector('i');
    if (pw.type === 'password') {
      pw.type = 'text';
      icon.classList.remove('fa-eye');
      icon.classList.add('fa-eye-slash');
    } else {
      pw.type = 'password';
      icon.classList.remove('fa-eye-slash');
      icon.classList.add('fa-eye');
    }
  });
}

// Form submission (Django handles the actual registration)
const form = document.getElementById('register-form');
if (form) {
  form.addEventListener('submit', function(e) {
    const password = document.getElementById('id_password').value;
    const confirmPassword = document.getElementById('id_password_confirm').value;
    
    if (password !== confirmPassword) {
      e.preventDefault();
      const errorDiv = document.createElement('div');
      errorDiv.className = 'alert alert-danger';
      errorDiv.textContent = 'Parollar mos kelmadi';
      form.insertBefore(errorDiv, form.firstChild);
    }
  });
}
