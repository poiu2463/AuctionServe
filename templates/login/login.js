const container = document.querySelector(".container"),
    signUp = document.querySelector(".signup-link"),
    login = document.querySelector(".login-link");

const togglePasswords = document.querySelectorAll('.icon-btn');

togglePasswords.forEach(function(togglePassword) {
    const passwordField = togglePassword.previousElementSibling;
    const showPasswordIcon = togglePassword.querySelector('.fa-eye');
    const hidePasswordIcon = togglePassword.querySelector('.fa-eye-slash');

    togglePassword.addEventListener('click', function() {
        const type = passwordField.getAttribute('type') === 'password' ? 'text' : 'password';
        passwordField.setAttribute('type', type);
        showPasswordIcon.style.display = type === 'password' ? 'block' : 'none';
        hidePasswordIcon.style.display = type === 'password' ? 'none' : 'block';
    });
});

signUp.addEventListener("click", () => {
    container.classList.add("active");
});
login.addEventListener("click", () => {
    container.classList.remove("active");
});