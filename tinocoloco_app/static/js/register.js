document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('registerForm');
    const inputs = form.querySelectorAll('input');
    const spinner = document.getElementById('spinner');
    const buttonText = document.getElementById('button-text');
    let password = '';

    // Obtener el token CSRF
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.startsWith(name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    const csrftoken = getCookie('csrftoken');

    // Validar email
    function isValidEmail(email) {
        return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
    }

    // Mostrar feedback
    function showFeedback(input, isValid, message) {
        const formGroup = input.closest('.form-group');
        const invalidFeedback = formGroup.querySelector('.invalid-feedback');
        const validFeedback = formGroup.querySelector('.valid-feedback');

        input.classList.remove('is-valid', 'is-invalid');
        input.classList.add(isValid ? 'is-valid' : 'is-invalid');

        if (isValid) {
            validFeedback.style.display = 'block';
            invalidFeedback.style.display = 'none';
            validFeedback.textContent = message;
        } else {
            invalidFeedback.style.display = 'block';
            validFeedback.style.display = 'none';
            invalidFeedback.textContent = message;
        }
    }

    // Validar campos
    inputs.forEach(input => {
        input.addEventListener('input', function () {
            const name = this.name;

            if (name === 'username') {
                const isValid = this.value.length >= 4;
                showFeedback(this, isValid, isValid ? 'Nombre de usuario válido' : 'Debe tener al menos 4 caracteres');
            }

            if (name === 'email') {
                const isValid = isValidEmail(this.value);
                showFeedback(this, isValid, isValid ? 'Email válido' : 'Email no válido');
            }

            if (name === 'password1') {
                password = this.value;
                const isValid = this.value.length >= 8;
                showFeedback(this, isValid, isValid ? 'Contraseña válida' : 'Debe tener al menos 8 caracteres');
            }

            if (name === 'password2') {
                const isValid = this.value === password;
                showFeedback(this, isValid, isValid ? 'Coinciden' : 'No coinciden');
            }
        });
    });

    // Muestra spinner y deshabilita el botón al enviar
    form.addEventListener('submit', function (e) {
        let isValid = true;
        inputs.forEach(input => {
            if (input.classList.contains('is-invalid')) {
                isValid = false;
            }
        });

        if (!isValid) {
            e.preventDefault();
            alert('Por favor, corrige los errores antes de enviar el formulario.');
        } else {
            buttonText.classList.add('d-none');
            spinner.classList.remove('d-none');
        }
    });
});

