// Function to disable the submit button and show a spinner
function disableSubmitButton(event) {
    event.preventDefault(); // Prevent the default form submission for demonstration purposes

    const submitBtn = document.getElementById('submit-btn');
    const spinner = document.getElementById('spinner');
    const submitText = document.getElementById('submit-btn-text');

    submitBtn.disabled = true;
    submitText.classList.add('d-none');
    spinner.classList.remove('d-none');

    // Simulate a form submission delay
    setTimeout(() => {
        event.target.submit();
    }, 1000); // Submit the form after 1 second
}
