document.addEventListener("DOMContentLoaded", function () {
    // Login form submission
    document.getElementById("loginForm").addEventListener("submit", function (e) {
        e.preventDefault();
        const email = document.getElementById("loginEmail").value;
        const password = document.getElementById("loginPassword").value;

        const loginData = {
            email: email,
            password: password
        };

        fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(loginData),
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                window.location.href = 'employeePage.html';
            } else {
                alert('Login failed: ' + data.message);
            }
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    });

    // Sign-up form submission
    document.getElementById("signupForm").addEventListener("submit", function (e) {
        e.preventDefault();
        const username = document.getElementById("signupUsername").value;
        const email = document.getElementById("signupEmail").value;
        const password = document.getElementById("signupPassword").value;
        const confirmPassword = document.getElementById("signupConfirmPassword").value;

        if (password !== confirmPassword) {
            alert("Passwords do not match!");
            return;
        }

        const signupData = {
            username: username,
            email: email,
            password: password
        };

        fetch('/signup', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(signupData),
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                window.location.href = 'welcomePage.html';
            } else {
                alert('Sign-up failed: ' + data.message);
            }
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    });
});